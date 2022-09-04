# import re

# import pandas as pd

# with open('题目.txt', 'r', encoding='utf-8') as f:
#   data = f.read()
# print(data)
# result_list = []
# username_list = re.findall('username="(.*?)"', source, re.S)
# content_list = re.findall('j_d_post_content " style="display:;">(.*?)<', source, re.S)
# reply_time_list = re.findall('class="tail-info">(2022.*?)<', source, re.S)
# import random
import re
from random import randint

wenti = []
chose = []
answer = []
wen = 1  # 要求题目前必须有题号，并且题号必须连续
with open("题目.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 去除两端空白符

        tihao = re.match(str(wen) + "[.、]?", line)  # 匹配题号
        chosehao = re.match("[ABCDabcd]", line)  # 匹配选项号
        answerhao = re.match("答案", line)  # 匹配答案号

        if tihao is not None:  # 匹配到题号
            wenti.append(line[tihao.end(0):])  # 去掉题号存储题目
            chose.append([])  # 置选项为空
            answer.append("")  # 置答案为空
            wen += 1

        elif chosehao is not None:  # 匹配到选项号
            chose[wen - 2].append(line)

        elif answerhao is not None:  # 匹配到答案号
            answer[wen - 2] = line

        else:  # 匹配失败
            raise Exception("程序出错了，匹配失败！")

# 抽题
chou = set()
while len(chou) < 5:
    chou.add(randint(0, len(wenti) - 1))

# 显示题目
count = 1
for i in chou:
    print(str(count) + ".", wenti[i])
    for j in chose[i]:
        print(j)
    print()
    count += 1

# 显示答案
count = 1
input("输入enter显示答案:")
for i in chou:
    print(str(count) + ".", end=' ')
    if answer[i] == "":
        print("无答案")
    else:
        print(answer[i])
    count += 1
