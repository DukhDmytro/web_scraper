import scrapy
from scrapy_app import items
from scraper.models import WebSites


class WorkSpider(scrapy.Spider):
    name = "rabotaua_spider"

    def __init__(self):
        self.to_scrap = 'https://rabota.ua/'
        self.jobs_web_site = WebSites.objects.get(jobs_web_site=self.to_scrap)

    def start_requests(self):
        urls = ['https://rabota.ua/zapros/python/%d0%ba%d0%b8%d0%b5%d0%b2?profLevelIDs=3']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for href in response.css("a.ga_listing").xpath('@href').getall():
            url = f"{self.to_scrap}{href}"
            yield response.follow(url, self.parse_vacancy)

        next_page = response.css("dd.nextbtn a::attr(href)").get()
        if next_page is not None:
            href = f"{self.to_scrap}{next_page}"
            yield response.follow(href, self.parse)

    def parse_vacancy(self, response):
        item = items.VacancyItem()
        item['title'] = response.css('h1::text').get()
        item['description'] = []
        item['url'] = response.request.url
        item['experience'] = []
        item['info'] = []
        item['jobs_web_site'] = self.jobs_web_site


        # item['description'] = response.css('div#job-description *::text').getall()
        # item['company_web_site'] = [
        #     f"{self.to_scrap}{response.css('p.text-indent.text-muted.add-top-sm a::attr(href)').get()}"]
        # item['url'] = response.request.url
        # item['experience'] = response.css('p.text-indent.add-top-sm::text').getall()[-1]
        # item['info'] = response.css('p.cut-bottom-print span::text').getall()
        # item['jobs_web_site'] = self.jobs_web_site
        yield item
