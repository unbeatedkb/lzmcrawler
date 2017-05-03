# coding: utf-8

import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

url = 'http://news.qq.com/world_index.shtml'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36'
}
content = requests.get(url, headers=headers).content
# print content

soup = BeautifulSoup(content, 'html.parser')
pt = re.compile('http://.+.qq.com/a/.+/.+.htm')
for i in soup.find_all('a'):
    href = i.get('href')
    if re.match(pt, href):
        print href