# coding: utf-8

'''链家网站的parser'''

from parserbase import ParserBase


'''链家二手房的parser'''
class LJesfParser(ParserBase):

    def __init__(self):
        super(LJesfParser, self).__init__()
        self.tag = 'LJesf'

    def can(self, parername):
        if parername == self.tag:
            return True
        else:
            return False

    def detailparse(self, doc):
        pass


'''链家成交记录的parser'''
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


'''链家小区详情的parser'''
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
