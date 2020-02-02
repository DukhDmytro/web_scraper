import scrapy
from scrapy_app import items
from scraper.models import WebSites


class DjinniSpider(scrapy.Spider):
    name = "djinni_spider"

    def __init__(self):
        self.to_scrap = 'https://djinni.co/'
        self.jobs_web_site = WebSites.objects.get(jobs_web_site=self.to_scrap)

    def start_requests(self):
        urls = ['https://djinni.co/jobs/?exp_level=2y&primary_keyword=Python&page=1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for href in response.css('.profile').xpath('@href').getall():
            url = f"{self.to_scrap}{href}"
            yield response.follow(url, self.parse_vacancy)

        next_page = response.css('ul.pager li a::attr(href)').getall()[-1]
        if next_page is not None:
            href = f"{self.to_scrap}{next_page}"
            yield response.follow(href, self.parse)

    def parse_vacancy(self, response):
        item = items.VacancyItem()
        item['title'] = response.css('h1::text').get()
        item['summary'] = response.css('p.profile::text').getall()
        item['description'] = response.css('div.profile-page-section::text').getall()
        item['company_web_site'] = response.css('div.profile-page-section a::attr(href)').getall()
        item['url'] = response.request.url
        item['experience'] = response.css('nobr::text').get()
        item['info'] = response.css('p.text-muted::text').getall()
        item['jobs_web_site'] = self.jobs_web_site
        yield item
