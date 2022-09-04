def fun(x):
    if x < 3:
        return 1
    else:
        return fun(x-1) + fun(x-2)


for i in range(1, 31):
    a = fun(i)
    print("%6d" % a, end="     ")
    if i % 5 == 0:
        print()
