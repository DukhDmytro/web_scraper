# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy_djangoitem import DjangoItem
import json



class ProductPipeline(DjangoItem):
    def process_item(self, item, spider):
        if spider.name == 'djinni_spider':
            for i, el in enumerate(item['description']):
                if "Сайт компанії" in el:
                    item['description'] = item['description'][:i]
        item['description'] = json.dumps(item['description'])
        if item['company_web_site']:
            item['company_web_site'] = item['company_web_site'][-1]
        else:
            item['company_web_site'] = ''
        item['job_info'] = ''.join(item['job_info'])
        item.save()
        return item
