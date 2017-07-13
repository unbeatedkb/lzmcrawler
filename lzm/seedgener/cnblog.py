# coding: utf-8

from seeder import Seeder
from lzm.log import getlogger


logger = getlogger(__file__)


class CnBlogSpider(Seeder):

    def __init__(self):
        super(CnBlogSpider, self).__init__()
        self.baseurl = 'https://www.cnblogs.com/cate/python/'
        self.name = 'CnBlog'

    def seed(self, nums):
        logger.info('add %d seeds' % nums)
        # 分析页面
        for i in range(1, nums+1):
            url = self.baseurl + '%d' % i
            self.rds.sadd(self.name, url)


if __name__ == '__main__':

    seeder = CnBlogSpider()
    seeder.seed(100)
