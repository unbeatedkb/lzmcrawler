# coding: utf-8

'''
    开启常驻进程，将配置文件中注册的Parser模块全部加载
    读取Redis，根据Redis中的key值调用相应的模块进行解析
    可另外设置优先级
'''

from parseutils import getparsers
import redis
from pymongo import MongoClient
from lzm.settings import Redis_Host, Redis_Port
from lzm.settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DB
from lzm.settings import Redis_Need_Parse, Mongo_Root_Name
import traceback


class ParseProcess(object):

    def __init__(self):
        self.parsers = []
        self.rds = redis.Redis(Redis_Host, Redis_Port)
        self.mg = MongoClient(MONGODB_HOST, MONGODB_PORT)[MONGODB_DB]

    def reconnect(self):
        try:
            self.rds = redis.Redis(Redis_Host, Redis_Port)
            self.mg = MongoClient(MONGODB_HOST, MONGODB_PORT)[MONGODB_DB]
        except:
            traceback.print_exc()

    def parseall(self):
        '''
            解析模块的主逻辑
        '''
        # 加载配置文件中注册的Parser模块
        self.parsers = getparsers()

        # 一直解析，直到待解析的集合为空
        while self.rds.scard(Redis_Need_Parse):
            # 读取redis，随机弹出一个待解析的id
            theid = self.rds.spop(Redis_Need_Parse)
            # 获取mongo集合
            mgcoll = self.mg[Mongo_Root_Name]
            if mgcoll.count() == 0:
                self.rds.srem(Redis_Need_Parse, theid)
            for doc in mgcoll.find({'theid': theid}):
                if not doc:
                    print 'no doc find, what\'s wrong with you.'
                    continue
                parsername = doc.get('parsername')
                for parser in self.parsers:
                    # 查看文档是否解析过
                    if int(doc.get('parsed')) == 1:
                        continue
                    if parser.can(parsername):
                        # 解析文档
                        parser.parse(doc)


if __name__ == '__main__':
    mypp = ParseProcess()
    # 开启一个常驻进程
    while True:
        mypp.parseall()