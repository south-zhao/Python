# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/11/23 9:54
# @Author : south(南风)
# @File : 云5.py
# Describe:
# -*- coding: utf-8 -*-

# 第一题
# with open("1793-Washington.txt", 'r', encoding='utf-8') as f:
#     data = f.readlines()
#
# data = [i.strip('\n') for i in data if i.strip('\n') and i.strip('\n') != " "]
# data = data[0] + data[1]
# data = data.replace(',', '')
# data = data.replace('.', '')
# data = data.replace('(', '')
# data = data.replace(')', '')
# data = data.replace(':', '')
# word = data.split(" ")
# set1 = set(word)
# dict1 = {}
# for i in set1:
#     num = word.count(i)
#     dict1[i] = num
#
#
# with open("Washington_词频.txt", 'w', encoding='utf-8') as f:
#     for i, j in dict1.items():
#         f.write(i + "   " + str(j) + '\n')

# 第二题

# import csv
# import random
# with open('7_4儿童谜语集.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     question = []
#     answer = []
#     header = next(reader)
#     rows = [row for row in reader]
#     random.shuffle(rows)
#     with open(f'{header[0]}.txt', 'w', encoding='utf-8') as f1, open(f'{header[1]}.txt', 'w', encoding='utf-8') as f2:
#         for i, j in random.sample(rows, 10):
#             f1.write(i.strip('\xa0') + '\n')
#             f2.write(j + '\n')












