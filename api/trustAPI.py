import app



class trustAPI():
    def __init__(self):
        self.trust_register_url = app.BASE_URL + '/trust/trust/register'
        self.get_recharge_verify_code_url = app.BASE_URL + '/common/public/verifycode/'


    def trust_register(self,session):
        response = session.post(self.trust_register_url)
        return response

    def get_recharge_verify_code(self,session,r):
        url = self.get_recharge_verify_code_url +r
        response = session.get(url)
        return response

    def recharge(self,session,amount,code='8888'):
        data = {"paymentType":"chinapnrTrust",
                "formStr":"reForn",
                "amount":"amount",
                "valicode":"8888"
                }
        response = session.post(self.recharge_url,data=data)
        return response