import pandas as pd


df1 = pd.DataFrame({'公司': ['恒盛', '创锐', '快学'], '分数': [90, 95, 85]})
df2 = pd.DataFrame({'公司': ['恒盛', '创锐', '京西'], '股价': [20, 180, 30]})
# print(df1)
# print(df2)
df3 = pd.merge(df1, df2, on='公司')  # on是合并的那一列，如果有很多列有共同内容
print(df3)
df4 = pd.merge(df1, df2, how='outer')  # 并集
print(df4)

df5 = pd.merge(df1, df2, how='left')  # 保留左边的完整
print(df5)

df6 = pd.merge(df1, df2, left_index=True, right_index=True)
print(df6)
