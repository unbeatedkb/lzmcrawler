# coding: utf-8

import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'http://blog.csdn.net/'
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36'
}
content = requests.get(url, headers=headers).content
# print content

soup = BeautifulSoup(content, 'html.parser')
for doc in soup.find_all(attrs={'class': 'blog_list clearfix'}):
    print doc.h3.a.get('href')
    print doc.h3.a.text
    print doc.find('div', attrs={'class': 'blog_list_c'}).text.strip()
