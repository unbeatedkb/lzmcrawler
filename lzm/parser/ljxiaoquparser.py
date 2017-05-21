# coding: utf-8

'''链家小区详情的parser'''

from parserbase import ParserBase
from bs4 import BeautifulSoup


class LJxiaoquParser(ParserBase):

    def __init__(self):
        super(LJxiaoquParser, self).__init__()
        self.tag = 'LJxiaoqu'

    def can(self, parername):
        if parername == self.tag:
            return True
        else:
            return False

    def detailparse(self, doc):
        pass
