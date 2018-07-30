# -*- coding: utf-8 -*-
import scrapy, json, time
from Huya.items import HuyaItem


class HuyaSpider(scrapy.Spider):
    name = 'huya'
    allowed_domains = ['www.huya.com']
    baseURL = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1663&tagAll=0&page='
    offset = 1
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']['datas']

        if not len(data_list):
            return

        for data in data_list:
            item = HuyaItem()
            item['nickname'] = data['nick']
            item['image'] = data['screenshot']
            item['peopleNum'] = data['totalCount']
            item['roomName'] = data['roomName']
            item['roomNum'] = data['profileRoom']
            yield item

        time.sleep(1)
        self.offset += 1
        yield scrapy.Request(self.baseURL + str(self.offset))
