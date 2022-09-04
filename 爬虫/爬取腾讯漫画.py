# -*- coding: utf-8 -*-
# @Time : 2022/8/27 20:06
# @Author : south(南风)
# @File : 爬取腾讯漫画.py
# Describe:
# -*- coding: utf-8 -*-
# 利用爬虫收集漫画
import json

import requests
import re
import base64

url = 'https://ac.qq.com/ComicView/index/id/629440/cid/4'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36 '
}

response = requests.get(url=url, headers=headers)
# print(response)

html_data = response.text
# print(html_data)

b64_str = re.findall("var DATA = '(.*?)',", html_data)[0]
# print(b64_str)
for i in range(len(b64_str)):
    try:
        json_str = base64.b64decode((b64_str[i:]).encode('utf-8')).decode('utf-8')
        # print(json_str)
        json_str = re.findall('"picture":(\[.*?\])', json_str)[0]
        # print(json_str)
        json_list = json.loads(json_str)
        for x in json_list:
            print(x["url"])

        break
    except:
        pass
# print(base64.b64decode(b64_str))











