# coding: utf-8

"""
    链家二手房的seeder
"""

from seeder import Seeder


class LJesfSeeder(Seeder):

    def __init__(self):
        super(LJesfSeeder, self).__init__()
        self.url = 'http://hz.lianjia.com/ershoufang/'
        self.name = 'LJesf'

    def seed(self):
        # 分析页面
        for i in range(1, 201):
            url = self.url + 'pg%d/' % i
            self.rds.sadd(self.name, url)


if __name__ == '__main__':

    seeder = LJesfSeeder()
    seeder.seed()
