# coding: utf-8

from lzm.settings import Redis_Root_Proxies
from lzm.settings import Redis_Host, Redis_Port
import redis
from xiciproxies import xiciproxies
from ip181proxies import ip181proxies
from the66ipproxies import the66ipproxies
from kuaiproxies import kuaiproxies
from lzm.log import getlogger

logger = getlogger(__file__)


def getproxies():
    # 结构{127.0.0.1:5800, asd:asd}/{127.0.0.1:5800, 1}
    proxies = {}
    proxies1 = the66ipproxies()
    logger.info('get %d proxies from the66ip' % len(proxies1.keys()))
    proxies2 = ip181proxies()
    logger.info('get %d proxies from ip181proxies' % len(proxies2.keys()))
    proxies3 = xiciproxies()
    logger.info('get %d proxies from xici' % len(proxies3.keys()))
    proxies4 = kuaiproxies()
    logger.info('get %d proxies from kuai' % len(proxies4.keys()))
    for i in (proxies1, proxies2, proxies3, proxies4):
        proxies.update(i)
    rds = redis.Redis(Redis_Host, Redis_Port)
    # 将代理存入redis
    for k, v in proxies.items():
        rds.hset(Redis_Root_Proxies, k, v)




