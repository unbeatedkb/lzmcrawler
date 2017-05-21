# coding: utf-8

import requests
from lzm.settings import Redis_Root_Proxies
from lzm.settings import Redis_Host, Redis_Port
import redis


def getproxies():
    # 结构{127.0.0.1:5800, asd:asd}
    proxies = {}
    proxies1 = the66ipproxies()
    proxies2 = bigproxies()
    proxies3 = xiciproxies()
    proxies4 = kuaiproxies()
    proxies5 = the360proxies()
    for i in (proxies1, proxies2, proxies3, proxies4, proxies5):
        proxies.update(i)
    rds = redis.Redis(Redis_Host, Redis_Port)
    # 将代理存入redis
    for k, v in proxies.items():
        rds.hset(Redis_Root_Proxies, k, v)


def the66ipproxies():
    proxies = {}
    return proxies


def bigproxies():
    proxies = {}
    return proxies


def xiciproxies():
    proxies = {}
    return proxies


def kuaiproxies():
    proxies = {}
    return proxies


def the360proxies():
    proxies = {}
    return proxies


