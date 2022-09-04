import easygui as eg

f = open('题目.txt', 'r', encoding='utf-8')
eg.codebox('文件内容', '', text=f.read())
