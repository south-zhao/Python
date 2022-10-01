import random
import pandas as pd
import numpy as np

data = pd.read_excel('真心话.xlsx', sheet_name='Sheet1', dtype={'c1': str})
a = data['c1']
WORD1 = a
data1 = pd.read_excel('大冒险.xlsx', sheet_name='Sheet1', dtype={'c1': str})
a1 = data1['c1']
WORD2 = a1
print("欢迎来到真心话大冒险")
iscontinue = ""
n = int(input("请输入人数:"))
while iscontinue == "Y" or iscontinue == "":
    i = 1
    j = 1
    while i <= n:
        a = np.random.randint(0, 100, n)
        i += 1                     # 每个人产生一个随机数字
    for i in a:
        print("第", j, "位", ":", i)
        j += 1
    b = np.min(a)     # 找出最小的数字
    print("最小的数字：", b)
    print("第", np.argmin(a) + 1, "位")
    c = int(input("请选择真心话（1）/大冒险（2）："))
    while c != 1 and c != 2:
        c = int(input("错误，请重新输入："))
    if c == 1:
        print(random.choice(WORD1))
    elif c == 2:
        print(random.choice(WORD2))
    iscontinue = input("\n按enter继续，输入N结束:")
