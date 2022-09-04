from tkinter import *
import pickle

users = []
users.append({'id': 'admin', 'pwd': '1234'})
users.append({'id': 'guest', 'pwd': '123'})
users.append({'id': 'python', 'pwd': '12345'})
with open('user.pkl', 'wb') as f:
    pickle.dump(users, f)
with open('user.pkl', 'rb') as f:
    f = pickle.load(f)
root = Tk()

Label(root, text="账号").grid(row=0)
Label(root, text="密码").grid(row=1)

v1 = StringVar()
v2 = StringVar()

e1 = Entry(root, textvariable=v1)
e2 = Entry(root, textvariable=v2, show="*")
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def ch():
    m = 0
    idok = False
    while not idok:
        for i in f:
            if v1.get() == i['id']:
                print("恭喜你输入正确")
                idok = True
                break
        if not idok:
            print("账号error")
            break
        while idok:
            if v2.get() == i['pwd']:
                print("恭喜你输入正确")
                break
            if idok:
                print("密码error")
                break


Button(root, text="kaim", width=10, command=ch).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="tui", width=10, command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()
