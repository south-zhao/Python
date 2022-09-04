import pandas as pd


df1 = pd.DataFrame({'公司': ['恒盛', '创锐', '快学'], '分数': [90, 95, 85]})
df2 = pd.DataFrame({'公司': ['恒盛', '创锐', '京西'], '股价': [20, 180, 30]})
df3 = pd.concat([df1, df2], axis=0)  # 不写axis默认为0，纵向拼接
print(df3)

df3 = pd.concat([df1, df2], ignore_index=True)  # 更改索引
print(df3)

# df3 = df1.append(df2)  # 淘汰
# print(df3)
# df3 = df1.append({'公司': '腾飞', '分数': '90'}, ignore_index=True)
# print(df3)
