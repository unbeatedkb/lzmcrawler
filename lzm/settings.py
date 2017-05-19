# coding: utf-8

# Enables scheduling storing requests queue in redis.
# 使用scrapy_redis组件中的Scheduler
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
# 使用scrapy_redis组件中的去重器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Store scraped item in redis for post-processing.
# 定义项目管道
ITEM_PIPELINES = {
    'lzm.pipelines.FilterWordsPipeline': 1,
    'lzm.pipelines.MongoDBPipeline': 2,
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# 存放常用的浏览器头
theuseragents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
]

SPIDER_MODULES = ['lzm.spiders']
NEWSPIDER_MODULE = 'lzm.spiders'
DEFAULT_ITEM_CLASS = 'lzm.items.Website'

# 自定义的downloader中间件
DOWNLOADER_MIDDLEWARES = {
    'lzm.middlewares.roatoragent.RoatorAgentMiddleware': 1
}

# 可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG
LOG_LEVEL = 'INFO'

# 设置爬取深度
DEPTH_LIMIT = 2

# Mongo连接配置
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "lzm"
MONGODB_COLLECTION = "blog"

# Redis连接配置
Redis_Ip = 'localhost'
Redis_Port = '6379'

