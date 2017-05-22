# coding: utf-8

import requests
import threading
import redis
from lzm.log import getlogger
from lzm.settings import Redis_Host, Redis_Port
from lzm.settings import Redis_Checked_Proxies


logger = getlogger(__file__)

testurl = 'http://hz.lianjia.com/'
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 '
                  '(KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36'
}



# 启动多线程测试代理质量
def checkproxies(proxies):
    for i in range(8):
        proxy = proxies.pop()
        t = threading.Thread(target=checkproxy, args=(proxy, ))
        t.setDaemon(True)
        t.start()


# 结构{'127.0.0.1:5800': 'asd:asd'}
def checkproxy(proxy):
    if len(proxy) != 1:
        logger.warn('error format proxy')
        return
    for k, v in proxy.items():
        if v and v != 1:
            # 代理需要认证的情况
            proxy = {
                'http': 'http://%s@%s' % (v, k)
            }
        else:
            # 不需要认证的情况
            proxy = {
                'http': 'http://%s' % k
            }
        # 请求测试网页
        try:
            r = requests.get(testurl, headers=headers, proxies=proxy, timeout=10)
        except:
            logger.warn('proxy timeout %s, %s' % (k, v))
            return
        if int(r.status_code) == 200:
            logger.info('checked proxy %s, %s' % (k, v))
            rds = redis.Redis(Redis_Host, Redis_Port)
            rds.hset(Redis_Checked_Proxies, k, v)
        else:
            logger.warn('bad proxy %s, %s' % (k, v))
            return


# checkproxy({'119.7.85.135:808': '1'})

