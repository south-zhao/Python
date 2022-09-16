from tkinter import *


def min():
    tk.iconify()


def show(event):
    popupmenu.post(event.x_root, event.y_root)


tk = Tk()
tk.title("ch")
tk.geometry("300x100")

popupmenu = Menu(tk, tearoff=False)

popupmenu.add_command(label="Min", command=min)
popupmenu.add_command(label="Exit", command=tk.destroy)
tk.bind("<Button-3>", show)
mainloop()
