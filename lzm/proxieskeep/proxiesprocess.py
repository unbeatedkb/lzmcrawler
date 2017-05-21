# coding: utf-8

from multiprocessing import Process
import time
from getallproxies import getproxies
import redis
from lzm.settings import Redis_Host, Redis_Port
from lzm.settings import Redis_Checked_Proxies, Redis_Root_Proxies
from check import checkproxy

'''
    维护代理池的主进程
    1.新增代理，每一个小时
    2.常驻进程检查代理的有效性
'''

'''获取代理，每一个小时从各大网站的代理处获取代理存入Redis'''


def fromproxies():
    rds = redis.Redis(Redis_Host, Redis_Port)
    while True:
        print 'what i want to do is get proxieskeep'
        getproxies()
        if rds.hlen(Redis_Root_Proxies) >= 100:
            # 未验证的代理数量超过100则休眠30分钟
            time.sleep(30 * 60)


class ProxiesProcess(object):

    def __init__(self):
        self.rds = redis.Redis(Redis_Host, Redis_Port)

    '''检查代理，从Redis取出代理，进行验证，将验证通过的代理存入Redis的可用代理的key中'''
    def checkproxies(self):
        print 'what i want to do is check proxieskeep'
        for k, v in self.rds.hgetall(Redis_Root_Proxies):
            item = {k: v}
            if checkproxy(item):
                self.rds.hset(Redis_Checked_Proxies, k, v)

    def processs(self):
        # 开启一个进程，每一个小时进行新增代理
        p1 = Process(target=fromproxies, args=())
        p1.start()
        # 设置常驻进程检查代理的有效性
        while True:
            # 检查代理的有效性
            self.checkproxies()
            # 当可用的代理数量充足时设置休眠
            if self.rds.hlen(Redis_Checked_Proxies) > 15:
                time.sleep(60)

if __name__ == '__main__':

    pp = ProxiesProcess()
    pp.processs()
