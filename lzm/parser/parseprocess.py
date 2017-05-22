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
import time
from lzm.log import getlogger

logger = getlogger(__file__)


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
            logger.error(traceback.format_exc())

    def parseall(self):
        '''
            解析模块的主逻辑
        '''

        # 加载配置文件中注册的Parser模块
        self.parsers = getparsers()

        while True:
            if not self.rds.scard(Redis_Need_Parse):
                logger.info('no pages need parsed, wait........')
                time.sleep(60)
                continue

            # 读取redis，随机弹出一个待解析的id
            theid = self.rds.spop(Redis_Need_Parse)
            logger.info('get id:%s from redis' % theid)

            # 获取mongo集合
            mgcoll = self.mg[Mongo_Root_Name]
            for doc in mgcoll.find({'theid': theid}):
                if not doc:
                    logger.warn('no doc found, theid is : %s' % theid)
                    continue
                parsename = doc.get('parsename', '')

                if not parsename:
                    logger.warn('no parsename found, theid is : %s' % theid)
                    continue

                if int(doc.get('parsed')) == 1:
                    # 查看文档是否解析过
                    logger.info('doc is already parsed, will continue')
                    continue

                for parser in self.parsers:
                    try:
                        if parser.can(parsename):
                            # 解析文档
                            logger.info('using parser %s' % parser.__class__.__name__)
                            parser.parse(doc)
                            break
                    except:
                        logger.exception('parser %s' % parser.__class__.__name__)


if __name__ == '__main__':
    mypp = ParseProcess()
    logger.info('start parsing..................')
    mypp.parseall()
