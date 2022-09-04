import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(1, 10).reshape(3, 3), columns=['c1', 'c2', 'c3'], index=['r1', 'r2', 'r3'])
# print(data)
# 按列选取
a = data['c1']
print(a)
# 输出列索引
b = data[['c1']]
print(b)
c = data[['c1', 'c3']]
print(c)
# 按行选取，左闭右开
a = data.iloc[1:3]
print(a)
# 名称选取
b = data.loc[['r2', 'r3']]
print(b)
# 行数很多用head（）选取前五行
c = data.head()
print(c)
d = data.head(2)
print(d)
# 按区块选取
a = data[['c1', 'c3']][0:2]  # 不推荐
print(a)
# 推荐
b = data.iloc[0:2][['c1', 'c3']]
print(b)
c = data.loc[['r1', 'r2'], ['c1', 'c3']]
print(c)
# 数据筛选
a = data[(data['c1'] > 1) & (data['c2'] == 5)]
print(a)

b = data.loc[data.c1 > 5]
print(b)


# 数据的排序
a = data.sort_values(by='c2', ascending=False)
a = a.sort_index()
print(a)

# 运算
data['c4'] = data['c3'] - data['c1']
print(data)

# 删除
a = data.drop(columns='c4', index='r1', inplace=True)
# print(a)
print(data)
