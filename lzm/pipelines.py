# coding: utf-8

from lzm.settings import Redis_Need_Parse
from lzm.settings import Redis_Host, Redis_Port
import redis
from scrapy.exceptions import DropItem
from pymongo import MongoClient
from lzm import settings
from scrapy import log
from lzm.log import getlogger

logger = getlogger(__file__)


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in item['description'].lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item


class MongoDBPipeline(object):

    def __init__(self):
        connection = MongoClient(
            settings.MONGODB_HOST,
            settings.MONGODB_PORT
        )
        db = connection[settings.MONGODB_DB]
        self.collection = db[settings.Mongo_Root_Name]
        self.rds = redis.Redis(Redis_Host, Redis_Port)

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                break
        if valid:
            theid = item['theid']
            self.collection.update({'theid': theid}, {'$set': dict(item)}, upsert=True)
            # log.msg("Question added to MongoDB database!",
            #         level=log.DEBUG, spider=spider)
            # 将待解析的id存入Redis
            logger.info('save one page, theid is %s' % theid)
            self.rds.sadd(Redis_Need_Parse, theid)
        return item
