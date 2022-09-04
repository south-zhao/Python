import easygui as eg
import sys
eg.msgbox("hello,python")
while 1:
    msg = "请问你愿意和我谈恋爱吗？"
    title = "表白"
    #choice = ["谈恋爱", "编程", "游戏", "琴棋书画"]

    #choice = eg.choicebox(msg, title, choice)

    #eg.msgbox("选择" + str(choice), "结果")

    #msg = "你希望重新开始吗"
    #title = "选择"

    if eg.ccbox(msg, title):
        sys.exit()
