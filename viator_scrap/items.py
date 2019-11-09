# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ViatorScrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    count = scrapy.Field()
    continent = scrapy.Field()
    scrap_time = scrapy.Field()
    scrap_date = scrapy.Field()
    city = scrapy.Field()
    pass
