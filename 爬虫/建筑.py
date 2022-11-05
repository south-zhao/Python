# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/18 14:30
# @Author : south(南风)
# @File : 建筑.py
# Describe: 
# -*- coding: utf-8 -*-
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import re

# url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_67.shtml"
url = "http://jianfangmi.com/qinggangbieshu/qinggangbieshuanli/"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(2)
data = browser.page_source
xml = etree.HTML(data)
name = xml.xpath('//*[@id="ct"]/div[1]/div[2]/div[2]/dl/dt/a//text()')
url1 = xml.xpath('//*[@id="ct"]/div[1]/div[2]/div[2]/dl/dt/a/@href')
# url1 = xml.xpath('/html/body/div[7]/div[2]/div[1]/div[2]/div/ul/li/a/@href')
# time1 = xml.xpath('/html/body/div[7]/div[2]/div[1]/div[2]/div/ul/li/span//text()')
# url1 = ['http://wsjkw.sc.gov.cn/' + i for i in url1]
# for i in url1:
#     browser.get(i)
#     time.sleep(2)
#     data1 = browser.page_source
#     link = re.findall('危重(.*?)人', data1, re.S)
#     link1 = re.findall('我省累计报告新型冠状病毒.*?例(.*?)例', data1, re.S)
#     print(link1, link)
#     print("====")
#
# print(url1, time1)

intro = xml.xpath('//*[@id="ct"]/div[1]/div[2]/div[2]/dl/dd[1]//text()')
time1 = xml.xpath('//*[@id="ct"]/div[1]/div[2]/div[2]/dl/dd[2]//text()')
for i in range(0, len(url1)):
    if not url1[i].startswith('http:'):
        url1[i] = 'http://jianfangmi.com/' + url1[i]

for i in range(0, len(name)):
    intro[i] = intro[i].replace('\n', ' ')

for i in range(0, len(name)):
    if intro[i] == " ":
        intro.pop(i)

for i in range(0, len(time1)):
    t = time1[i].replace('\n', '')
    if t is False:
        time1.pop(i)
# print(name, url1, intro, time1)

for i, j, z, x in zip(name, url1, intro, time1):
    print(i)
    print(j)
    print(z)
    print(x)
    print("==========")










