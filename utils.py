import json
import logging,pymysql
from requests import request
from bs4 import BeautifulSoup
import app



def assert_utils(self,response,status_code,status,desc):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(status, response.json().get("status"))
    self.assertEqual(desc, response.json().get("description"))


def request_third_api(form_data):
    soup = (form_data,"html.parser")
    third_url = soup.form['action']
    logging.info('third request ur ={}'.format(third_url))
    data = {}
    for input in  soup.findall('input'):
        data.setdefault(input['name'],input['value'])
    logging.info("third request data = {}".format(data))

    response = request.post(third_url,data=data)
    logging.info("third request data = {}".format(data))
    return response


class DButils:
    @classmethod
    def get_conn(cls,db_name):
        conn = pymysql.connect(app.BASE_URL,app.DB_USERNAME,app.DB_PASSWORD,db_name,autocommit=True)
        return conn

    @classmethod
    def close(cls,cursor,conn):
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    @classmethod
    def delete(cls,db_name,sql):
        try:
            conn = cls.get_conn(db_name)
            cursor = conn.cursor()
            cursor.execute(sql)
        except Exception as e :
            conn.rollback()
        finally:
            cls.close(cursor,conn)


def read_imgVerify_data(file_name):
    file = app.BASE_DIR + "/data/" + file_name
    test_case_data = []
    with open(file,encoding="utf-8") as f :
        verify_data = json.load(f)
        test_data_list = verify_data.get("test_get_img_verify_code")
        for test_data in test_data_list:
            test_case_data.append([test_data.get("type"),test_data.get("status_code")])
    print("json data={}".format(test_case_data))
    return test_case_data


def read_register_data(file_name):
    file =app.BASE_DIR + "/data/"+file_name
    test_case_data =[]
    with open(file, encoding="utf-8") as f:
        #将JSON数据格式 转换为字典格式
        register_data = json.load(f)
        #获取所有测试数据的列表
        test_data_list = register_data.get("test_register")
        #依次读取测试数据 列表中的每一条，并进行相应字段提取
        for test_data in test_data_list:
            test_case_data.append((test_data.get("phone"),test_data.get("pwd"),test_data.get("imgVerifyCode"),test_data.get("phoneCode"),test_data.get("dyServer"),test_data.get("invite_phone"),test_data.get("status_code"),test_data.get("status"),test_data.get("description")))
        print("test_case_data = {}".format(test_data_list))
        return test_case_data

#定义统一的读取所有参数文件的方法
def read_param_data(filename,method_name,param_names):

    #filename: 参数数据文件的文件名
    #method_name: 参数数据文件中定义的测试数据列表的名称， 如 test_get_img_verify_code
    #
    #param_name  参数数据文件一组测试数据中所有的参数组成的字符串,如：type,status_code

    #获取测试数据的文件的文件路径
    file = app.BASE_DIR + "/data/" + filename
    test_case_data = []
    with open(file,encoding="utf-8")as f:
        #将JSON字符串转换为字典格式
        file_data = json.load(f)
    #获取所有测试数据的列表
        test_data_list = file_data.get(method_name)
        for test_data in test_data_list:
            # 将test_data对应的一组测试数据，全部读取出来，并生成一个列表
            test_params =[]
            for param in param_names.split(","):
            #依次获取同一组测试数据中的每个参数的值，添加到test_params中,形成一个列表
                test_params.append(test_data.get(param))
            #每完成一组测试数据的读取，就添加到test_case_data后, 直到所有的测试数据读取完成
            test_case_data.append(test_params)
    print("test_case_data={}".format(test_case_data))
    return test_case_data












