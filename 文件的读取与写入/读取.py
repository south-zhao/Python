import pandas as pd


data = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A', 'B'])
#data.index.name = 'F'
#data.reset_index()
data.to_excel('E:\\example.xlsx', index=False)
data.to_csv('data.csv', index=False)
file1 = pd.read_csv('data.csv')
file = pd.read_excel('E:\\example.xlsx', sheet_name=0)
print(file)
print(file1)
