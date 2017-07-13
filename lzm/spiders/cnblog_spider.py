# coding: utf-8

from scrapy import Spider
from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from lzm.items import BlogItem
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider
import hashlib


def md5(s):
    try:
        s = str(s)
        m = hashlib.md5()
        m.update(s)
        return m.hexdigest()
    except:
        return ''


class CnBlogSpider(RedisSpider):

    name = 'CnBlog'
    redis_key = 'CnBlog'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(CnBlogSpider, self).__init__(*args, **kwargs)

    '''
        parse接收response，分两种情况。
        如果返回的response是需要的结果，返回且解析
        如果返回的response是中间状态，继续发起request
        特殊情况，如果返回的结果既是中间结果又是需要的结果又是中间状态，返回解析且在此发起request
    '''
    def parse(self, response):

        links = Selector(response).xpath('///*[@id="post_list"]/div')
        for link in links:
            item = BlogItem()
            item['title'] = link.xpath('div[2]/h3/a/text()').extract()[0]
            blog_url = link.xpath('div[2]/h3/a/@href').extract()[0]
            item['url'] = blog_url
            item['description'] = link.xpath('div[2]/p/text()').extract()[0].strip()
            print item['title']
            print item['url']
            print item['description']

            return item

