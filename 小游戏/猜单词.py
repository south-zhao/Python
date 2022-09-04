import random
import pandas as pd

data = pd.read_excel('单词1.xlsx', sheet_name='Sheet1', dtype={'c1': str, 'c2': str})   #读取单词1表格
a = data['c1']    #将表格第一列给a，创建元组
WORDS = a
a1 = data['c2']     #将表格第二列给a1，创建元组
WORDS1 = a1
print(
    """
             欢迎参加猜单词游戏
         把字母组合成为一个正确的单词.
    """
)
print("如果不会请输入no")
iscontinue = "y"
while iscontinue == "y" or iscontinue == "":  #控制程序开始和停止
    word = random.choice(WORDS)    #随机选取一个单词
    correct = word
    jumble = ""
    while word:    #将单词字母打乱顺序，产生新的组合
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]  #通过切片乱序
    print("乱序后的单词:", jumble)
    guess = input("\n请你猜:")
    while guess != correct and guess != 'no':
        print("对不起,不正确.")
        guess = input("继续猜:")
    if guess == correct:
        print("真棒，你猜对了！")
        print(WORDS1[list(WORDS).index(correct)])
        iscontinue = input("\n按enter继续，输入N结束:")
    elif guess == "no":
        print(correct)
        print(WORDS1[list(WORDS).index(correct)])
        iscontinue = input("\n按enter继续，输入N结束:")
#cdata.columns[cdata.loc[1].isin([17592719302995])]