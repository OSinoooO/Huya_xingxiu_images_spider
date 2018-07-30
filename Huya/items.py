# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuyaItem(scrapy.Item):
    #昵称
    nickname = scrapy.Field()
    #主播图片
    image = scrapy.Field()
    #观看人数
    peopleNum = scrapy.Field()
    #标题
    roomName = scrapy.Field()
    #房间连接
    roomNum = scrapy.Field()
