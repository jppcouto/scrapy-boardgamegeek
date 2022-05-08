import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader
from ..items import BoardgamegeekItem

class JogosSpider(scrapy.Spider):
    name = 'jogo'
    start_urls = ['https://boardgamegeek.com/browse/boardgame/page/1']

    def parse(self, response):

        items = BoardgamegeekItem()

        for jogo in response.css('#row_'):
            items['rank'] = jogo.css('.collection_rank a::attr(name)').get()
            items['nome'] = jogo.css('.primary ::text').get()
            items['ano'] = response.css('.dull::text').get()[1:-1]
            items['avaliacao'] = jogo.css('#row_ .collection_bggrating:nth-child(5) ::text').get().split()[0]
            #items['avaliacao'] = jogo.cssresponse.css('#row_ .collection_bggrating:nth-child(4)::text').get().split()[0]
            yield items

        prox_pag=response.xpath('//*[@id="maincontent"]/form/div/div[1]/a[5]').attrib['href']
        if prox_pag is not None:
            yield  response.follow(prox_pag,callback=self.parse)


if __name__ == "__main__" :
    process=CrawlerProcess()
    process.crawl(JogosSpider)
    process.start()