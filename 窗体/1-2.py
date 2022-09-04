from tkinter import *

tk = Tk()
tk.title("My")
tk.geometry("300x160+400+200")
tk.configure(bg="red")
Label(tk, text="windows I like python tkinter", bitmap="info", cursor="heart", fg="red", compound="bottom",
      wraplength=50, justify="left", relief="sunken", underline=4, bd=4).pack()
mainloop()
