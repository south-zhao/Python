# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/13 20:03
# @Author : south(南风)
# @File : 大众点评.py
# Describe: 
# -*- coding: utf-8 -*-
import requests
from fontTools.ttLib import TTFont

url = "https://www.dianping.com/xian/ch10/g110r467"

payload={}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': 'navCtgScroll=0; showNav=#nav-tab|0|1; fspop=test; cy=17; cye=xian; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=183d139ccb6c8-075c6eff2f75d7-26021f51-e1000-183d139ccb6c8; _lxsdk=183d139ccb6c8-075c6eff2f75d7-26021f51-e1000-183d139ccb6c8; _hc.v=3b4336f9-4d7b-6558-eda1-38b5f2840b1f.1665662570; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1665662570; s_ViewType=10; lgtoken=05915b7dc-381d-4cdd-819e-301d20438c21; WEBDFPID=3w9vywyu0vwz56wx1ux7uw39zuwzw57u816w86z13w5979585v2uw93y-1981022617210-1665662616793WGGCIGAfd79fef3d01d5e9aadc18ccd4d0c95071572; _lxsdk_s=183d139ccb6-a02-97e-f40%7C%7C75; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1665662692; s_ViewType=10',
  'Referer': 'https://www.dianping.com/xian/ch10/g110',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.text

print(data)
















































