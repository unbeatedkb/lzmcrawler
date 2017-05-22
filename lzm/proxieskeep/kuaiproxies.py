# coding: utf-8

import requests
import traceback
from bs4 import BeautifulSoup
from lzm.log import getlogger

logger = getlogger(__file__)

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) '
                  'Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36'
}

baseurl = 'http://www.kuaidaili.com/proxylist/'


def kuaiproxies():
    proxies = {}
    for i in range(1, 11):
        url = baseurl+str(i)
        try:
            content = requests.get(url, headers=headers, timeout=30).content
        except:
            logger.error(traceback.format_exc())
            continue
        soup = BeautifulSoup(content, 'html.parser')
        try:
            for block in soup.find_all('tr'):
                # print block
                contents = block.text.split('\n')
                # print contentsy
                if contents[2].isdigit():
                    proxy = '%s:%s' % (contents[1], contents[2])
                    proxies.update({proxy: 1})
        except:
            logger.error(traceback.format_exc())
    return proxies


# kuaiproxies()
