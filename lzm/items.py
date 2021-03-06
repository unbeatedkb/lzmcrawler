# coding: utf-8

from scrapy.item import Item, Field


# 链家成交记录
class LJtradeItem(Item):

    baseurl = Field()  # 初始链接
    rootpage = Field()  # 初始网页
    theid = Field()  # 标识id
    parsename = Field()  # 解析tag
    collname = Field()  # 解析后存放的集合名
    parsed = Field()  # 是否解析过的标识


# 链家小区
class LJxiaoquItem(Item):

    baseurl = Field()  # 初始链接
    rootpage = Field()  # 初始网页
    theid = Field()  # 标识id
    parsename = Field()  # 解析tag
    collname = Field()  # 解析后存放的集合名
    parsed = Field()  # 是否解析过的标识


class BlogItem(Item):

    title = Field()
    description = Field()
    content = Field()
    url = Field()


# 处理新闻的item类
class tencentnewItem(Item):

    title = Field()  # 标题
    thetime = Field()  # 发布时间
    source = Field()  # 来源
    content = Field()  # 新闻内容
    thetype = Field()  # 新闻分类
    comments = Field()  # 新闻评论


# 链家二手房
class LJesfItem(Item):

    baseurl = Field()  # 初始链接
    rootpage = Field()  # 初始网页
    theid = Field()  # 标识id
    parsename = Field()  # 解析tag
    collname = Field()  # 解析后存放的集合名
    parsed = Field()  # 是否解析过的标识


# 创业邦事件
class CYeventItem(Item):

    baseurl = Field()  # 初始链接
    rootpage = Field()  # 初始网页
    theid = Field()  # 标识id
    parsename = Field()  # 解析tag
    collname = Field()  # 解析后存放的集合名
    parsed = Field()  # 是否解析过的标识























