# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AtmosParserSingleItem(scrapy.Item):
    full_name = scrapy.Field()
    biography = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()