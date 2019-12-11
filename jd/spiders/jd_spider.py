# -*- coding: utf-8 -*-
import scrapy
from  jd.items import JdItem
import sys
from scrapy.selector import Selector
import urllib
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor#crawlspider中专门用于提取相关连接的工具
import requests
from scrapy.http import Request
class JdSpiderSpider(scrapy.Spider):
    name = "jd_spider"
    allowed_domains = ["jd.com"]
    start_urls = ['http://list.jd.com/list.html?cat=9987,653,655&page=1']
    rules = [Rule(LinkExtractor(allow=r"page=\d+?"), callback='parse_item', follow=True)]

    def parse(self, response):
        selector = Selector(response)
        lis = selector.xpath('//ul[class="gl-warp clearfix"]/li')
        base_price_url = 'https://p.3.cn/prices/mgets?callback=jQuery%s&skuIds=J_%s'
        for li in lis:
            item = JdItem()

            item['name'] = li.xpath('div/div[class="p-img"]/a/@title').extract()[0]
            item['comment_num'] = li.xpath('div/div[class="p-commit"]/strong/a/text()').extract()[0]
            item['url'] = li.xpath('div/div[class="p-img"]/a/@href').extract()[0]
            item['info'] = li.xpath('div/div[class="p-name p-name-type-2"]/a/em/text()').extract()[0]

            print('解析异常。。。。。')

            price_url = base_price_url % (item['product_id'], item['product_id'])  # 这样就获得了每一款sku的价格的链接


            yield Request(url=price_url, callback=self.parse, meta={'item': item,'dont_redirect': True,
                 'handle_httpstatus_list': [302]})


        pass
