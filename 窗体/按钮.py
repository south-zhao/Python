from tkinter import *
import math


tk = Tk()
tk.title("weilai")
canvans = Canvas(tk, width=640, height=480)
canvans.pack()
canvans.create_line(100, 100, 200, 100, width=10, fill='red')
x_c, y_c, r = 320, 240, 100
x, y = [], []
for i in range(12):
    x.append(x_c + r * math.cos(30*i*math.pi/180))
    y.append(y_c + r * math.sin(30*i*math.pi/180))
for i in range(12):
    for j in range(12):
        canvans.create_line(x[i], y[i], x[j], y[j])
mainloop()

