"""
一个四位数，前两位数相同，后两位数相同，但是与前两位不相同
4位数刚好是一个整数的平方
求这个四位数
"""
flog = 0
for i in range(10):
    if flog:  # 优化算法，一旦找到就停止程序
        break
    for j in range(10):
        if flog:  # 优化算法，一旦找到就停止程序
            break
        if i != j:
            k = 1000 * i + 100 * i + 10 * j + j
            for each in range(31, 100):
                if each * each == k:
                    print("车牌号为:", k)
                    flog = 1  # 优化算法，一旦找到就停止程序
                    break
