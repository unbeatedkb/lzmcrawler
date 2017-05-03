# coding: utf-8

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Store scraped item in redis for post-processing.
ITEM_PIPELINES = {
    'lzm.pipelines.FilterWordsPipeline': 1,
    'lzm.pipelines.MongoDBPipeline': 2,
    'scrapy_redis.pipelines.RedisPipeline': 300
}

SPIDER_MODULES = ['lzm.spiders']
NEWSPIDER_MODULE = 'lzm.spiders'
DEFAULT_ITEM_CLASS = 'lzm.items.Website'


# 可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG
LOG_LEVEL = 'INFO'

# 设置爬取深度
DEPTH_LIMIT = 2

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "lzm"
MONGODB_COLLECTION = "blog"

Redis_Ip = 'localhost'
Redis_Port = '6379'