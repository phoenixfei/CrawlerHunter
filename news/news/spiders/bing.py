# -*- coding: utf-8 -*-
import scrapy


class BingSpider(scrapy.Spider):
    name = 'bing'
    # allowed_domains = ['bing.com']
    start_urls = ['https://cn.bing.com/search?q=voctor%20engine+language:en&count=50']

    def parse(self, response):
        pass
