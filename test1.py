# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/16 16:23
# @Author : south(南风)
# @File : test1.py
# Describe: 
# -*- coding: utf-8 -*-


# 第二次编程第一题
class Transform:
    def __init__(self):
        self.money = 0
        self.dollar = 0

    def m_d(self):
        self.money = float(input("请输入人民币的金额:"))
        self.dollar = self.money / 6
        print(f"人民币：{self.money} ===>  美元：{self.dollar}")

    def d_m(self):
        self.dollar = float(input("请输入美元的金额:"))
        self.money = self.dollar * 6
        print(f"美元：{self.dollar} ===>  人民币：{self.money}")

    def run(self):
        while True:
            print("""            ========欢迎进入汇率转换系统======
            |1.人民币转美元                 |
            |2.美元转人民币                 |
            |3.退出                       |
            ==============================
            """)
            choose = input("请输入你要进行的操作对应的数字:")
            if choose == '1':
                self.m_d()
            elif choose == '2':
                self.d_m()
            else:
                break


if __name__ == '__main__':
    a = Transform()
    a.run()

import turtle
#
# for i in range(1, 4):
#     turtle.fd(200)
#     turtle.seth(120*i)
# turtle.done()
#
# for i in range(1, 4):
#     turtle.fd(100)
#     turtle.seth(-120 * i)
# turtle.seth(60)
# turtle.fd(100)
# turtle.seth(-60)
# turtle.fd(200)
# turtle.seth(180)
# turtle.fd(200)
# turtle.seth(60)
# turtle.fd(100)
# turtle.done()
#
# turtle.speed(8)
# for i in range(100):
#     turtle.fd(5 * (i + 1))
#     turtle.left(90)
# turtle.done()


turtle.circle(10)
for i in range(1, 9):
    turtle.penup()
    turtle.right(90)
    turtle.fd(10)
    turtle.pendown()
    turtle.left(90)
    turtle.circle((i+1) * 10)

turtle.done()
