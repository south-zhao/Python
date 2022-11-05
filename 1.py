
# 第一题
# a = 0
# for i in range(3):
#     b = int(input(" "))
#     a += b
# a = a / 3
# print("%.3f" % a)

# 第二题
# for i in range(65, 91):
#     print(chr(i), end="")
#
# print()
#
# for i in range(97, 123):
#     print(chr(i), end=" ")
#
# # 第三题
# a = input("")
# print(a[::-1])
#
#
# # 第四题
# dict1 = {"张三": 90, "李四": 88, "王五": 77, "李雷": 82, "韩梅梅": 95}
# dict1 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
# for i in dict1:
#     x, y = i
#     print(x, " ", y)
#
# # 第五题
def sum_MN(m, n):
    sum1 = 0
    for i in range(m, n + 1):
        sum1 += i
    print(sum1)

sum_MN(100, 200)
sum_MN(200, 300)


