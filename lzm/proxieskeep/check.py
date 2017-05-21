# coding: utf-8

import requests

testurl = 'http://hz.lianjia.com/ershoufang/'
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 '
                  '(KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36'
}


# 结构{127.0.0.1:5800, asd:asd}
def checkproxy(proxy):
    if len(proxy) != 1:
        return False
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
            r = requests.get(testurl, headers=headers, proxies=proxy, timeout=30)
        except:
            return False
        if int(r.status_code) == 200:
            return True
        else:
            return False

