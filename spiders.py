import os
import django
from scrapy_app.scrapy_app.spiders import djinni_spider, workua_spider
from scrapy.crawler import CrawlerRunner
from crochet import setup


os.environ['DJANGO_SETTINGS_MODULE'] = 'web_scraper.DDsettings'
django.setup()


def start_spiders():
    """
    Run spiders
    """
    setup()
    runner = CrawlerRunner()
    runner.crawl(djinni_spider.DjinniSpider)
    runner.crawl(workua_spider.WorkSpider)
