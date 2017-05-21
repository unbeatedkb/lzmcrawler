# coding: utf-8

'''
    Parser工具模块
'''

from lzm.settings import PARSERS
from scrapy.utils.conf import build_component_list
from scrapy.utils.misc import load_object


# 获取全部的parser
def getparsers():

    myparsers = []
    # 从配置文件获取parsers
    myprs = build_component_list(PARSERS, {})

    for clspath in myprs:
        try:
            mycl = load_object(clspath)
            parser = mycl()
            myparsers.append(parser)
        except:
            import traceback
            traceback.print_exc()

    return myparsers
