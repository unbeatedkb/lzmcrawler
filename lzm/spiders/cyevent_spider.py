# coding: utf-8

from scrapy_redis.spiders import RedisSpider
from lzm.items import CYeventItem
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


class CYeventSpider(RedisSpider):

    name = 'CYevent'
    redis_key = 'CYevent'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(CYeventSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        logger.info('--------------------------------------------------')
        logger.info('get response from web %s' % response.url)
        logger.info('--------------------------------------------------')
        item = CYeventItem()
        item['rootpage'] = response.body
        item['baseurl'] = response.url
        item['theid'] = md5(response.body)
        item['parsename'] = self.name
        item['collname'] = self.name
        item['parsed'] = 0
        return item