# coding: utf-8

'''
    自动更换代理的模块
    从维护的代理池中取出验证过的代理，如果代理池为空，则不用代理
'''

import redis
from lzm.settings import Redis_Host, Redis_Port
from lzm.settings import Redis_Checked_Proxies
from random import choice
import base64
from lzm.log import getlogger

logger = getlogger(__file__)


class ProxyMiddleWare(object):

    def __init__(self):
        self.rds = redis.Redis(Redis_Host, Redis_Port)

    # 处理Requests的方法
    def process_request(self, request, spider):

        proxies = self.rds.hgetall(Redis_Checked_Proxies)
        if not proxies:
            return

        # 代理字符串结构"YOUR_PROXY_IP:PORT"
        theproxy = choice(proxies.keys())

        # 认证的结构USERNAME:PASSWORD
        theauth = proxies[theproxy]

        request.meta['proxy'] = 'http://%s' % theproxy
        logger.info('using proxy : %s' % theproxy)
        # 代理需要认证的情况
        if theauth and theauth != 1:
            encoded_auth = base64.b64encode(theauth)
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_auth

