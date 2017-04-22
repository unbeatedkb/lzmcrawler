# coding: utf-8
# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'

ITEM_PIPELINES = {'dirbot.pipelines.FilterWordsPipeline': 1,
                  'dirbot.pipelines.MongoDBPipeline': 2}

# 可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG
LOG_LEVEL = 'INFO'


MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "spy"
MONGODB_COLLECTION = "test"