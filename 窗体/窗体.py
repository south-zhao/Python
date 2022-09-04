from tkinter import *


root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.title("MyWindow")
label = Label(root, text="I like tkinter", fg="yellow", bg="blue", height=5, width=15, anchor="center",
              wraplength=40, font="Helvetic 10 bold")
label.pack()
w = 300
h = 160
x = (screenWidth - w) / 2
y = (screenHeight - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))  # root.geometry("300x160+400+400")
root.mainloop()
