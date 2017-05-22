# coding: utf-8

SPIDER_MODULES = ['lzm.spiders']
NEWSPIDER_MODULE = 'lzm.spiders'
DEFAULT_ITEM_CLASS = 'lzm.items.Website'

# Enables scheduling storing requests queue in redis.
# 使用scrapy_redis组件中的Scheduler
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
# 使用scrapy_redis组件中的去重器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Store scraped item in redis for post-processing.
# 定义项目管道
ITEM_PIPELINES = {
    # 'lzm.pipelines.FilterWordsPipeline': 1,
    'lzm.pipelines.MongoDBPipeline': 2,
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# 设置爬取间隔，单位为秒
# DOWNLOAD_DELAY = 0.25

# 存放常用的浏览器头
theuseragents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
]

# 覆盖默认的request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'zh-CN',
}

# 覆盖Scrapy默认的浏览器头
USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'

# 自定义的downloader中间件
DOWNLOADER_MIDDLEWARES = {
    'lzm.downloadermiddlewares.roatoragent.RoatorAgentMiddleware': 401,
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'lzm.downloadermiddlewares.proxies.ProxyMiddleWare': 700
}

# 可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG
LOG_LEVEL = 'INFO'

# 设置爬取深度
DEPTH_LIMIT = 2

# 设置初始的Rediskey的类型
REDIS_START_URLS_AS_SET = True

# Mongo连接配置
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "lzm"
MONGODB_COLLECTION = "blog"

# Redis连接配置
Redis_Host = 'localhost'
Redis_Port = '6379'

# Redis中存放待解析的文档集合名的key，set类型
Redis_Need_Parse = 'needparse'
# Mongo中存放未解析的网页的collname
Mongo_Root_Name = 'rootpages'

# Redis中存入验证过代理的key
Redis_Checked_Proxies = 'checkedproxies'
# Redis中存放爬取的代理的key
Redis_Root_Proxies = 'rootproxies'

# 定义Parser模块的parsers
PARSERS = {
    'lzm.parser.parserbase.ParserBase': 1,
    'lzm.parser.ljesfparser.LJesfParser': 2,
    'lzm.parser.ljtradeparser.LJtradeParser': 3,
    'lzm.parser.ljxiaoquparser.LJxiaoquParser': 4
}

# 日志文件夹路径
# LOGS_PATH = 'D:/work_code/lzmcrawler/lzm/logs/'
LOGS_PATH = 'D:/code/lzmcrawler/lzm/logs/'
# 日志文件夹最大文件数
MAX_LOGS = 60
