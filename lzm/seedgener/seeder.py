# coding: utf-8

"""
    Seeder基类
"""

import redis
from lzm.settings import Redis_Host, Redis_Port


class Seeder(object):

    def __init__(self):
        self.rds = redis.Redis(Redis_Host, Redis_Port)

    def seed(self, nums):
        pass
