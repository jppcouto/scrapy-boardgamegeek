# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BoardgamegeekItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    nome = scrapy.Field()
    ano = scrapy.Field()
    avaliacao = scrapy.Field()
    pass
