from tkinter import *

tk = Tk()
c = Canvas(tk, width=640, height=480, bg="yellow")
c.pack()

c.create_arc(10, 10, 110, 110, extent=45, style=ARC)
c.create_arc(10, 110, 310, 410, extent=90, width=5, outline="blue", fill="pink")
c.create_arc(100, 200, 250, 450, extent=359, style=ARC, width=10, outline="red")
c.create_oval(100, 200, 250, 450, width=10, outline="red", fill="aqua")
c.create_oval(10, 10, 110, 110, fill="yellow")
myPict = PhotoImage(file='../img/title1.gif')
c.create_image(0, 0, image=myPict, anchor=NW)
mainloop()
