# coding: utf-8

'''
    链家二手房Spider类
'''

from scrapy_redis.spiders import RedisSpider
from lzm.items import LJxiaoquItem
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


class LJxiaoquSpider(RedisSpider):

    name = 'LJxiaoqu'
    redis_key = 'LJxiaoqu'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(LJxiaoquSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        logger.info('--------------------------------------------------')
        logger.info('get response from web %s' % response.url)
        logger.info('--------------------------------------------------')
        item = LJxiaoquItem()
        item['rootpage'] = response.body
        item['baseurl'] = response.url
        item['theid'] = md5(response.body)
        item['parsename'] = self.name
        item['collname'] = self.name
        item['parsed'] = 0
        return item
