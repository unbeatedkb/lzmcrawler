# coding: utf-8

from bs4 import BeautifulSoup
from scrapy import Spider
from dirbot.items import BlogItem
from scrapy.http import Request

class CsdnSpider(Spider):

    name = 'csdn'
    # allowed_domains = 'blog.csdn.net'
    start_urls = ['http://blog.csdn.net/']

    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36'
    }

    def start_requests(self):
        yield Request('http://blog.csdn.net/', headers=CsdnSpider.headers)

    def parse(self, response):
        item = BlogItem()
        soup = BeautifulSoup(response.body)
        for doc in soup.find_all(attrs={'class': 'blog_list clearfix'}):
            item['title'] = doc.h3.a.text
            detail_url = doc.h3.a.get('href')
            print detail_url
            item['url'] = doc.h3.a.get('href')
            item['description'] = doc.find('div', attrs={'class': 'blog_list_c'}).text
            yield Request(detail_url, headers=CsdnSpider.headers, meta={'item': item}, callback=self.parse_details)

    def parse_details(self, response):
        item = response.meta.get('item')
        details = response.body
        # csdn每个博客似乎都是定制的，无法通过制定元素抓取
        # soup = BeautifulSoup(content, 'html.parser')
        # details = soup.find('div', attrs={'class': 'article_title'}).text
        print details
        item['content'] = details
        yield item
