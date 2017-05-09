# coding: utf-8

import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

url = 'http://hz.lianjia.com/chengjiao/'
proxies = {
  "http": "http://222.74.225.231:3128",
}


print requests.get(url, proxies=proxies).content