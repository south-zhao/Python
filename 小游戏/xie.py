import pandas as pd
import csv

df = pd.read_excel('1.xlsx', sheet_name=0)
print(df.c1)

result_list = []
username_list = pd.read_excel('1.xlsx', usecols=[0], index_col=None)
# print(username_list)
content_list = pd.read_excel('1.xlsx', sheet_name=0, index_col=1)
# print(content_list)
reply_time_list = pd.read_excel('1.xlsx', sheet_name=0, index_col=2)
# print(reply_time_list)

for i in range(len(username_list)):
    result = {'username': username_list[i],
              'content': content_list[i],
              'reply_time': reply_time_list[i]}
    result_list.append(result)

with open('tieba.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['username', 'content', 'reply_time'])
    writer.writeheader()
    writer.writerows(result_list)

import xlrd
import xlwt

workbook = xlrd.open_workbook('1.xlsx')
# sheet_names()获取文件当中所有sheet名字
print(workbook.sheet_names())
# sheet_by_index() 通过索引获取对象
sheet = workbook.sheet_by_index(1)
print(sheet.name)
# sheet_by_name()  通过名字获取对象
sheet = workbook.sheet_by_name('c1')
print(sheet.name)
# sheets()  获取所有sheet对象 返回值是list
sheet = workbook.sheets()
print(sheet)
# sheet.nrows() 获取指定sheet行数
sheet = workbook.sheet_by_name('pieChart')
print(sheet.nrows)
# sheet.ncols() 与上面同理
