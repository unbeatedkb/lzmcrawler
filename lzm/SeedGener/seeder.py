# coding: utf-8

"""
    Seeder基类
"""

import redis
from seed_settings import Redis_host, Redis_port


class Seeder(object):

    def __init__(self):
        self.rds = redis.Redis(Redis_host, Redis_port)

    def seed(self):
        pass
