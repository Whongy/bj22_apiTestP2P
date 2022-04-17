import logging
import unittest
import requests
from api.approveAPI import approveAPI
from api.loginAPI import loginAPI
from utils import assert_utils


class approve(unittest.TestCase):
    phone1 = '13033447711'
    phone2 = '13033447712'

    realname = '张三'
    cardId = '110117199003070995'
    def setUp(self) -> None:
        self.login_api = loginAPI()
        self.approve_api =approveAPI()
        self.session = requests.Session()
    def tearDown(self) -> None:
        self.session.close()


    def test01_approve_success(self):
        # 用户登录
        response = self.login_api.login(self.session,self.phone1)
        logging.info('login response={}'.format(response.json()))
        assert_utils(self,response,200,200,"登录成功")

        #发送认证请求
        response =self.approve_api.approve(self.session,self.realname,self.cardId)
        assert_utils(self,response,200,200,"提交成功!")

    def test02_approve_isNull(self):# 用户登录
        response = self.login_api.login(self.session,self.phone1)
        logging.info('login response={}'.format(response.json()))
        assert_utils(self,response,200,200,"登录成功")

        #发送认证请求
        response =self.approve_api.approve(self.session,"",self.cardId)
        logging.info('approve response={}'.format(response.json()))
        assert_utils(self,response,200,100,"姓名不能为空")


    def test03_approve_cardIdIsNull(self):# 用户登录
        response = self.login_api.login(self.session,self.phone2)
        logging.info('login response={}'.format(response.json()))
        assert_utils(self,response,200,200,"登录成功")

        #发送认证请求
        response =self.approve_api.approve(self.session,self.realname,"")
        logging.info('approve response={}'.format(response.json()))
        assert_utils(self,response,200,100,"身份证号不能为空")

    def test04_get_approve(self):
        response = self.login_api.login(self.session, self.phone1)
        logging.info('login response={}'.format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")

        response = self.approve_api.getApprove(self.session)
        logging.info('approve response={}'.format(response.json()))

        self.assertEqual(200,response.status_code)

