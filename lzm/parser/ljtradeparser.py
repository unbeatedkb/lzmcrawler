# coding: utf-8

'''链家成交记录的parser'''

from parserbase import ParserBase
from bs4 import BeautifulSoup


class LJtradeParser(ParserBase):

    def __init__(self):
        super(LJtradeParser, self).__init__()
        self.tag = 'LJtrade'

    def can(self, parername):
        if parername == self.tag:
            return True
        else:
            return False

    def detailparse(self, doc):
        pass
