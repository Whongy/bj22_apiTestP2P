import pymysql
import unittest
import parameterized
from scirpt.login import login
import app
import time
from lib.HTMLTestRunner import HTMLTestRunner
suite =unittest.TestSuite()
suite.addTest(unittest.makeSuite(login))

report_file = app.BASE_DIR + "/report/report{}.html" .format(time.strftime("%Y%m%d-%H%M%S"))

with open(report_file,'wb') as  f:
    runner = HTMLTestRunner(f, title="p2p金融项目接口测试",description='test')
    runner.run(suite)



