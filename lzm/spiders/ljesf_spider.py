# coding: utf-8

'''
    链家二手房Spider类
'''

from scrapy_redis.spiders import RedisSpider
from lzm.items import LJesfItem
import hashlib
from lzm.log import getlogger

logger = getlogger(__file__)


def md5(s):
    try:
        s = str(s)
        m = hashlib.md5()
        m.update(s)
        return m.hexdigest()
    except:
        return ''


class LJesfSpider(RedisSpider):

    name = 'LJesf'
    redis_key = 'LJesf'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(LJesfSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        logger.info('get response from web %s' % response.url)
        item = LJesfItem()
        item['rootpage'] = response.body
        item['theid'] = md5(response.body)
        item['parsename'] = self.name
        item['collname'] = self.name
        item['parsed'] = 0
        return item
