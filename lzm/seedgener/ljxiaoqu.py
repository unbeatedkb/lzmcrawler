# coding: utf-8

from seeder import Seeder
from lzm.log import getlogger

logger = getlogger(__file__)


class LJxiaoquSeeder(Seeder):

    def __init__(self):
        super(LJxiaoquSeeder, self).__init__()
        self.url = 'http://hz.lianjia.com/xiaoqu/'
        self.name = 'LJxiaoqu'

    def seed(self, nums):
        logger.info('add %d seeds' % nums)
        # 分析页面
        for i in range(1, nums+1):
            url = self.url + 'pg%d/' % i
            self.rds.sadd(self.name, url)


if __name__ == '__main__':

    seeder = LJxiaoquSeeder()
    seeder.seed(100)
