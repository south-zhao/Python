# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/9/23 19:57
# @Author : south(南风)
# @File : 爬取小姐姐.py
# Describe: 爬取小姐姐照片并进行测评
# -*- coding: utf-8 -*-
from pprint import pprint

import requests
import os
import re
import json
import csv
c = open('data.csv', 'a', encoding="utf-8", newline="")
csv_writer = csv.DictWriter(c, fieldnames=[
    "昵称",
    "价格",
    "热度",
    "简介",
    "详情页",
])
csv_writer.writeheader()
from tqdm import tqdm
import base64
for page in range(1, 11):
    # url = "https://www.peiwantv.com/userlist/1/1"
    url = "https://www.peiwantv.com/api"

    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
    #                   "Safari/537.36 "
    # }
    data = {
        "act": "userList",
        "page": page,
        "type": "1",
        "sex": "2",
        "voice": "1",
        "order": "1"
    }

    response = requests.post(url=url, data=data)
    # print(response.text)
    # print(response)
    # 返回数据有{}形式，用json加载
    # print(response.json())
    # pprint()打印多行字典
    data1 = response.json()['data']['rows']
    for i in data1:
        # print(i)
        # pprint(i)
        dict1 = {
            "昵称": i['nickname'],
            "价格": i['price'],
            "热度": i['exp'],
            "简介": i['summary'].replace("\n", ''),
            "详情页": f"https://www.peiwantv.com/user/{i['uid']}"
        }
        # pprint(dict1)
        # break
        audio = "https://static.peiwan.tv/" + json.loads(i['voice'])["url"]

        img_url = f"https://www.peiwantv.com/user/avatar/{i['uid']}?image…ew2/1/interlace/1/ignore-error/1/w/100/format/jpg"

        img_con = requests.get(url=img_url).content
        audio_con = requests.get(url=audio).content
        title = i['nickname']
        file = f"data\\{title}\\"
        if not os.path.exists(file):
            os.makedirs(file)
        with open(file + title + '.jpg', 'wb') as img1:
            img1.write(img_con)
        with open("img\\" + title + '.jpg', 'wb') as img1:
            img1.write(img_con)
        with open(file + title + '.mp3', 'wb') as au:
            au.write(audio_con)

        csv_writer.writerow(dict1)
