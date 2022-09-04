for i in range(20):
    for j in range(33):
        k = 100 - 5 * i - 3 * j
        if 3 * k + i + j == 100:
            print(f"公鸡:{i}只\n母鸡:{j}只\n小鸡:{3 * k}只")
            print("----------")
