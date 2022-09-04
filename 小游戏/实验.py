import random
import pandas as pd

data = pd.read_excel('单词1.xlsx', sheet_name='Sheet1', dtype={'c1': str, 'c2': str})
a = data['c1']
WORDS = a
a1 = data['c2']
WORDS1 = a1
word = random.choice(WORDS)
print(WORDS1[list(WORDS).index(word)])
