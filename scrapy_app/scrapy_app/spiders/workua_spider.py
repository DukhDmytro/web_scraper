import scrapy
from scrapy_app import items
from main.models import WebSites

class WorkSpider(scrapy.Spider):
    name = "workua_spider"

    def __init__(self):
        self.to_scrap = 'https://www.work.ua'
        self.jobs_web_site = WebSites.objects.get(jobs_web_site=self.to_scrap)

    def start_requests(self):
        urls = ['https://www.work.ua/jobs-kyiv-python/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for href in response.css("h2 a::attr(href)").getall():
            url = f"{self.to_scrap}{href}"
            yield response.follow(url, self.parse_vacancy)

        next_page = response.css("li.no-style a::attr(href)").getall()[-1]
        if next_page is not None:
            href = f"{self.to_scrap}{next_page}"
            yield response.follow(href, self.parse)

    def parse_vacancy(self, response):
        item = items.ProductItem()
        item['title'] = response.css('h1#h1-name::text').get()
        item['summary'] = []
        item['description'] = response.css('div#job-description *::text').getall()
        item['company_web_site'] = [f"{self.to_scrap}{response.css('p.text-indent.text-muted.add-top-sm a::attr(href)').get()}"]
        item['url'] = response.request.url
        item['experience'] = response.css('p.text-indent.add-top-sm::text').getall()[-1]
        item['info'] = response.css('p.cut-bottom-print span::text').getall()
        item['jobs_web_site'] = self.jobs_web_site
        yield item
