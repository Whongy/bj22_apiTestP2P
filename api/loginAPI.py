import app
import requests



class loginAPI():

    def __init__(self):
        self.getImgCode_url = app.BASE_URL + '/common/public/verifycode1/'
        self.getSmsCode_url = app.BASE_URL + '/member/public/sendSms'
        self.register_url = app.BASE_URL + "/member/public/reg"
        self.login_url = app.BASE_URL + "/member/public/login"

    def getImgCode(self,session,num):
        url = self.getImgCode_url + num
        response = session.get(url)

        return response

    def getSmsCode(self,session,phone,imgVerifyCode):
        data = {'phone':phone,'imgVerifyCode':imgVerifyCode,'type':'reg'}

        response = session.post(self.getSmsCode_url,data=data)

        return response

    def register(self,session,phone,pwd,imgVerifyCode='8888',phoneCode='666666',dyServer='on',invitePhone=''):
        data ={
            "phone":phone,
            "password":pwd,
            "verifycode":imgVerifyCode,
            "phone_code":phoneCode,
            "dy_server":dyServer,
            "invite_phone":invitePhone
        }
        response = session.post(self.register_url,data=data)
        return response

    def login(self,session,phone='13033447711',pwd='test123'):
        data = {
            "keywords":phone,
            "password":pwd,
        }
        response = session.post(self.login_url,data=data)
        return response






