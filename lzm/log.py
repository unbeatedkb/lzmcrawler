# coding: utf-8

'''
    日志模块
'''

import logging
import datetime
from lzm.settings import LOGS_PATH
from lzm.settings import MAX_LOGS
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def cleanlog():
    while len(os.listdir(LOGS_PATH)) >= MAX_LOGS:
        filelist = os.listdir(LOGS_PATH)
        latesttime = 9999999999
        latestfile = None
        for i in range(len(filelist)):
            if os.path.getctime(LOGS_PATH+filelist[i]) < latesttime:
                latesttime = os.path.getctime(LOGS_PATH+filelist[i])
                latestfile = filelist[i]
            else:
                pass
        os.remove(LOGS_PATH+latestfile)


def getlogname():
    filetime = datetime.datetime.now().strftime('%Y_%m_%d_%H')
    filname = LOGS_PATH + str(filetime)
    return filname


def getlogger():
    if not os.path.exists(LOGS_PATH):
        os.mkdir(LOGS_PATH)

    # 创建一个handler，用于写入日志文件
    filename = getlogname()
    fh = logging.FileHandler(filename)
    # fh.setLevel(logging.DEBUG)

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s : %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    # 清理日志文件夹
    try:
        cleanlog()
    except:
        import traceback
        logger.error(traceback.format_exc())

    return logger


'''------test part-------'''
if __name__ == '__main__':
    lger = getlogger()
    lger.info('xixixi')
