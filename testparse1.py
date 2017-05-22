# coding: utf-8

import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
import redis
from pymongo import MongoClient

def test1():
    mg = MongoClient('localhost', 27017)['lzm']
    mgcoll = mg['test']
    print mgcoll.count()

def test2():
    from random import choice
    l = {1: 2, 3: 4}
    print l[choice(l.keys())]

def test3():
    l = {1: 2, 0: 6}
    l1 = {3: 5, 4: 2}
    l2 = dict(l, **l1)
    print l2
    print len(l2)

def test4():
    import os
    print os.listdir('lzm/spiders/')
    for f in os.listdir('lzm/spiders/'):
        print type(os.path.getctime('lzm/spiders/'+f))

def test5():
    l = (2, 3, 4, 5)
    print l.pop()
    print l


test5()



