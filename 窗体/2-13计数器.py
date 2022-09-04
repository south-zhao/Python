from tkinter import *


counter = 0


def run(digit):
    def counting():
        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000, counting)

    counting()


tk = Tk()
tk.title("计数器")
d = Label(tk, bg="yellow", fg="blue", height=3, width=10, font="Helvetic 20 bold")
d.pack()
run(d)
mainloop()

