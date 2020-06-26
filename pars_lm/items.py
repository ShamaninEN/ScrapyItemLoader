# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.loader.processors import MapCompose, TakeFirst, Identity
import scrapy
import re

def change_value(value):
    if value:
        value = re.sub(r"\n", '', value)
        value_start = re.sub(r"^\s+", '', value)
        value_end = re.sub(r"(\s\s+)", '', value_start)
    return value_end
def change_to_float(value):
    if value:
        value = float(re.sub(r"\s", '', value))
    return value

class ParsLmItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(output_processor=Identity())
    price = scrapy.Field(input_processor=MapCompose(change_to_float), output_processor=TakeFirst())
    articul = scrapy.Field(output_processor=TakeFirst())
    properties_name = scrapy.Field(input_processor=MapCompose(change_value))
    properties_value = scrapy.Field(input_processor=MapCompose(change_value))
    item_link = scrapy.Field(output_processor=TakeFirst())
