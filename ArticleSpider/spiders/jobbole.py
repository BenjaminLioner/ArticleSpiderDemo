# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
import os

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']


    def parse(self, response):
        # title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()
        # print(title[0])
        # 成功在'http://blog.jobbole.com/114424/' 页面中获得标题, 存为title 变量, 类型 字符串



        # 获取下一页的url并且交给scrapy进行下载
        '''
        1.获取文章列表终端额具体文章url并且交给解析函数进行具体字段来解析的
        2.获取下一页的url交给scrapy进行下载,下载完成后交给parse


        :param response:
        :return:
        '''

        # post_urls =  response.xpath("//a[@class='archive-title']/text()").extract()
        # for post_url in post_urls:
        #     print(post_url)
        #     Request(url = post_url, callback=self.parse_details)
        title_list = response.xpath("//a[@class='archive-title']/text()").extract()

        for title in title_list:
            try:
                file = open('标题.txt', 'a')
                file.write(title+"\n")
                file.close()
            except:
                pass

        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

        pass


    def parse_details(self, response):
        pass


    def url_join(self, base, url):
        return parse.urljoin(base, url)