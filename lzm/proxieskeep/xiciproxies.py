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

baseurl = 'http://www.xicidaili.com/wt/'
baseurl2 = 'http://www.xicidaili.com/nt/'


def xiciproxies():
    proxies = {}
    url1 = [baseurl + str(i) for i in range(1, 11)]
    url2 = [baseurl2 + str(i) for i in range(1, 11)]
    urls = url1 + url2
    for url in urls:
        try:
            content = requests.get(url, headers=headers, timeout=30).content
        except:
            logger.error(traceback.format_exc())
            continue
        soup = BeautifulSoup(content, 'html.parser')
        blocks = soup.find_all('tr', attrs={'class': 'odd'})
        try:
            for block in blocks:
                ip = block.text.split('\n')[2]
                port = block.text.split('\n')[3]
                proxy = '%s:%s' % (ip, port)
                proxies.update({proxy: 1})
        except:
            logger.error(traceback.format_exc())

    return proxies


'''-----test part-----'''
if __name__ == '__main__':
    xiciproxies()

