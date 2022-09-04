# 准备作案工具
import win32gui as gui  # gui--图形用户界面 -- 窗口程序
import win32con as con  # control = 控制权限

# 1.找到要发送的对象(通过窗口名字)   找窗口(1.窗口类型 2.窗口名字)
handle = gui.FindWindow(0,'70')
for i in range(4):
    # 2.准备要发送的内容
    # gui窗口 send发送  message消息  给窗口发送一个消息(黏贴)
    gui.SendMessage(handle,con.WM_PASTE)

    # 3.发送消息
    # 给窗口发送一个消息(发送对象,按下一个键,指定回车键)
    gui.SendMessage(handle,con.WM_KEYDOWN,con.VK_RETURN)

