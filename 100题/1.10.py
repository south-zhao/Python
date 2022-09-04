def char_to_num(ch):
    if '0' <= ch <= '9':
        return int(ch)
    else:
        return ord(ch)  # 将字母字符转变为数字


def num_to_char(num):
    if 0 <= num <= 9:
        return str(num)
    else:
        return chr(num)  # 将数字转变为字符


def s_to_d(temp, s):
    d_num = 0
    for i in range(len(temp)):
        d_num = (d_num*s)+char_to_num(temp[i])

    return d_num


def d_to_o(d_num, obj):
    d = []
    while d_num:
        d.append(num_to_char(d_num % obj))
        d_num //= obj

    return d


def out(d):
    f = len(d) - 1
    while f >= 0:
        print(d[f], end="")
        f -= 1
    print()


M = 101
flag = 1
while flag:
    print("之前的数：")
    temp = input()
    print("之前数制：")
    s = int(input())
    print("后的数制")
    obj = int(input())
    print("结果:")
    d_num = s_to_d(temp, s)
    d = d_to_o(d_num, obj)
    out(d)
    print("1 或 0（结束）")
    flag = int(input())
