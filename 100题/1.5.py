books = {1, 2, 3, 4, 5}
a = 0
for i in books:
    for j in books:
        if i != j:
            for z in books:
                if i != j and j != z and i != z:
                    a += 1
                    print(f"A:{i}\tB:{j}\tC:{z}\t", end="   ")
                    if a % 5 == 0:
                        print()
print(a)
