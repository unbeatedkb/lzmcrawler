# coding: utf-8


from scrapy.spiders import Spider
from lzm.items import LJesfItem
from scrapy.http import Request

class LJesfspider(Spider):

    name = 'LJesf'

    start_urls = ['http://blog.csdn.net/']

    headers = {
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.96 Safari/537.36'
    }

    def start_requests(self):
        for i in range(120):
            yield Request('http://hz.lianjia.com/chengjiao/pg%s/' % i, headers=self.headers, meta=
            {'proxy': 'http://58.52.201.117:8080'})
            # yield Request('http://hz.lianjia.com/chengjiao/pg%s/' % i, headers=self.headers)

    def parse(self, response):
        '''
详情标题：/div/div[1]/a
房情介绍：/div/div[2]/div[1]/text()
建成日期：/div/div[3]/div[1]/text()
地段位置：/div/div[4]/span[2]/span/text()
挂牌价格：/div/div[5]/span[2]/span[1]/text()
成交周期：/div/div[5]/span[2]/span[2]/text()
成交时间：/div/div[2]/div[2]
成交来源：/div/div[3]/div[2]
成交价格：/div/div[2]/div[3]/span
成交单价：/div/div[3]/div[3]/span
        :param response: 
        :return: 
        '''
        blocks = response.xpath('/html/body/div[4]/div[1]/ul/li')
        for block in blocks:
            print block.xpath('/div[1]/div[1]/a/text()').extract()
            print block.xpath('/div/div[2]/div[1]/text()').extract()
            print block.xpath('/div/div[3]/div[1]/text()').extract()
            print block.xpath('/div/div[4]/span[2]/span/text()').extract()
            print block.xpath('/div/div[5]/span[2]/span[1]/text()').extract()
            print block.xpath('/div/div[5]/span[2]/span[2]/text()').extract()
            print block.xpath('/div/div[2]/div[2]/text()')[0].extract()
            print block.xpath('/div/div[3]/div[2]/text()')[0].extract()
            print block.xpath('/div/div[2]/div[3]/span/text()')[0].extract()
            print block.xpath('/div/div[3]/div[3]/span/text()')[0].extract()




















