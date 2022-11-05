# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/17 8:05
# @Author : south(南风)
# @File : 科技处.py
# Describe: 
# -*- coding: utf-8 -*-
import time
import json
import sys
from lxml import etree
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载完毕，寻找某些元素
from selenium.webdriver.support import expected_conditions as EC  ##等待指定标签加载完毕
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pymysql
import csv


class Tech:
    def __init__(self):
        self.browser = webdriver.Chrome()
        f = open('科技处.csv', 'a', encoding="utf-8-sig", newline="")
        self.csv_writer = csv.writer(f)

        # 3.构建列表头
        self.csv_writer.writerow(["板块", "网址", "标题", "网址", "时间", "点击量"])

    def get_kj(self, url):
        self.browser.get(url)
        # wait = WebDriverWait(self.browser, 100)
        # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'list')))
        time.sleep(2)
        data = self.browser.page_source
        return data

    def parse_data(self, data):
        xml = etree.HTML(data)
        type1 = xml.xpath('/html/body/div[3]/div/div/h3/a[2]//text()')
        url = xml.xpath('/html/body/div[3]/div/div/h3/a[2]/@href')
        title = xml.xpath('/html/body/div[3]/div/div/ul/li/a//text()')
        url_t = xml.xpath('/html/body/div[3]/div/div/ul/li/a/@href')
        for z, x in zip(type1, url):
            for m in range(10):
                i = title[0]
                title.remove(i)
                j = url_t[0]
                url_t.remove(j)
                data1 = self.get_kj('https://www.nsmc.edu.cn' + j)
                self.browser.back()
                xml1 = etree.HTML(data1)
                date = xml1.xpath('/html/body/div[3]/div/div[1]/span[1]//text()')[0]
                num = xml1.xpath('/html/body/div[3]/div/div[1]//span[2]//text()')[1]
                self.csv_writer.writerow([z, 'https://www.nsmc.edu.cn' + x, i, 'https://www.nsmc.edu.cn' + j, date, num])


    def run(self):
        data = self.get_kj('https://www.nsmc.edu.cn/kejichu')
        self.parse_data(data)


if __name__ == '__main__':
    a = Tech()
    a.run()
