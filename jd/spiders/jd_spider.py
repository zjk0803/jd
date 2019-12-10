# -*- coding: utf-8 -*-
import scrapy
from  ..items import JdItem
import sys
from scrapy.selector import Selector
class JdSpiderSpider(scrapy.Spider):
    name = "jd_spider"
    allowed_domains = ["www.jd.com"]
    start_urls = ['http://www.jd.com/']

    def parse(self, response):
        selector = Selector(response)
        lis = selector.xpath('//ul[class="gl-warp clearfix"]/li')
        for li in lis:
            item = JdItem()
            try:
                item['name'] = li.xpath('div/div[class="p-name p-name-type-2"]/text()').ex
        pass
