# coding: utf-8


from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import traceback
import random
from lzm.settings import theuseragents


class RoatorAgentMiddleware(UserAgentMiddleware):

    '''
        用于轮换user-agent的中间件类
        scrapy默认的useragent处理类是直接读取配置文件的useragent
    '''

    def __init__(self, user_agent='Scrapy'):
        if not theuseragents:
            # 如果配置文件中未存放浏览器头，则使用scrapy默认的浏览器头
            super(RoatorAgentMiddleware, self).__init__()
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

