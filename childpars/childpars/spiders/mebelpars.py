import scrapy


class MedelparsSpider(scrapy.Spider):
    name = "medelpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru"]

    def parse(self, response):
        pass
