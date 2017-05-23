# -*- coding: utf-8 -*-

import redis
from lzm.settings import Redis_Checked_Proxies
from lzm.settings import DEFAULT_PAGE_CHECKER_WORDS
from lzm.settings import Redis_Host, Redis_Port
from lzm.log import getlogger

logger = getlogger(__file__)


# charests = ('utf8', 'gbk', 'gb2312', 'big5', 'ascii',
#             'shift_jis', 'euc_jp', 'euc_kr', 'iso2022_kr',
#             'latin1', 'latin2', 'latin9', 'latin10', 'koi8_r',
#             'cyrillic', 'utf16', 'utf32'
#              )
#
# def encode(stri, encoding='utf8'):
#     if isinstance(stri, unicode):
#         return stri.encode(encoding)
#     else:
#         for i in charests:
#             try:
#                 return stri.decode(i).encode(encoding)
#                 break
#             except:
#                 pass
#         else:
#             return stri


class PageErrorCheckMiddleware(object):

    def __init__(self):
        self.default_page_check_keywords = DEFAULT_PAGE_CHECKER_WORDS
        self.rds = redis.Redis(Redis_Host, Redis_Port)

    def process_response(self, request, response, spider):
        # 监测是否被封
        self.check_ip_forbidden(request, response, spider)

        return response

    def disableproxy(self, request):
        try:
            proxy = request.meta['proxy']
            proxy = proxy.split('http://')[1]
        except:
            return
        logger.info('disable the bad proxy %s' % proxy)
        try:
            self.rds.hdel(Redis_Checked_Proxies, proxy)
        except:
            logger.error('disbale proxy failed')

    '''检查返回内容，是否被封'''
    def check_ip_forbidden(self, request, response, spider):

        # if response.status == 403:
        #    spider.on_ip_forbidden(request, True)
        #    return

        content = response.body

        if not content:
            self.disableproxy(request)
            return

        url = str(response.url)
        if url.find('captcha') != -1:
            self.disableproxy(request)

        error_key_word = [
             "稍后再试", "未经授权的访问"]
        error_key_word = error_key_word + self.default_page_check_keywords

        for key in error_key_word:
            if content.find(key) != -1:
                self.disableproxy(request)
                return

