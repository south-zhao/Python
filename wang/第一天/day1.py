# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/11/5 8:37
# @Author : south(南风)
# @File : day1.py
# Describe:
# -*- coding: utf-8 -*-
# 注释：起到解释说明的作用
# 前面加上#，#后的内容表示注释内容，不执行  单行注释
"""
多行注释：三对引号，引号里面包裹的内容全部都是注释
英文单双号都可以，
"""
# TODO 帮助我们快速定位到我们注释代码的位置

"""
变量：用来保存和记录一些数据
定义一个变量，有三步:
    1.开辟一个内存空间
    2.将数据放入内存空间
    3.将变量名和内存空间的地址进行绑定
    
使用变量的话：先定义再使用

变量定义的模板：
    变量名 = 数据/值(必须赋予初值)

变量名的命名:
    1.只能由数字，英文字母，英文下划线组成
    2.不能以数字开头
    3.不能和你编程语言的一些关键字冲突
    
变量名的三大特性:
    1.数据类型（可以看作人的性别）
    2.值（可以看作人本身）
    3.地址（人的身份证号）
"""

# import keyword
#
# print(keyword.kwlist)
# print(type(keyword.kwlist))

# money = 100.1
# print(money)  # 看值
# print(id(money))  # 看id
# print(type(money))  # 看数据类型

# 小整数池的概念  当你的数据在[-5, 256]时如果数值相同，id也相同
# a = 32
# b = 32
# print(id(a))
# print(id(b))

# a = -18
# b = -18
# print(id(a))
# print(id(b))

# 数据类型
"""
数字类型：
    1.int 整型
    2.float 浮点型
"""
# a = 100
# print(type(a))
# b = 1001.111111111111111
# print(type(b))

"""
字符串：
    用来记录和描述一些东西
    str 用一对英文的单，双引号(记录一行的数据)
    用三对单，双引号包裹
    1.相加
    2.相乘
    单包双，双包单
"""
str1 = '今天有点冷'
str2 = "希望明天会更好"
# print(str1 + str2)
# print(str1 * 3)
# print(type(str1))
# print(type(str2))
# str3 = """床前明月光
# 疑是地上霜
# 举头望明月
# 低头思故乡
# """
# print(str3)
"""
列表：
    变量名 = []（定义了一个空列表）
    变量名 = list(可迭代对象)
    [] 元素  个数不限，数据类型不限 
取：
    list[位置参数]
索引：
    从0开始，第一个数据的位置是0
    取最后一个元素的方法:
        1.list1[-1]
        2.list1[len(list1) - 1]
        3.list1.pop() 用变量接收
        
    list1.pop(位置参数) 如果不写位置参数，默认删除最后一个，有返回值，将你删除的那个数据返回出来
    
改: 
    list[位置] = 新值
切片：
    list[开始的位置:结束的位置 + 1:步长]  (左闭右开)
"""
# list1 = list(str1)
# print(list1)


# list2 = []
# for i in str1:
#     list2.append(i)
# print(list2)

# 错误的，但是我们可以将其转化成字符串
# list1 = list(12345)
# list2 = list("1234")
# print(list1)
# list1 = [123, "你好", 19.9, [19, "hucsa", 19.2]]
# print(list1[0:2])
# list1[0] = 234
# print(list1)
# length = len(str1)  # 计算长度
# print(length)
# print(list1[-1])
# print(list1[len(list1) - 1])
# a = list1.pop(1)
# print(a)
# print(list1)
# print(list1[3][0])
"""
字典:
    键值对  键和值一一对应
    变量名 = {}(定义一个空字典)
    变量名 = {键: 值, 键: 值...}
    取值: dict[键名]
    键必须是唯一的，int,float,str(较多),tuple,bool(不建议)
    值:任意
    
bool ：True, False
"""
# dict1 = {"height": 171, "weight": 69}
# print(dict1["height"])


a = [511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 522]
print(a[int((len(a) - 1) / 2)])

"""
a = {
    '小赵':{'姓名':'小赵','年龄':18,'爱好':['唱歌','打篮球',['中国风歌曲']]}
}
索引和根据键取值，修改值
1. 输出小赵的第二个爱好
2. 将小赵的中国风歌曲改成rap   无限套娃操作

选择合适的数据类型，定义一个变量来表示自己的名字，年龄，爱好

以下代码有什么问题？
_1 = 2
12  = 3
int = python
a = [1,[[2]
b = {[1]:1}
c = {11,22:33}
"""
