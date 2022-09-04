from tkinter import *


def sta():
    if de.get():
        statu.pack(side=BOTTOM, fill=X)
    else:
        statu.pack_forget()


tk = Tk()
tk.title("che")
tk.geometry("300x180")
men = Menu(tk)
file = Menu(men, tearoff=False)
men.add_cascade(label="File", menu=file)
file.add_command(label="Exit", command=tk.destroy)


vi = Menu(men, tearoff=False)
men.add_cascade(label="View", menu=vi)

de = BooleanVar()
de.set(True)
vi.add_checkbutton(label="Statu", command=sta, variable=de)

tk.config(menu=men)

status = StringVar()
status.set("显示")
statu = Label(tk, textvariable=status, relief="raised")
statu.pack(side=BOTTOM,fill=X)

mainloop()

