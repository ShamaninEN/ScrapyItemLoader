# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from pars_lm.items import ParsLmItem
from scrapy.loader import ItemLoader

class LeroySpider(scrapy.Spider):
    name = 'leroy'
    allowed_domains = ['leroymerlin.ru']
    def __init__(self, thing):
        self.start_urls = [f'https://leroymerlin.ru/search/?q={thing}']


    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//div[@class='list-paginator'] //a[contains(@class, 'next-paginator-button')]/@href").extract_first()
        item_links = response.xpath("//div[@class='product-name']/a[contains(@class, 'product-name-inner')]/@href").extract()
        for item_link in item_links:
            yield response.follow(f'https://leroymerlin.ru{item_link}', callback=self.parse_item )


        yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response:HtmlResponse):
        loader = ItemLoader(item=ParsLmItem(), response=response)
        loader.add_xpath('photos', "//source[contains(@media, '1024px')]/@data-origin")
        loader.add_xpath('name', "//h1[@class='header-2']/text()")
        loader.add_xpath('articul', "//span[@slot='article']/@content")
        loader.add_xpath('price', "//span[@slot='price']/text()")
        loader.add_xpath('properties_name', "//div[@class='def-list__group']/dt/text()")
        loader.add_xpath('properties_value', "//div[@class='def-list__group']/dd/text()")
        loader.add_value('item_link', response.url)
        yield loader.load_item()