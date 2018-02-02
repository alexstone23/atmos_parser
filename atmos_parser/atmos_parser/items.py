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


class AtmosParserSingleItemExtended(scrapy.Item):
    titles = scrapy.Field()
    image_link = scrapy.Field()
    full_name = scrapy.Field()
    biography = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()
    education = scrapy.Field()
