# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/11/15 12:17
# @Author : south(南风)
# @File : 云4.py
# Describe:
# -*- coding: utf-8 -*-
# 第一题
# import random


# def compare(a, b):
#     with open(a, 'r', encoding='utf-8') as f, open(b, 'r', encoding='utf-8') as f1:
#         data = f.read()
#         data1 = f1.read()
#     if data == data1:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     a = input("输入第一个文件名:")
#     b = input("输入第二个文件名:")
#     res = compare(a, b)
#     if res:
#         print("NO difference!")
#     else:
#         print("difference!")


# 第二题
# import random
#
#
# def chose():
#     with open('student.txt', 'r', encoding='utf-8') as f:
#         data = f.read()
#     data = data.split(" ")
#     data = [i.strip('\n') for i in data]
#     random.shuffle(data)
#     num = random.choice(data)
#     print(num)
#
#
# if __name__ == '__main__':
#     chose()
#     while True:
#         a = input("是否继续抽取(Y/N):")
#         if a == "Y":
#             chose()
#         else:
#             break


# 第三题
def score(answer):
    with open('answer.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        data = [i.strip("\n") for i in data]
        # print(data)
        sum1 = 0
        for i, j in zip(data, answer):
            num = i.index(j)
            sc = int(i[num+1]+i[num+2])
            sum1 += sc
        print(f'总成绩为{sum1}')


if __name__ == '__main__':
    a = input("请输入答案:")
    score(a)



