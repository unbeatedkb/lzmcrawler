# coding: utf-8

from scrapy import Spider
from scrapy.selector import Selector
from dirbot.items import BlogItem

class BlogSpider(Spider):

    name = 'blog'
    allowed_domains = 'cnblogs.com'
    start_urls = ['https://www.cnblogs.com/cate/python/']



    def parse(self, response):

        links = Selector(response).xpath('///*[@id="post_list"]/div')
        print links
        for link in links:
            item = BlogItem()
            item['title'] = link.xpath('div[2]/h3/a/text()').extract()[0]
            item['url'] = link.xpath('div[2]/h3/a/@href').extract()[0]
            item['description'] = link.xpath('div[2]/p/text()').extract()[0].strip()
            print item['title']
            print item['url']
            print item['description']

            yield item

