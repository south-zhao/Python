# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/28 21:25
# @Author : south(南风)
# @File : D1.py
# Describe: 
# -*- coding: utf-8 -*-

# 第一题
# def BMI(w, h):
#     bmi = w / (h * h)
#     return bmi
#
#
# def tzl(w, h, a, s):
#     bmi = BMI(w, h)
#     tzl = 1.2 * bmi + 0.23 * a - 5.4 - 10.8 * s
#     print(f"你的BMI为{bmi}")
#     print(f"你的体脂率为{tzl}")
#
#
# if __name__ == '__main__':
#     weight = float(input("请输入你的体重(kg):"))
#     height = float(input("请输入你的身高(m):"))
#     age = int(input("请输入你的年龄:"))
#     sex = int(input("请输入你的性别对应的数字(男: 1, 女: 0):"))
#     tzl(weight, height, age, sex)

# 第二题
# import math
# s = 0
# for i in range(1, 101): # 算10000的话将101改为10001
#     s = s + 1 / math.pow(i, 2)
#
# print(math.pow(6 * s, 0.5))
# print(s)
# 第三题
# import math
# s = 1
# for i in range(1, 3): # 此处和上一处相同
#     s = s + 1 / math.factorial(i)
# print(s)


def opposite(list1):
    list1.sort()
    max1 = list1[len(list1) - 1]
    min1 = list1[0]
    jicha = max1 - min1
    sum1 = 0
    for i in list1:
        sum1 += i
    opposite_ji = jicha / (sum1 / len(list1))
    print("%.6f" % opposite_ji)


if __name__ == '__main__':
    list1 = []
    while True:
        num = input("请输入数字(结束的话输入n):")
        if num == "n":
            break
        list1.append(float(num))
    opposite(list1)


