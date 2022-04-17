# 初始化日志配置
import logging
import os
from logging import handlers

# BASE_URL = "http://ihrm-test.itheima.net/#/login/api/sys"
BASE_URL = "http://user-p2p-test.itheima.net"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_URL ='52.83.144.39'
DB_USERNAME ='root'
DB_PASSWORD ='itcast_p2p_20191228'
DB_MEMBER ='czbk_member'
DB_FINANCE = 'czbk_finance'

def init_log_config():
    #创建日志器
    logger = logging.getLogger()

    #设置日志打印级别
    logger.setLevel(logging.INFO)


    #创建控制台处理器
    sh = logging.StreamHandler()


   # logfile = BASE_DIR + "log" + os.sep + "log{}.log".format("%Y%m%D %H%M%S")
    logfile = BASE_DIR + os.sep+"log"+os.sep+"p2p.log"

    fh = logging.handlers.TimedRotatingFileHandler(logfile, when="M", interval=5, backupCount=5,
                                                   encoding="UTF-8")

    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d]- %(message)s'

    formatter = logging.Formatter(fmt)

    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)


    # #创建文件处理器
    # log_path = BASE_DIR +"/log/p2p.log"
    # fh = logging.handlers.TimedRotatingFileHandler(log_path,when="midnight",interval=1,backupCount=7,encoding="YTF-8")
    #
    # #创建格式化器
    #
    # f = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d]- %(message)s'
    # formatter = logging.Formatter(f)
    #
    # #把格式化添加到处理器中
    # sh.setFormatter(formatter)
    # fh.setFormatter(formatter)
    #
    #
    # #把处理器添加到日志中
    # logger.addHandler(sh)
    # logger.addHandler(fh)