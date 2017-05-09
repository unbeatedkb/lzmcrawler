# coding: utf-8

from bs4 import BeautifulSoup
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.spiders import CrawlSpider


class NetEaseSpider(CrawlSpider):

    name = 'netease'
    start_urls = ['http://news.163.com/']

    # redis_key = 'netease:requests'

    rules = (
        Rule(LinkExtractor(allow='http://\w+.163.com/'), callback='parse_list', follow=True),
        Rule(LinkExtractor(allow='http://news.163.com/\w+/'), callback='parse_list', follow=True),
        Rule(LinkExtractor(allow='http://\w+.163.com/\d+/\d+/\d+/.+.html'), callback='parse_details', follow=False)
    )


    def parse_list(self, response):

        soup = BeautifulSoup(response.body, 'html.parser')
        for link in soup.find_all('a'):
            if link.get('href'):
                yield Request(link.get('href'))

    def parse_details(self, response):

        # 大分类
        thetype1 = response.xpath('//*[@id="ne_wrap"]/body/div[4]/div[1]/div[1]/a[2]/text()').extract()[0]
        print thetype1
        # 小分类
        thetype1 = response.xpath('//*[@id="ne_wrap"]/body/div[4]/div[1]/div[1]/a[3]/text()').extract()[0]
        print thetype1
        # 时间
        thetype1 = response.xpath('//*[@id="epContentLeft"]/div[1]/text()').extract()[0]
        print thetype1
        # 来源
        thetype1 = response.xpath('//*[@id="ne_article_source"]/text()').extract()[0]
        print thetype1
        # 摘要
        thetype1 = response.xpath('//*[@id="epContentLeft"]/div[2]/div[2]/text()').extract()[0]
        print thetype1
        # 文章内容
        thetype1 = response.xpath('//*[@id="endText"]/text()').extract()[0]
        print thetype1

    def parse_items(self, response):

        pass















