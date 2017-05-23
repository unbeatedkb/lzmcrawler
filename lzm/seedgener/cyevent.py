# coding: utf-8

from seeder import Seeder
from lzm.log import getlogger


logger = getlogger(__file__)


class CYeventSpider(Seeder):

    def __init__(self):
        super(CYeventSpider, self).__init__()
        self.baseurl = 'http://www.cyzone.cn/event/'
        self.name = 'CYevent'

    def seed(self, nums):
        logger.info('add %d seeds' % nums)
        # 分析页面
        for i in range(1, nums+1):
            url = self.baseurl + 'list-764-0-%d-0-0-0-0/' % i
            self.rds.sadd(self.name, url)


if __name__ == '__main__':

    seeder = CYeventSpider()
    seeder.seed(100)
