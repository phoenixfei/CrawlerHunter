# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    page_url = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
