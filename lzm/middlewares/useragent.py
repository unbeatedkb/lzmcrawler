# coding: utf-8

'''
    用于轮换user-agent的模块
'''

from scrapy.downloadermiddlewares import useragent
from scrapy.http import Request
import traceback
from lzm.middlewares.theuseragents import theuseragents
import random


class Agentroator(useragent):

    def __init__(self):
        if not theuseragents:
            super(Agentroator, self).__init__()
        else:
            lenth = len(theuseragents)
            self.user_agent = theuseragents[random.randint(0, lenth-1)]

    def process_request(self, request, spider):

        # 处理request，return None
        try:
            request.headers.setdefault(b'User-Agent', self.user_agent)
        except Exception as e:
            traceback.print_exc()
            pass

