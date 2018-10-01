# _*_ coding: utf-8 _*_
__author__ = "Carl Benjamin"
__date__ = "2018/10/1 17:52"

from scrapy.cmdline import execute

import sys, os


sys.path.append(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(__file__))
# print(os.path.dirname(__file__))
# print(os.path.abspath(__file__))

execute(['scrapy', 'crawl', 'jobbole'])