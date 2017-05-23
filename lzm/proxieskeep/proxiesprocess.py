# coding: utf-8

from multiprocessing import Process
import time
from getallproxies import getproxies
import redis
from lzm.settings import Redis_Host, Redis_Port
from lzm.settings import Redis_Checked_Proxies, Redis_Root_Proxies
from check import checkproxies
from lzm.log import getlogger

logger = getlogger(__file__)

'''
    维护代理池的主进程
    1.新增代理，每一个小时
    2.常驻进程检查代理的有效性
'''


# 获取代理
def fromproxies():
    rds = redis.Redis(Redis_Host, Redis_Port)
    while True:
        if rds.hlen(Redis_Root_Proxies) >= 100:
            # 未验证的代理数量超过100则休眠20分钟
            logger.info('enough proxies, sleep 20 mins')
            time.sleep(20*60)
            continue
        logger.info('get free proxies from web')
        getproxies()


class ProxiesProcess(object):

    def __init__(self):
        self.rds = redis.Redis(Redis_Host, Redis_Port)

    # 检查代理质量
    def checktheproxies(self):
        if not self.rds.hlen(Redis_Root_Proxies):
            time.sleep(20)
            return
        i = 0
        checklist = []
        for k, v in self.rds.hgetall(Redis_Root_Proxies).items():
            if len(checklist) == 8:
                checkproxies(checklist)
                i = 0
                checklist = []
            item = {k: v}
            checklist.append(item)
            self.rds.hdel(Redis_Root_Proxies, k)
            i += 1

    def processs(self):

        # 开启一个进程新增代理
        p1 = Process(target=fromproxies, args=())
        p1.start()

        while True:

            # 设置常驻进程检查代理的有效性
            # 当可用的代理数量充足时设置休眠
            if self.rds.hlen(Redis_Checked_Proxies) > 15:
                logger.info('enough checked proxies, wait.....')
                time.sleep(60)
                continue

            # 检查代理的有效性
            self.checktheproxies()

if __name__ == '__main__':

    pp = ProxiesProcess()
    pp.processs()
