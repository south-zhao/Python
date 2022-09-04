from tkinter import *


def bgu(source):
    red = rSlider.get()
    green = gSlider.get()
    blue = bSlider.get()
    print("R=%d, G=%d, B=%d" % (red, green, blue))
    myColor = "#%02x%02x%02x" % (red, green, blue)
    c.config(bg=myColor)


tk = Tk()
tk.title("画布")
c = Canvas(tk, width=640, height=240)
rSlider = Scale(tk, from_=0, to=255, command=bgu)
gSlider = Scale(tk, from_=0, to=255, command=bgu)
bSlider = Scale(tk, from_=0, to=255, command=bgu)
gSlider.set(125)
rSlider.grid(row=1, column=1)
gSlider.grid(row=1, column=2)
bSlider.grid(row=1, column=3)
c.grid(row=2, column=1, columnspan=3)
mainloop()
