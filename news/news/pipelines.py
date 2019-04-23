# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# If you just want text content, use command to get it.


class NewsPipeline(object):
    # def __init__(self):
    #     self.file = open('news/news_content.txt', mode='w', encoding='gbk')

    def process_item(self, item, spider):
        # self.file.write(item['content'] + '\n' + '*' * 100 + '\n')
        return item

    # def close_spider(self, spider):
    #     self.file.close()
