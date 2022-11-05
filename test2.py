# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/16 16:39
# @Author : south(南风)
# @File : test2.py
# Describe: 第三次编程
# -*- coding: utf-8 -*-

# 第三次编程第一题
# w = 50
# for i in range(10):
#     w = w + 0.5
#     moon_w = 0.165 * w
#     print("第%d年:地球体重:%.2f------->月球体重:%.2f" % (i + 1, w, moon_w))

# 第二题
# x = 1
# for i in range(1, 366):
#     if i > 3:
#         x = x * 1.01
#
#
# print("%.2f" % x)

# 第三题
import math

# x = (math.pow(2, 4) + 7 - 3 * 4) / 5
#
# x1 = (1 + math.pow(3, 2)) * ((16 % 7) / 7)
#
# print(x)
#
# print(x1)

# 第四题
# x1 = math.sin(2 * math.pi)
# x2 = math.floor(-2.5)
# x3 = math.gcd(12, 9)
# x4 = math.log(math.e)
# x5 = math.floor(3.2)
# x6 = round(math.fabs(-2.5))
# print(x1)
# print(x2)
# print(x3)
# print(x4)
# print(x5)
# print(x6)


# 第五题
# def check(num1):
#     if num1 == num1[::-1]:
#         print(f'{num1}是回文数')
#     else:
#         print(f'{num1}不是回文数')
#
#
# num = input('请输入一个数字:')
# check(num)


# 第六题
# (1)
# s = "hello"
# t = "world"
# s += t
# print(s)
# print(s[-1])
# print(s[2:8])
# print(s[::3])
# print(s[-2::-1])

# (2)
# s = "Python String"
# print(s.upper())
# print(s.lower())
# print(s.find("i"))
# print(s.replace("ing", "gni"))
# print(s.split(" "))

# (3)
# a = 389
# x = ''
# print(bin(a))
# print(oct(a))
# print(hex(a))
# for i in str(a):
#     x += r'\u{}'.format(ord(i))
# print(x)

# (4)
# a = 0.002178
# print('%e' % a)
# print('%.4f' % a)
# print('{:.2%}'.format(a))

# (5)
# print("{:15s}:{:<8.2f}".format("Length", 23.87501))

# 第七题
# import time
#
# for i in range(1, 101):
#     time.sleep(0.1)
#     print("\r", "Download progress: {}%".format(i), end="")
#     for x in range(1, i + 1):
#         if x % 2 == 0:
#             print('\033[37;47m \033[0m', end=" ")


