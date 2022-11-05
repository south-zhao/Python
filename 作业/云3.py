# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/11/3 15:09
# @Author : south(南风)
# @File : 云3.py
# Describe: 
# -*- coding: utf-8 -*-
# def pr():
#     print("向颖")
#
#
# if __name__ == '__main__':
#     pr()

# def re_pr(name, num):
#     for i in range(num):
#         print(name)
#
#
# if __name__ == '__main__':
#     name = input("输入姓名:")
#     num = int(input("输入要打印的次数:"))
#     re_pr(name, num)


# def separate(num):
#     list1 = []
#     for i in num:
#         list1.append(i)
#     tuple1 = tuple(list1)
#     return tuple1
#
#
# if __name__ == '__main__':
#     num = input("请输入一个小于10000的数字:")
#     a = separate(num)
#     print(a)


def getBMI(w, h):
    bmi = w / (h * h)
    if bmi < 18:
        con = "偏瘦"
    elif 18 <= bmi < 25:
        con = "正常体重"
    elif 25 <= bmi < 30:
        con = "超重"
    elif 30 <= bmi < 35:
        con = "轻度肥胖"
    elif 35 <= bmi < 40:
        con = "中度肥胖"
    else:
        con = "重度肥胖"

    return bmi, con


if __name__ == '__main__':
    weight = float(input("请输入你的体重(kg):"))
    height = float(input("请输入你的身高(m):"))
    b, r = getBMI(weight, height)
    print("%.3f  %s" % (b, r))





