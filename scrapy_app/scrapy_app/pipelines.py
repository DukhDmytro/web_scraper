# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy_djangoitem import DjangoItem


class ProductPipeline(DjangoItem):
    def process_item(self, item, spider):
        item['description'] = ''.join(item['description'])
        if item['summary'] is None:
            item['summary'] = ''
        else:
            item['summary'] = ''.join(item['summary'])
        if item['company_web_site']:
            item['company_web_site'] = item['company_web_site'][-1]
        else:
            item['company_web_site'] = ''
        item['info'] = ''.join(item['info'])
        item.save()
        return item
