import re

st = '123Qwe!_@#你我他\t \n\r'
res1 = re.findall('\w', st)
res2 = re.findall('\W', st)
res3 = re.findall('\s', st)
res4 = re.findall('\S', st)
print(res1)
print(res2)
print(res3)
print(res4)
