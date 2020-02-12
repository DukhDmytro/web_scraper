import scrapy
from scrapy_app import items
from scraper.models import WebSites, Selectors


class DjinniSpider(scrapy.Spider):
    name = "djinni_spider"

    def __init__(self):
        self.to_scrap = ''
        self.jobs_web_site = None
        self.selectors = {}

    start_urls = [
        'https://djinni.co/jobs/?english_level=intermediate&exp_level=2y&primary_keyword=Python&location=%D0%9A%D0%B8%D0%B5%D0%B2',
    ]

    def set_init(self, to_scrap):
        self.to_scrap = to_scrap
        self.jobs_web_site = WebSites.objects.get(jobs_web_site=self.to_scrap)
        self.selectors = Selectors.objects.filter(jobs_web_site=self.jobs_web_site).values().first()

    def parse(self, response):
        if response.url.startswith('https://djinni.co/'):
            self.set_init('https://djinni.co/')
        if response.url.startswith('https://www.work.ua'):
            self.set_init('https://www.work.ua')
        for href in response.css(self.selectors['vacancy_link']).getall():
            url = f"{self.to_scrap}{href}"
            yield response.follow(url, self.parse_vacancy)

        next_page = response.css(self.selectors['next_page']).getall()[-1]
        if next_page is not None:
            href = f"{self.to_scrap}{next_page}"
            yield response.follow(href, self.parse)

    def parse_vacancy(self, response):
        item = items.VacancyItem()
        item['title'] = response.css(self.selectors['title']).get()
        item['description'] = response.css(self.selectors['description']).getall()
        item['company_web_site'] = response.css(self.selectors['company_web_site']).getall()
        item['url'] = response.request.url
        item['job_info'] = response.css(self.selectors['job_info']).getall() + [response.css(self.selectors['experience']).get()]
        item['jobs_web_site'] = self.jobs_web_site
        yield item
