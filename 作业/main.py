import sys  # 导入sys模块
import tkinter as tk

import ttkbootstrap as ttk

sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000

class m_d_p:
    def G_M(self):
        root = ttk.Window(
            title="音乐下载器",  # 设置窗口的标题
            themename="litera",  # 设置主题
            size=(450, 450),  # 窗口的大小
            position=(450, 200),  # 窗口所在的位置
            minsize=(0, 0),  # 窗口的最小宽高
            maxsize=(1920, 1080),  # 窗口的最大宽高
            resizable=None,  # 设置窗口是否可以更改大小
            alpha=1.0)  # 设置窗口的透明度(0.0完全透明）

        label1 = ttk.Label(root, text='搜索', bootstyle='info')  # 在root界面中创建一个文本框，文本框的内容为text
        label1.grid()  # 在root界面中定位label1，默认位置为窗口的左上角

        entry1 = ttk.Entry(root, show=None)  # 在root界面创建输入框
        entry1.insert('0', '歌曲名字或作者')
        entry1.grid(row=0, column=1)  # 在root界面中定位entry1，位置为0行，2列

        var = ttk.StringVar()  # 声明一个特殊变量StringVar，用于表示单选按钮
        r1 = ttk.Radiobutton(root, text='网易云', variable=var, value='netease')  # 设置单选按钮r1的参数
        r1.grid(row=1, column=0)  # 在root界面中定位r1的位置

        r2 = ttk.Radiobutton(root, text='QQ', variable=var, value='qq')  # 再设置一个单选按钮r2
        r2.grid(row=1, column=1)  # 在root界面中定位r2的位置

        box = tk.Listbox(root, width=50, heigh=15)  # 在root界面中设置一个列表框，框宽50，高15
        box.grid(row=2, columnspan=2)  # 定位列表框，columnspan=2表示横跨两列

        label2 = ttk.Label(root, text='页数:', bootstyle='info')
        label2.grid(row=3, column=0)

        entry2 = ttk.Entry(root)
        entry2.grid(row=3, column=1)

        button1 = ttk.Button(root, text='搜索', bootstyle=('primary', "outline-toolbutton"))  # 在root界面中设置一个按钮1
        button1.grid(row=4, column=0)  # 定位按钮1

        button2 = ttk.Button(root, text='下载', bootstyle=('primary', "outline-toolbutton"))  # 在root界面中设置一个按钮2
        button2.grid(row=4, column=1)  # 定位按钮2

        root.mainloop()  # 显示界面

    def m_s(self):
        get_ = self.G_M().entry1.get()
        print(get_)

    def m_d(self):
        return 0

if __name__ == '__main__':
    a = m_d_p()
    a.G_M()
