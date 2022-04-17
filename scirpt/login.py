import logging
import unittest
from api.loginAPI import loginAPI
import requests
import random
from utils import assert_utils


class login(unittest.TestCase):

    phone1 = '13033447711'
    phone2 = '13033447712'

    phone3 = '13012332174'
    phone4 = '13012362174'
    imgCODE="8888"
    smsCode="666666"
    pwd = 'test123'
    noExistPhone = '1300000000'

    def setUp(self) -> None:

        self.login_api = loginAPI()
        self.session = requests.Session()
    def tearDown(self) -> None:
        self.session.close()

    def test01_get_img_code_random_float(self):

        r = random.random()

        #定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session,str(r))

        self.assertEqual(200,response.status_code)
        #接收返回结果 ，断言


    def test02_get_img_code_random_int(self):
        r = random.randint(10000,900000)

        response = self.login_api.getImgCode(self.session,str(r))

        self.assertEqual(200,response.status_code)

    def test03_get_img_code_paramIsNull(self):
        #r = random.randint(10000, 900000)

        response = self.login_api.getImgCode(self.session, "")

        self.assertEqual(404, response.status_code)

    def test04_get_img_code_randomChar(self):
        r = random.sample("fdsjhkgqwe312",8)
        rand = ''.join(r)
        logging.info(rand)

        response = self.login_api.getImgCode(self.session,rand)

        self.assertEqual(400, response.status_code)

    def test05_get_sms_code_success(self):
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)



        response = self.login_api.getSmsCode(self.session,self.phone1,self.imgCODE)
        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self,response,200,200,"短信发送成功")




        # self.assertEqual(200,response.status_code)
        # self.assertEqual(200,response.json().get("status"))
        # self.assertEqual("短信发送成功",response.json().get("description"))


    def test06_get_sms_code_wrong_img_code(self):
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)

        error_code ='1234'
        response =self.login_api.getSmsCode(self.session,self.phone1,error_code)
        assert_utils(self,response,200,100,"图片验证码错误")

    def test07_get_sms_code_is_null(self):
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)


        response = self.login_api.getSmsCode(self.session,self.phone1,'')
        assert_utils(self,response,200,100,'图片验证码错误')

    def test08_get_sms_code_phone_is_null(self):
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)

        response = self.login_api.getSmsCode(self.session,'',self.imgCODE)
        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self,response,200,100,None)

    def test09_get_sms_code_no_img_verify(self):
        response = self.login_api.getSmsCode(self.session,self.phone1,self.imgCODE)


        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self, response, 200, 100, "图片验证码错误")


    #输入必填项 注册成功
    def test10_register_success_param_must(self):
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

        #3 成功注册-输入必填项
        response = self.login_api.register(self.session,self.phone1,self.pwd)

        #response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        logging.info("get register response={}".format(response.json()))
        #对结果进行断言
        assert_utils(self,response,200,200,"注册成功")

    #输入所有项，注册成功
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


    def test12_register_phone_is_exist(self):
        # 成功获取验证码
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)

        response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        # 成功获取短信验证马

        # 3 注册失败-手机号码已存在
        response = self.login_api.register(self.session, self.phone1, self.pwd)

        # response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        logging.info("get register response={}".format(response.json()))
        # 对结果进行断言
        assert_utils(self, response, 200, 100, "手机已存在!")

    def test13_register_password_is_null(self):
        # 成功获取验证码
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)

        response = self.login_api.getSmsCode(self.session, self.phone3, self.imgCODE)
        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        # 成功获取短信验证马

        # 3 注册失败-手机号码已存在
        response = self.login_api.register(self.session, self.phone3, self.pwd)

        # response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        logging.info("get register response={}".format(response.json()))
        # 对结果进行断言
        assert_utils(self, response, 200, 100, "密码不能为空")
    def test14_register_img_code_is_wrong(self):
        # 成功获取验证码
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)

        response = self.login_api.getSmsCode(self.session, self.phone4, self.imgCODE)
        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        # 3 注册失败-图品验证码错误
        response = self.login_api.register(self.session, self.phone4, self.pwd,'1234')

        # response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        logging.info("get register response={}".format(response.json()))
        assert_utils(self, response, 200, 100, "验证码错误!")

    def test15_register_sms_code_wrong(self):
        # 成功获取验证码
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)

        response = self.login_api.getSmsCode(self.session, self.phone4, self.imgCODE)
        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        # 3 注册失败-短信 验证码错误
        response = self.login_api.register(self.session, self.phone4, self.pwd,phoneCode='123456')

        # response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        logging.info("get register response={}".format(response.json()))
        assert_utils(self, response, 200, 100, "验证码错误")


        #注册失败- 不同意 注册协议

    def test16_register_noAgreeProtcol(self):
        # 成功获取验证码
        r = random.random()

        # 定义参数
        # 调用接口类的接口
        response = self.login_api.getImgCode(self.session, str(r))

        self.assertEqual(200, response.status_code)

        response = self.login_api.getSmsCode(self.session, self.phone4, self.imgCODE)
        logging.info("get sms code response={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        #注册失败- 不同意 注册协议
        response = self.login_api.register(self.session, self.phone4, self.pwd,dyServer='off')

        # response = self.login_api.getSmsCode(self.session, self.phone1, self.imgCODE)
        logging.info("get register response={}".format(response.json()))
        assert_utils(self, response, 200, 100, "请同意我们的条款")

    #登录成功
    def test17_login_success(self):
        response = self.login_api.login(self.session,self.phone1,self.pwd)
        assert_utils(self,response,200,200,"登录成功")
    #挡路失败-用户名不存在
    def test18_login_phone_no_exist(self):

        response = self.login_api.login(self.session, self.noExistPhone, self.pwd)
        assert_utils(self, response, 200, 100, "用户不存在")









