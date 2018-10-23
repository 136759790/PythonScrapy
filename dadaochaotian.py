# -*- coding: utf-8 -*-
import scrapy


class DadaochaotianSpider(scrapy.Spider):
    name = 'dadaochaotian'
    allowed_domains = ['208xs.com']
    start_urls = ['http://208xs.com/']

    def parse(self, response):
        pass
