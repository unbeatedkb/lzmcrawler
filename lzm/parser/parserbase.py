# coding: utf-8

import redis
from lzm.settings import Redis_Host, Redis_Port
from lzm.settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DB
from pymongo import MongoClient
import traceback
from lzm.settings import Mongo_Root_Name

'''
    parser模块的基类
    功能: 
    读取配置文件
    从文件夹中加载所有的模块
    读取Redis中的数据
    根据配置文件的优先级进行解析
'''


class ParserBase(object):

    def __init__(self):
        try:
            self.rds = redis.Redis(Redis_Host, Redis_Port)
            self.mg = MongoClient(MONGODB_HOST, MONGODB_PORT)[MONGODB_DB]
        except:
            pass

    def reconnect(self):
        try:
            self.rds = redis.Redis(Redis_Host, Redis_Port)
            self.mg = MongoClient(MONGODB_HOST, MONGODB_PORT)[MONGODB_DB]
        except:
            traceback.print_exc()

    def can(self, parername):
        return False

    def parse(self, doc):
        # 解析网页，存入待存放的集合
        self.detailparse(doc)
        # 修改解析标识
        theid = doc.get('theid')
        self.mgcoll = self.mg[Mongo_Root_Name]
        self.mgcoll.update({'theid': theid}, {'$set': {'parsed': '1'}})

    # 具体的解析函数
    def detailparse(self, doc):
        pass

'''--------test part------------'''

if __name__ == '__main__':

    pb = ParserBase()
    pb.rds.hset('11', '22', '33')
    mgcoll = pb.mg['LJxiaoqu']
    for doc in mgcoll.find():
        print doc








