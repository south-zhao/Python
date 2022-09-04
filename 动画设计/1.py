from tkinter import *
import time
from random import *


tk = Tk()
tk.title("hello")
c = Canvas(tk, width=640, height=480)
c.pack()
id1 = c.create_oval(10, 50, 60, 100, fill='yellow', outline='lightgray', width=5)
id2 = c.create_oval(10, 150, 60, 200, fill='blue', outline='aqua', width=5)
for i in range(0, 1000):
    if randint(1, 100) > 60:
        c.move(1, 4, 0)
    else:
        c.move(2, 3, 0)
    c.update()
    time.sleep(0.05)
mainloop()
