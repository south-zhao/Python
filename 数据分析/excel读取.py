# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Author  : south(南风)
# @Time    : 2022/9/10 13:46
# @File    : excel读取.py
# @Software: PyCharm
# @Describe: 读取excel表格里面的内容
import xlrd

book = xlrd.open_workbook("grade.xlsx")

for sheet in book.sheets():
    print(sheet.name)



