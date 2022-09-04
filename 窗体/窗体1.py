from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("zxj")
root.geometry("680x680")

image = Image.open("恋爱协议.jpg")
恋爱协议 = ImageTk.PhotoImage(image)
label = Label(root, compound="left", text="我的世界", image=恋爱协议, relief="solid")
label.pack()
root.mainloop()
