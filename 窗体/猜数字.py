import random
from tkinter import *

i = 1


def tr():
    global i
    if x.get() == a:
        y.set("恭喜你猜对了！\n"
              f"你一共猜了{i}次")
    if x.get() < a:
        y.set("太小了！")
        i += 1
    if x.get() > a:
        y.set("太大了!")
        i += 1
    if x.get() > 100:
        y.set("错误，请重新输入")
        x.set("")


a = random.randint(1, 101)
tk = Tk()
tk.title("猜数字")
x = IntVar()
x.set("")
y = StringVar()
Label(tk, text="请输入一个1-100的数字:", width=40, height=2, anchor="center").grid(row=0)
Entry(tk, textvariable=x).grid(row=1)
Label(tk, textvariable=y, anchor="center", fg="red").grid(row=2)
Button(tk, text="确定", command=tr).grid(row=3)
mainloop()
