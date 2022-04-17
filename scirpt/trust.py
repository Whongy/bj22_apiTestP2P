import unittest
import logging
from random import random

import requests
from bs4 import BeautifulSoup

from api.loginAPI import loginAPI
from api.trustAPI import trustAPI
from utils import assert_utils ,request_third_api


class trust(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = loginAPI()
        self.trust_api = trustAPI()
        self.session = requests.Session()


    def tearDown(self) -> None:
        self.session.close()
        #开户请求
    def test01_trust_request(self):
        #1 认证通过得账号登录
        response =  self.login_api.login(self.session)
        logging.info("login response={}".format(response.json()))
        assert_utils(self,response,200,200,"登录成功")
        #发送开户请求
        response = self.trust_api.trust_register(self.session)
        logging.info("trust register response={}".format(response.json()))

        self.assertEqual(200,response.status_code)
        self.assertEqual(200,response.json().get("status"))

        # 发送第三方 开户请求
        form_data = response.json().get('description').get("form")
        logging.info("form resposne= {}".format(form_data))

        #解析form表单中得内容  并提取第三请求得参数
        soup = BeautifulSoup(form_data,'html.parser')
        third_url = soup.form['action']
        logging.info("third request url={}".format(third_url))



        data = {}

        for input in soup.findAll("input"):
            data.setdefault(input['name'],input['value'])
        logging.info("third request data={}".format(data))


        #发送第三方请求
        response =requests.post(third_url,data=data)
        self.assertEqual(200,response.status_code)
        self.assertEqual('UserRegister OK',response.text)

    def recharge(self):
        #1 登录成功
        # 1 认证通过得账号登录
        response = self.login_api.login(self.session)
        logging.info("login response={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")
        #2  获取充值验证码
        r = random()
        response =self.trust_api.get_recharge_verify_code(self.session,str(r))
        logging.info("get recharge verify code response={}".format(response.text))
        self.assertEqual(200,response.status_code)
        #3   发送充值方式
        response =self.trust_api.recharge(self.session,'10000')
        logging.info("recharge response = {} ".format(response.json()))
        self.assertEqual(200,response.status_code)
        self.assertEqual(200,response.json().get("status"))
        #4   发送第三方充值

        form_data = response.json().get('description').get("form")
        logging.info("form resposne= {}".format(form_data))

        response =  request_third_api(form_data)
        self.assertEqual('NetSave OK',response.text)


