# -*- coding: utf-8 -*-
from time import gmtime, strftime

import scrapy
from lxml.etree import XPathError

from ..items import ViatorScrapItem


class ViatorSpiderSpider(scrapy.Spider):
    name = 'viator_spider'
    allowed_domains = ['viator.com']
    start_urls = ['https://www.viator.com/sitemap/']

    def parse(self, response):
        for link in response.xpath('//div[@class="row listing highlight-visited html-sitemap"]/div/ul/li/a'):
            url = "https://www.viator.com"+link.xpath('@href').extract()[0]
            continent = link.xpath('text()').extract()
            yield scrapy.Request(url, callback=self.parse_country, meta={"continent": continent})

    def parse_country(self, response):
        for link in response.xpath('//div[@class="container-fluid"]/div/div/ul/li'):
            if 'ttd' in link.xpath('a/@href').extract()[0]:
                country_name = link.xpath('a/text()').extract()[0]
                while True:
                    try:
                        link = link.xpath('ul/li')
                    except XPathError:
                        url = "https://www.viator.com" + link.xpath('a/@href').extract()[0]
                        city_name = link.xpath('a/text()').extract()[0]
                        break
                # url = "https://www.viator.com"+link.xpath('a/@href').extract()[0]
                # country_name = link.xpath('text()').extract()[0]
                continent = response.meta['continent']
                yield scrapy.Request(url, callback=self.parse_place, meta={'country': country_name, 'continent': continent, 'city': city_name})

    def parse_place(self, response):
        item = ViatorScrapItem()
        item["scrap_date"] = strftime("%Y-%m-%d", gmtime())
        item["scrap_time"] = strftime("%H:%M", gmtime())
        item['continent'] = response.meta['continent']
        item["country"] = response.meta['country']
        item["city"] = response.meta['city']
        item["count"] = response.xpath('//div[@id="productsList"]/@data-product-count').extract()
        item['page_des'] = response.xpath('//div[@id="productsList"]/@data-filter-counts').extract()
        yield item
