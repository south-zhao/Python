from tkinter import *
from tkinter import messagebox


def newfile():
    messagebox.showinfo("New File", "新建文档")


def openfile():
    messagebox.showinfo("New File", "打开文档")


def savefile():
    messagebox.showinfo("New File", "保存文档")


def saveAsfile():
    messagebox.showinfo("New File", "另存为")


def about():
    messagebox.showinfo("About me", "赵鑫杰作")


def findNext():
    messagebox.showinfo("Find Next", "查找下一个")


def pro():
    messagebox.showinfo("Find Pro", "查找上一个")


tk = Tk()
tk.title("菜单")
tk.geometry("300x180")

men = Menu(tk)
filemenu = Menu(men, tearoff=False)
findmenu = Menu(filemenu, tearoff=False)
men.add_cascade(label="File", menu=filemenu)
filemenu.add_cascade(label="Find", menu=findmenu)
findmenu.add_command(label="Find Next", command=findNext)
findmenu.add_command(label="Find Pro", command=pro, accelerator="Ctrl+A")
filemenu.add_command(label="New File", command=newfile, underline=1)
filemenu.add_command(label="Open file", command=openfile, accelerator="Ctrl+n")
filemenu.add_separator()
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Save as", command=saveAsfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=tk.destroy)

helpmenu = Menu(men, tearoff=False)
men.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)
tk.config(menu=men)
tk.bind("<Control-n>",lambda event: messagebox.showinfo("New File", "打开文档"))
tk.bind("<Control-A>", lambda event: messagebox.showinfo("Find Pro", "查找上一个"))
mainloop()
