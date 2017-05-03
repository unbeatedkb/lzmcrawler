# coding: utf-8

from redis import Redis
from lzm.settings import Redis_Ip, Redis_Port
import sys

'''
    用于seed种子的类
    目的，根据需求将种子送入redis，供spider进行抓取
'''


class NetEaseSeeder(object):

    def __init__(self):
        self.rdsobj = Redis(Redis_Ip, Redis_Port)

    # 生成种子放入redis
    def processseed(self):
        url = 'http://news.163.com/domestic/'
        self.rdsobj.sadd('netease:requests', url)

if __name__ == '__main__':

    ts = NetEaseSeeder()
    ts.processseed()
















