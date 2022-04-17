import logging
import unittest
import random
from time import sleep
import requests
from parameterized import parameterized
from api.loginAPI import loginAPI
from utils import assert_utils, read_imgVerify_data,read_register_data,read_param_data


class login(unittest.TestCase):

    phone1 ='13033447711'
    phone2 ='13033447712'
    phone3 ='13033447713'
    phone4 ='13033447714'
    pwd = 'test123'
    imgCODE = "8888"
    smsCode = "666666"

    def setUp(self) -> None:

        self.login_api = loginAPI()
        self.session = requests.Session()
    def tearDown(self) -> None:
        self.session.close()

    @parameterized.expand(read_param_data("imgVerify.json","test_get_img_verify_code","type,status_code"))
    def test01_get_img_code(self,type,status_code):
        r =''
        if type == 'float':
            r = random.random()
        elif type =='int':
            r = random.randint(1000000,90000000)
        elif type =='char':
            r=''.join(random.sample('abcdefghijklmnopqrstovwxyz',8))

        response = self.login_api.getImgCode(self.session,r)
        logging.info("r={} response={}".format(r,response))

        self.assertEqual(status_code,response.status_code)


    def test09_get_sms_code_no_img_verify(self):
        response = self.login_api.getSmsCode(self.session,self.phone1,self.imgCODE)


        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self, response, 200, 100, "图片验证码错误")


    #输入必填项 注册成功
    @parameterized.expand(read_param_data("register.json","test_register","phone,pwd,imgVerifyCode,phoneCode,dyServer,invitePhone,status_code,status,description"))
    def test10_register(self,phone,pwd,imgVerifyCode,phoneCode,dyServer,invitePhone,status_code,status,description):
        #获取图片验证码成功
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)
        # 获取短信验证码成功
        response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")
        # 使用个参数化的测试数据进行注册，并返回对应结果
        # 发送注册请求
        response = self.login_api.register(self.session,phone,pwd,imgVerifyCode,phoneCode,dyServer,invitePhone)
        logging.info("register response = {}".format(response.json()))

        # 对收到的相应进行断言
        assert_utils(self,response,status_code,status,description)




        # 成功获取验证码
        # r = random.random()
        #
        # # 定义参数
        # # 调用接口类的接口
        # response = self.login_api.getImgCode(self.session, str(r))
        #
        # self.assertEqual(200, response.status_code)
        #
        # response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        # logging.info("get sms code response={}".format(response.json()))
        # assert_utils(self, response, 200, 200, "短信发送成功")
        #
        # #成功获取短信验证马
        #
        # #3 成功注册-输入必填项
        # response = self.login_api.register(self.session,self.phone1,self.pwd)
        #
        # #response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        # logging.info("get register response={}".format(response.json()))
        # #对结果进行断言
        # assert_utils(self,response,200,200,"注册成功")












    def test11_register_success_param_all(self):
        #成功获取验证码
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)

        response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        #成功获取短信验证马

        #3 成功注册-输入所有项
        response = self.login_api.register(self.session,self.phone2,self.pwd,invitePhone='13012345678')


