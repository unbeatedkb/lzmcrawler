from scrapy.item import Item, Field


class BlogItem(Item):

    title = Field()
    description = Field()
    content = Field()
    url = Field()
