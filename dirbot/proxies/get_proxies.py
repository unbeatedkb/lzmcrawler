# coding: utf-8

import requests
import traceback
from bs4 import BeautifulSoup

url = 'http://www.xicidaili.com/'
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36'
}

class get_proxies(object):

    def __init__(self):
        self.proxies = []

    def get_proxies(self):
        try:
            content = requests.get(url, headers=headers, timeout=60).content
        except:
            traceback.print_exc()
            return self.proxies
        # print content
        soup = BeautifulSoup(content, 'html.parser')
        blocks = soup.find_all('tr', attrs={'class': 'odd'})
        for block in blocks:
            ip = block.text.split('\n')[2]
            port = block.text.split('\n')[3]
            # print ip
            # print port
            proxy = '%s:%s' % (ip, port)
            print proxy
            self.proxies.append(proxy)
if __name__ == '__main__':
    gp = get_proxies()
    gp.get_proxies()
