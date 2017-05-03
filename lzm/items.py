# coding: utf-8

from scrapy.item import Item, Field


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

