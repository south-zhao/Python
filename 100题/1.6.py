def yu(a, b, c):
    def day(a, b, c):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def leap(a):
            global d
            if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
                d = 'leap'
                return d

        days1 = 0
        days3 = 0
        for i in range(1991, a + 1):
            if leap(i-1) == 'leap':
                days2 = 366
            else:
                days2 = 365
            days1 = days1 + days2
        if leap(a) == 'leap':
            days[1] += 1
            for j in range(1, b):
                days3 = days[j - 1] + days3
        else:
            for j in range(1, b):
                days3 = days[j - 1] + days3
        days1 = days1 + days3 + c
        return days1

    a1 = day(a, b, c)
    print(f"相隔{a1}天")
    if (a1 % 5) <= 3:
        print("打鱼！")
    else:
        print("晒网")


d = 'no'

if __name__ == "__main__":
    a = int(input("请输入年份:"))
    b = int(input("请输入月份:"))
    c = int(input("请输入日期:"))
    yu(a, b, c)
