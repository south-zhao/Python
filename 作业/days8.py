"""
1.以覆盖写的方式  创建一份文件  文件里面写的数据是 '我的名字是XX'
2. 读取1当中的文件的内容
3. 将2中读取到的内容以追加写的方式 写入到另外一份文件
"""

# f = open('作业.txt', 'w', encoding='utf-8')

# f.write(a)
# f.close()
# print("over!")

# data = open('作业.txt', 'r', encoding='utf-8')
# content = data.read()
# print(content)
# data.close()
# file = open('作业.txt', 'a+', encoding='utf-8')
# a = "我的名字是爱吃柚子的小赵"
# file.write(a)
# file.seek(0)
# b = file.read()
# print(b)
# file.close()

# with open('作业.txt', 'a+', encoding='utf-8') as a:
#     a.seek(0)
#     for x in a:
#         print(x)

with open('作业.txt', 'a+', encoding='utf-8') as a:
    a.seek(0)
    print(a.readlines()[::-1])






