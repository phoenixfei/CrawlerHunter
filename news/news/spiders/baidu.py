# -*- coding: utf-8 -*-
import re
import scrapy
from pyquery import PyQuery as pq
from ..items import NewsItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    # allowed_domains = ['baidu.com']
    start_urls = [
        'http://news.baidu.com/ns?word=%E7%9F%A2%E9%87%8F%E5%8F%91%E5%8A%A8%E6%9C%BA&tn=news&from=news&cl=2&rn=20&ct=1']

    def parse(self, response):
        html = response.text
        doc = pq(html)
        next_page = doc('a.n').eq(-1).attr('href')
        # print('scrapy', next_page)
        if next_page:
            # print('http://news.baidu.com'+next_page)
            yield scrapy.Request('http://news.baidu.com' + next_page, callback=self.parse)

        result_divs = doc('div.result').items()
        for div in result_divs:
            # print(type(div))
            item = NewsItem()
            page_url = div('h3 a').attr('href')
            title = div('h3 a').text()
            time_source = div.find('p').filter('.c-author').text()
            # print(page_url, title, time_source)
            time = time_source.split(' ')[1].strip()
            source = time_source.split(' ')[0].strip()
            item['page_url'] = page_url
            item['title'] = title
            item['time'] = time
            item['source'] = source
            # item['content'] = self.__parse_content(html=html)
            if page_url:
                yield scrapy.Request(url=page_url, meta={'item': item}, callback=self.parse_new_url)

    def parse_new_url(self, response):
        item = response.meta.get('item')
        print('2text', item)
        print('2url', response.url)
        html = response.text
        content = self.__parse_content(html=html)
        item['content'] = content
        yield item

    def __parse_content(self, html):
        """ remove the the javascript and the stylesheet and the comment content
        (<script>....</script> and <style>....</style> <!-- xxx -->) """
        pattern = re.compile(r'<script.*?</script>|<style.*?</style>|<!--.*?-->|<meta.*?>|<ins.*?</ins>|<[^>]+>',
                             re.I | re.M | re.S)
        content = pattern.sub('', html)
        # use method get page_content
        result = self.__get_text(content)
        # remove other space, format text
        r = re.compile(r'''^\s+$''', re.M | re.S)
        result = r.sub('', result)
        r = re.compile(r'''\n+''', re.M | re.S)
        result = r.sub('\n', result)
        return result

    def __get_text(self, content):
        """
        method steps:
        1.remove HTML tags, but leave space, called c_text
        2.for c_text, spilt by '\n', and use k lines, called c_block
        3.remove c_block space, count #.word, called max_text_len
        4.if max_text_len > threshold, leave text
        :param content: the html removed html5'tags
        :return: web page text content
        """
        main_text = []
        block_width = 3  # the width of c_block
        c_text_len = []
        lines = content.split('\n')
        # print(lines)
        for i in range(len(lines)):
            if lines[i] == ' ' or lines[i] == '\n':
                lines[i] = ''
        for i in range(0, len(lines) - block_width):
            word_num = 0
            for j in range(i, i + block_width):
                word_num += len(lines[j])
            c_text_len.append(word_num)
        start = -1
        end = -1
        bool_start = False
        bool_end = False
        max_text_len = 88
        if len(c_text_len) < 3:
            return 'title'
        for i in range(len(c_text_len) - 3):
            if (c_text_len[i] > max_text_len and not bool_start):
                if (c_text_len[i + 1] != 0 or c_text_len[i + 2] != 0 or c_text_len[i + 3] != 0):
                    bool_start = True
                    start = i
                    continue
            if (bool_start):
                if (c_text_len[i] == 0 or c_text_len[i + 1] == 0):
                    end = i
                    bool_end = True
            temp = []
            if (bool_end):
                for ii in range(start, end + 1):
                    if (len(lines[ii]) < 5):
                        continue
                    temp.append(lines[ii] + "\n")
                text = "".join(list(temp))
                if 'Copyright' in text:
                    continue
                main_text.append(text)
                bool_end = bool_start = False
        result = ''.join(list(main_text))
        return result
