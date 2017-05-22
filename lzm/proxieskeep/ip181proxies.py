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

baseurl = 'http://www.ip181.com/daili/'


def ip181proxies():
    proxies = {}
    urls = [baseurl+'%d.html' % i for i in range(1, 11)]
    for url in urls:
        try:
            content = requests.get(url, headers=headers, timeout=30).content
        except:
            logger.error(traceback.format_exc())
            continue
        soup = BeautifulSoup(content, 'html.parser')
        try:
            for block in soup.find_all('tr'):
                contents = block.text.split('\n')
                try:
                    restime = contents[5].split(u'秒')[0].strip()
                    restime = float(restime)
                except:
                    continue
                if restime > 2.0:
                    continue
                proxy = '%s:%s' % (contents[1], contents[2])
                proxies.update({proxy: 1})
        except:
            logger.error(traceback.format_exc())
    return proxies


# ip181proxies()

























