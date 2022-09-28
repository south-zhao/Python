# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/9/26 17:50
# @Author : south(南风)
# @File : 我有一剑.py
# Describe: 
# -*- coding: utf-8 -*-
import requests
from lxml import etree
import time

begin = time.time()
for x in range(198, 249):
    url = f"https://www.9biqu.com/biquge/25607/14890{x}.html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
                      "Safari/537.36 "
    }

    response = requests.get(url=url, headers=headers)

    # print(response)

    # print(response.text)

    content = response.text

    title = etree.HTML(content).xpath('/html/head/title')

    content1 = etree.HTML(content).xpath('//*[@id="content"]/p')
    i = title[0]
    if i.text is not None:
        for x in content1[0:]:
            if x.text is not None:
                # print(x.text.strip("&nbsp;"))
                with open("我有一剑\\" + i.text[:10], 'a', encoding="utf-8") as f:
                    f.write(x.text)
    with open("我有一剑\\" + i.text[:10], 'r', encoding="utf-8") as f1:
        res = []
        for y in f1.readlines():
            res.append(y.strip(" \n"))
    # print(res)
    count = 0
    with open("我有一剑\\" + i.text[:10], 'w', encoding="utf-8") as f2:
        for x in res:
            f2.write(x)
            count += 1
            if count % 5 == 0:
                f2.write("\n")

end = time.time()
print(end - begin)

print("over!")
