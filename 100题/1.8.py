def sort(b):
    n = len(b)
    j = 1
    while j <= n-1:
        m = 0
        while m < n-j:
            if a[m] > a[m+1]:
                a[m], a[m+1] = a[m+1], a[m]
            m += 1
        j += 1
    for each in a:
        print(each, end="  ")


x = input()
a = x.split(" ")
for i in range(0, len(a)):  # 类型转换
    a[i] = int(a[i])
print(a)
print("------------")
sort(a)
