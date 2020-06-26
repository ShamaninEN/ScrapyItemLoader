from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from pars_lm import settings
from pars_lm.spiders.leroy import LeroySpider

search = input('Введите чего ищите: ')

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroySpider, thing=search)


    process.start()