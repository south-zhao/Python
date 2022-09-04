from tkinter import *
from random import *

tk = Tk()
tk.title("re")
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
for i in range(50):
    x1, y1 = randint(1, 640), randint(1, 480)
    x2, y2 = randint(1, 640), randint(1, 480)
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    canvas.create_rectangle(x1, y1, x2, y2, outline="blue", fill="pink")
mainloop()
