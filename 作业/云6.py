# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/11/30 7:59
# @Author : south(南风)
# @File : 云6.py
# Describe:
# -*- coding: utf-8 -*-
import jieba
from zhon.hanzi import punctuation
import PIL
import string
import jieba.posseg as pseg
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# 第一题
# with open("2.txt", 'r', encoding='utf-8') as f:
#     data = f.read()
# p = punctuation
# p1 = string.punctuation
# for i in p:
#     data = data.replace(i, "")
#
# for i in p1:
#     data = data.replace(i, "")
# data = data.replace("\n", "")
#
# data_list = jieba.lcut(data)
#
#
# word_counts = Counter()
# for x in data_list:
#     word_counts[x] += 1
# # # 获取前100最高频的词
# # word_counts_top100 = word_counts.most_common(100)
# # print(word_counts_top100)
# with open("one.txt", 'w', encoding='utf-8') as f:
#     for i, j in word_counts.items():
#         f.write(i + "   " + str(j) + "\n")
# # 绘制词云
# my_cloud = WordCloud(
#     background_color='white',  # 设置背景颜色  默认是black
#     width=900, height=600,
#     mask=np.array(PIL.Image.open('1.png')),
#     font_path='simhei.ttf',   # 设置字体  显示中文
#     max_font_size=99,         # 设置字体最大值
#     min_font_size=16,         # 设置子图最小值
#     random_state=50           # 设置随机生成状态，即多少种配色方案
# ).generate_from_frequencies(word_counts)
# my_cloud.to_file("one.png")
# # 显示生成的词云图片
# plt.imshow(my_cloud, interpolation='bilinear')
# # 显示设置词云图中无坐标轴
# plt.axis('off')
# plt.show()


# 第二题

with open("2.txt", 'r', encoding='utf-8') as f:
    data = f.read()
p = punctuation
p1 = string.punctuation
for i in p:
    data = data.replace(i, "")

for i in p1:
    data = data.replace(i, "")
data = data.replace("\n", "")

noun = []
verb = []
adj = []
words = pseg.lcut(data)
for i in words:
    if i.flag == "n":
        noun.append(i.word)
    elif i.flag == "v":
        verb.append(i.word)
    elif i.flag == "a":
        adj.append(i.word)

# 名词
noun = "".join(noun)
# 动词
verb = "".join(verb)
# 形容词
adj = "".join(adj)

noun_list = jieba.lcut(noun)
verb_list = jieba.lcut(verb)
adj_list = jieba.lcut(adj)

noun_counts = Counter()
for x in noun_list:
    noun_counts[x] += 1

noun_list = jieba.lcut(noun)


verb_counts = Counter()
for x in verb_list:
    verb_counts[x] += 1


adj_counts = Counter()
for x in adj_list:
    adj_counts[x] += 1


with open("名词.txt", 'w', encoding='utf-8') as f:
    for i, j in noun_counts.items():
        f.write(i + "   " + str(j) + "\n")

with open("动词.txt", 'w', encoding='utf-8') as f:
    for i, j in verb_counts.items():
        f.write(i + "   " + str(j) + "\n")


with open("形容词.txt", 'w', encoding='utf-8') as f:
    for i, j in adj_counts.items():
        f.write(i + "   " + str(j) + "\n")
# # 绘制词云
my_cloud = WordCloud(
    background_color='white',  # 设置背景颜色  默认是black
    width=900, height=600,
    mask=np.array(PIL.Image.open('1.png')),
    font_path='simhei.ttf',   # 设置字体  显示中文
    max_font_size=99,         # 设置字体最大值
    min_font_size=16,         # 设置子图最小值
    random_state=50           # 设置随机生成状态，即多少种配色方案
).generate_from_frequencies(noun_counts)
# # 显示生成的词云图片
my_cloud.to_file("名词.png")
plt.imshow(my_cloud, interpolation='bilinear')
# 显示设置词云图中无坐标轴
plt.axis('off')
plt.show()


my_cloud = WordCloud(
    background_color='white',  # 设置背景颜色  默认是black
    width=900, height=600,
    mask=np.array(PIL.Image.open('1.png')),
    font_path='simhei.ttf',   # 设置字体  显示中文
    max_font_size=99,         # 设置字体最大值
    min_font_size=16,         # 设置子图最小值
    random_state=50           # 设置随机生成状态，即多少种配色方案
).generate_from_frequencies(verb_counts)
# # 显示生成的词云图片
my_cloud.to_file("动词.png")
plt.imshow(my_cloud, interpolation='bilinear')
# 显示设置词云图中无坐标轴
plt.axis('off')
plt.show()


my_cloud = WordCloud(
    background_color='white',  # 设置背景颜色  默认是black
    width=900, height=600,
    mask=np.array(PIL.Image.open('1.png')),
    font_path='simhei.ttf',   # 设置字体  显示中文
    max_font_size=99,         # 设置字体最大值
    min_font_size=16,         # 设置子图最小值
    random_state=50           # 设置随机生成状态，即多少种配色方案
).generate_from_frequencies(adj_counts)
# # 显示生成的词云图片
my_cloud.to_file("形容词.png")
plt.imshow(my_cloud, interpolation='bilinear')
# 显示设置词云图中无坐标轴
plt.axis('off')
plt.show()
