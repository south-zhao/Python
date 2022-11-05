# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/17 21:23
# @Author : south(南风)
# @File : test1.py
# Describe: 云1
# -*- coding: utf-8 -*-
# 第一题
# student_id = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
# an1 = student_id[:3]
# an2 = student_id[7:]
# an3 = student_id[3:8]
# an4 = student_id[0::2]
# an5 = student_id[0::5]
# print(an1)
# print(an2)
# print(an3)
# print(an4)
# print(an5)
# 第二题
# import math
#
#
# def sv(num):
#     sum1 = 0
#     for i in num:
#         sum1 += i
#     leng = len(num)
#     avg = float(sum1 / leng)
#     return avg
#
#
# def mid(num):
#     num.sort()
#     if len(num) % 2 == 0:
#         middle1 = float((num[int(len(num) / 2) - 1] + num[int(len(num) / 2)]) / 2)
#     else:
#         middle1 = num[int((len(num) - 1) / 2)]
#     return middle1
#
#
# def stand(num):
#     avg1 = sv(num)
#     sum2 = 0
#     for i in num:
#         sum2 += math.pow(i - avg1, 2)
#     d = math.pow(sum2 / (len(num) - 1), 0.5)
#     return d
#
#
# if __name__ == '__main__':
#     a = list(map(int, input("请输入十个数据，用空格隔开:").split(" ")))
#     # print(type(a[0]))
#     avd = sv(a)
#     middle = mid(a)
#     d = stand(a)
#     print(avd)
#     print(middle)
#     print(d)


# 第三题
# word = input("请输入一段英文句子:").split(" ")
# max1 = word[0]
# for i in word[1:]:
#     if len(i) > len(max1):
#         max1 = i
#
# print(max1)



