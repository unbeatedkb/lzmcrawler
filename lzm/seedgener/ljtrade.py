# coding: utf-8

from seeder import Seeder
from lzm.log import getlogger

logger = getlogger(__file__)


class LJtradeSeeder(Seeder):

    def __init__(self):
        super(LJtradeSeeder, self).__init__()
        self.url = 'http://hz.lianjia.com/chengjiao/'
        self.name = 'LJtrade'

    def seed(self, nums):
        logger.info('add %d seeds' % nums)
        # 分析页面
        for i in range(1, nums+1):
            url = self.url + 'pg%d/' % i
            self.rds.sadd(self.name, url)


if __name__ == '__main__':

    seeder = LJtradeSeeder()
    seeder.seed(100)