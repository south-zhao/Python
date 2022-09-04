# -*- coding: utf-8 -*-
# @Time : 2022/8/25 19:57
# @Author : south(南风)
# @File : 爬取vip.py
# Describe:
# -*- coding: utf-8 -*-
# 爬虫爬取VIP付费内容
"""
1.发送数据请求   网址
2.获取数据
3.解析数据
"""
import requests
from lxml import etree


url = "https://www.duanmeiwen.com/xinshang/2211583.html"
# 伪装爬虫代码  模拟成为浏览器向服务器发送数据请求
headers = {
    # 键值对
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36 '
}

# 发送数据请求
response = requests.get(url=url, headers=headers)
# print(response)  <Response [200]> 响应对象  请求成功   200 状态码

# response.encoding = 'gb2312'  # 设置编码方式
# 自动识别编码方式
# response.encoding = response.apparent_encoding
# print(response.text)
# 转化为二进制
content = response.content
# 加载网页数据
doc = etree.HTML(content).xpath('//div[@class="content"]/p')  # // 定位任意标签  / 下一级标签 @ 属性  [] 条件
# print(doc)
for p in doc:
    # print(p.text)
    if p.text is not None:
        with open('1.txt', 'a', encoding='utf-8') as f:
            f.write(p.text + '\n')
print("over")





















