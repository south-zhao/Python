# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/11/11 19:58
# @Author : south(南风)
# @File : day2.py
# Describe:
# -*- coding: utf-8 -*-
"""
tuple 元组
和列表基本相同  但是它里面的数据不可更改
用()定义
"""
# a = (1, 2, 3)
# print(type(a))
# print(a[1])

# a = (1, 2, 3, [1, 2, 3, 4])  # 可以改列表里的
"""
用户交互
    我的代码能够与用户进行交流，用户可以操作
    input("提示信息")  输入    进行到这，就会等待用户的输入    输入的数据的数据类型为str
    print 输出    sep以。。。隔开   默认空格，可以更改   end以..结尾 默认换行
    
格式化输出
    %s进行占位  字符串%s  整型%d  用%来将占位符与变量一一对应   print("你的姓名是%s,你的年龄是%s" % (a, b))
    f""   在引号里输入内容，对应位置用大括号将你的变量名包裹起来
    ”{} {}“.format(变量名, 变量名)  对应位置用大括号进行占位  如果不写位置参数 默认与后面的变量名按照默认位置一一对应
    也可在里面输入对于变量名的位置参数  从0开始  "你的姓名是{1},你的年龄是{0}".format(a, b)  此时0的位置输出a变量 1的位置输出b变量
"""
# a = input("请输入你的姓名:")
# print(type(a))
# print(a)

# print(1, 2, sep='!')
# print(1, end=' ')
# print(2)
# print(3)


# a = input("请输入你的姓名:")
# b = input("你的年龄是:")
# print("你的姓名是" + a)
# print("你的姓名是%s,你的年龄是%s" % (a, b))
# print(f"你的姓名是{a},你的年龄是{b}")
# print("你的姓名是{1},你的年龄是{0}".format(a, b))
"""
链式赋值
    ·变量名=变量名=变量名=值
交叉赋值
    变量名1， 变量名2， 变量名3.。。。=值1，值2，值3.。。
    左右变量名与值一一对应
解压赋值
    变量名1， 变量名2.。。=str/list/tuple/dict
    *_接受除了你规定的变量以外的剩余数据
    对于字典，接受的是键名
成员运算符
   in   not in 
"""

# a = b = c = 1
# a = 5
# b = 3
# a, b = b, a
# print(a, b)


# str1 = "你好呀！"
# a, *_, b = str1
# print(a, b)

# dict1 = {"ni": 1, "dhj": 3}
# a, b = dict1
# print(a, b)

"""
if分支结构
    做和不做  二选一
    这个，那个，另外一个  多选一
二选一
    if 条件:
        结果（必须要缩进）
    else
    
多选一
    if
    
    elif
    
    else（可有可无）
"""
# age = input("请输入你的年龄:")
# age = int(input("请输入你的年龄:"))
# if age < 0:
#     print("输入错误")
# else:
#     if age < 18:
#         print("你还未成年")
#     else:
#         print("你已经成年")
# if age[0] == "-":
#     print("输入错误")
# else:
#     if int(age) < 18:
#         print("你还未成年")
#     else:
#         print("你已经成年")

"""
循环结构（for能做的while也可以， while可以的的for不一定可以）
    while 条件:
        代码
    while
        条件循环
        break
            直接停止
        continue
            从下一次再开始
    for
        迭代循环
        循环的次数取决于你in后面的变量的长度 或者是range的所有可能性
        range(数字)  是几就循环几次
        range(开始的数字，结束的数字，步长)   左闭右开
        
        for 变量名 in range(), str, list,dict,tuple,set,file
"""
# for i in "你好吗":
#     print(i)
# for i in range(5):
#     print(i)
i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i-1)






