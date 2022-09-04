import random

list1 = []
for i in range(20):
    c = random.randint(1, 100)
    if c not in list1:
        list1.append(c)
b = sorted(list1)
print(b)
a = int(input("输入要查找的数字:"))
length = len(list1) - 1
begin = 0
mid = 0
while (b[begin] < b[length]) and (b[begin] < a < b[length]):
    mid = int((length + begin) / 2)
    if a > b[mid]:
        begin = mid
    elif a < b[mid]:
        length = mid
    else:
        print(mid + 1)
        break
    if (length == begin + 1) and (b[begin] < a < b[length]):
        print("无")
        break
if a <= b[begin] or a >= b[length]:
    length = len(list1) - 1
    begin = 0
    if a == b[begin]:
        print(begin + 1)
    elif a == b[length]:
        print(length + 1)
    else:
        print("无")
