from tkinter import *
import time


def ballMove(event):
    if event.keysym == 'Left':  # 左移
        c.move(id1, -5, 0)
    if event.keysym == 'Right':  # 右移
        c.move(id1, 5, 0)
    if event.keysym == 'Up':  # 上移
        c.move(id1, 0, -5)
    if event.keysym == 'Down':  # 下移
        c.move(id1, 0, 5)


tk = Tk()
tk.title('游戏')
c = Canvas(tk, width=640, height=480)
c.pack()
id1 = c.create_oval(300, 220, 340, 260, fill='red')
c.bind_all('<KeyPress-Left>', ballMove)
c.bind_all('<KeyPress-Right>', ballMove)
c.bind_all('<KeyPress-Up>', ballMove)
c.bind_all('<KeyPress-Down>', ballMove)
mainloop()
