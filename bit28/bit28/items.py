# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Bit28Item(scrapy.Item):
    # define the fields for your item here like:
    image = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    delivery = scrapy.Field()
    link = scrapy.Field()
    sku = scrapy.Field()
    shop = scrapy.Field()
    category = scrapy.Field()
