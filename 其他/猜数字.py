import easygui as eg
import random

eg.msgbox('欢迎进入第一个小游戏', '', '继续')
f = random.randint(1, 101)

guess = eg.integerbox('猜猜想的数字是多少(1-100)', '猜数字', lowerbound=1, upperbound=100)
i = 0
while True:
    if guess == f:
        eg.msgbox('恭喜你猜对了！')
        eg.msgbox('可惜没有奖励')
        break
    else:
        if guess > f:
            eg.msgbox("哥，大了大了~~~")
            i += 1
        else:
            eg.msgbox("嘿，小了小了~~~")
            i += 1
        guess = eg.integerbox('猜猜想的数字是多少(1-100)', '猜数字', lowerbound=1, upperbound=100)

eg.msgbox("游戏结束了,你一共猜了%d次" % i)

