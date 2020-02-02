# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#
from scrapy_djangoitem import DjangoItem
from main.models import Vacancies


class ProductItem(DjangoItem):
    django_model = Vacancies
