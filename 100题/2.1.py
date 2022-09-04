def man():
    a = 0
    for i in range(4):
        for j in range(4):
            if (i + j) >= 2:
                for m in range(7):
                    if (i + j + m) == 8:
                        a += 1
                        print(i, "   ", j, "     ", m, "\n")

    return a


a = man()
print(a)
