"""
题目
    提示用户输入账号和密码
    如果账户是老杨，密码是123，就输出 恭喜老杨登基成功
    或者账户是木易，密码是321，就输出 恭喜木易登基成功
    否则。输出总有刁民想害朕

    提示用户输入账号和密码，有输入的三次机会
    如果账户是老杨，密码是123，就输出 恭喜老杨登基成功，程序结束
    否则就输出账户或者密码错误，输出剩余的错误机会次数

    猜年龄游戏   假设年龄是88
    提醒用户输入年龄，如果猜对了，打印恭喜信息并退出
    如果猜错了，提示猜错了，最多尝试3次
"""

account = input("请输入用户名:")
password = input("请输入密码(三位数):")

while True:
    if account == "老杨" and password == "123":
        print(f"恭喜{account}登基成功!")
        break
    elif account == "木易" and password == "321":
        print(f"恭喜{account}登基成功!")
        break
    else:
        print("总有刁民想害朕")


account = input("请输入用户名:")
password = input("请输入密码(三位数):")
i = 1
while i <= 3:
    if account == "老杨" and password == "123":
        print(f"恭喜{account}登基成功!")
        break
    else:
        if account != "老杨" and password == "123":
            print("用户名错误!\n剩余%s次机会" % (3 - i))
            i += 1
        elif account == "老杨" and password != "123":
            print("密码错误!\n剩余%s次机会" % (3 - i))
            i += 1
        else:
            print("用户名和密码都错误!\n剩余%s次机会" % (3 - i))
            i += 1
        account = input("请输入用户名:")
        password = input("请输入密码(三位数):")


number = int(input("请输入数字(1-100):"))
i = 1
while i <= 3:
    if number == 88:
        print("恭喜猜对了!")
        break
    elif number > 88:
        print("太大了!\n剩余%s次机会" % (3 - i))
        i += 1
    else:
        print("太小了!\n剩余%s次机会" % (3 - i))
        i += 1
    number = int(input("请输入数字(1-100):"))

