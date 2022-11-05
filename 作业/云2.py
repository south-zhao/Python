# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/26 9:47
# @Author : south(南风)
# @File : 云2.py
# Describe: 
# -*- coding: utf-8 -*-

# 第一题第一问
# a = {1, 2, 3, 4, 5}
# b = {2, 4, 6}
# 第一种写法
# c = a - b
# 第二种写法
# c = a.difference(b)
# print(c)

# 第一题第二问
# 第一种写法
# d = a & b
# 第二种写法
# d = a.intersection(b)
# print(d)

# 第一题第三问
# 第一种写法
# e = a | b
# 第二种写法
# e = a.union(b)
# print(e)


# 第二题第一问
# dic_student = {}  # 第一种方法
# dic_student = dict()  # 第二种方法

# 第二题第二问
# for i in range(5):
#     name = input("请输入姓名:")
#     age = input("请输入年龄:")
#     dic_student[name] = age

# 第二题第三问
# for n, a in dic_student.items():
#     print("{0:{2}<5}{1:<5}".format(n, a, chr(12288)))

# 第二题第四问
# age = list(dic_student.values())
# age.sort()
# age_max = age[len(age) - 1]
# age_min = age[0]
# sum = 0
# for i in age:
#     sum += int(i)
#
# print(sum / len(age))
# print(age_max)
# print(age_min)

# 第三题
# 第一问的存储
# information = {'John': 123, 'Marry': 111, 'Tommy': 123456}
#
# while True:
#     # 这两步是第二问的要求输入信息
#     account = input("请输入用户名:")
#     password = int(input("请输入密码:"))
#     # 这是第三问的判断信息
#     if account in list(information.keys()):
#         if password == information[account]:
#             print("登录成功")
#             break
#         else:
#             print("密码不正确")
#     else:
#         print("用户名不正确")





