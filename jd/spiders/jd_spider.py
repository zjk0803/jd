# -*- coding: utf-8 -*-
import scrapy


class JdSpiderSpider(scrapy.Spider):
    name = "jd_spider"
    allowed_domains = ["www.jd.com"]
    start_urls = ['http://www.jd.com/']

    def parse(self, response):
        
        pass
