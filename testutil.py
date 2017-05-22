# coding: utf-8

from pymongo import MongoClient
import redis

mg = MongoClient('localhost', 27017)['lzm']
rds = redis.Redis()

mgcoll = mg['rootpages']

for doc in mgcoll.find():
    theid = doc.get('theid')
    rds.sadd('needparse', theid)



