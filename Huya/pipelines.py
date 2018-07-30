# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from Huya.settings import IMAGES_STORE
import scrapy, os, json

class HuyaPipeline_images(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['image']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok == True][0]
        os.rename(IMAGES_STORE + image_path, IMAGES_STORE + 'full/' + item['nickname'] + '.jpg')
        return item

class HuyaPipeline(object):
    def open_spider(self, spider):
        self.f = open('C:/Users/HP/Desktop/huya.json', 'wb+')
        self.f.write('['.encode('utf-8'))

    def process_item(self, item, spider):
        data = {}
        data['昵称'] = item['nickname']
        data['房间名'] = item['roomName']
        data['房间号'] = item['roomNum']
        data['图片链接'] = item['image']
        data['观看人数'] = item['peopleNum']

        self.f.write(json.dumps(data, ensure_ascii=False).encode('utf-8') + ',\n'.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.f.write(']'.encode('utf-8'))
        self.f.close()