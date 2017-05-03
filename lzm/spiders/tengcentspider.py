# coding: utf-8
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
import re
from scrapy.http import Request
from bs4 import BeautifulSoup


pt_list = re.compile('http://\w+.news.qq.com/')
pt_details = re.compile('http://\w+.qq.com/a/\d+/\d+.htm')

class TencentSpider(RedisCrawlSpider):

    name = 'tencentnews'
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10'
                      ' Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36'
    }
    start_urls = ['http://news.qq.com/']

    rules = (
        # class scrapy.spiders.Rule(link_extractor, callback=None, cb_kwargs=None, follow=None,
        # process_links=None, process_request=None)
        Rule(LinkExtractor(allow='http://\w+.news.qq.com/'), callback='parse_list', follow=True),
        Rule(LinkExtractor(allow='http://\w+.qq.com/a/\d+/\d+.htm'), callback='parse_details', follow=False)
    )

    def start_requests(self):
        yield Request('http://news.qq.com/', headers=self.headers, callback=self.parse_list)

    def parse_list(self, response):
        content = response.body
        soup = BeautifulSoup(content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if not href:
                continue
            if re.match(pt_list, href):
                yield Request(href, callback=self.parse_list, headers=self.headers)
            if re.match(pt_details, href):
                yield Request(href, callback=self.parse_details, headers=self.headers)

    def parse_details(self, response):
        # soup = BeautifulSoup(response.body, 'lxml')
        title = response.xpath('//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/h1/text()').extract()[0]
        print title
        try:
            thetype = response.xpath('//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[1]/a/text()').extract()[0]
        except:
            thetype = ''
        print thetype
        thetime = response.xpath('//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[3]/text()').extract()[0]
        print thetime
        source = response.xpath('//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[2]/a/text()').extract()[0]
        print source
        thecontent = ''
        content = response.xpath('//*[@id="Cnt-Main-Article-QQ"]/p/text()').extract()
        for ct in content:
            thecontent = thecontent + ct + '\n'
        print thecontent
        # commenturl = response.xpath('//*[@id="commentTotleNum"]/@href').extract()
        # commenturl = response.xpath('//a[@id="commentTotleNum"]').extract()[0]
        # print commenturl
        # 评论放在iframe中，暂时不去处理，节约时间
        # commenturl = soup.find('a', attrs={'id': 'commentTotleNum'}).get('href')
        # print commenturl


