# 1. 利用函数，实现对任意一份文件的复制
# 2. 利用函数和参数，实现对两个数字比较大小，返回更大的数字
# 3. 利用文件操作实现，将用户输入的账户和密码，以追加的方式保存成文件 db.txt
# 4. 利用文件操作，实现将用户输入的账户和密码，与db.txt文件里面的账户和密码进行
# 对比，如果账户和密码都对，则提示登录成功，如果用户输入的账户和密码和db.txt文件
# 的账户和密码都对比不上，则提示账户或密码错误
# TODO 输出有颜色的字
# print("\033[36;40m生鲜鱼白\033[0m")
"""
格式：print("\033[前景色;背景色m内容\033[0m") print("\033[31;40m两次输入的密码不一致\033[0m")

颜色      前景色      背景色

黑色      30          40
红色      31          41
绿色      32          42
黄色      33          43
蓝色      34          44
紫红色     35          45
青蓝色     36          46
白色      37          47
"""


def new():
    y = '1'
    while y == '1':
        account = input("请输入账号:").strip()
        passport = input("请输入密码:").strip()
        again = input("请再次输入密码:").strip()

        def passport1(a, b):
            with open('db.txt', 'a', encoding='utf-8') as f:
                f.write(a + " " + b + '\n')

        if passport == again:
            with open('db.txt', 'r', encoding='utf-8') as f1:
                content = f1.read()
            if account not in content:  # and passport not in content
                passport1(account, passport)
                print("注册成功！")
            else:
                print("已存在!")
            y = input("是否继续输入是（1）否（0）").strip()
        else:
            print("失败!\n请重新输入")


def check():
    account = input("请输入账号:").strip()
    passport = input("请输入密码:").strip()
    with open('db.txt', 'r', encoding='utf-8') as f:
        for i in f:
            if i.strip('\n') != "":
                a, b = i.strip('\n').split(" ")
                if account == a and passport == b:
                    print("登录成功!")
                    break
        else:
            print("错误!")
            return True


def change():
    bool1 = "True"
    while bool1 == "True":
        account = input("请输入账号:").strip()
        passport = input("请输入原密码:").strip()
        new_file = ''
        with open('db.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            f.seek(0)
            for i in f:
                if i.strip('\n') != "":
                    a, b = i.strip('\n').split(" ")
                    if account == a and passport == b:
                        c = input("请输入修改后的密码:")
                        b = b.replace(b, c)
                        new_file = new_file + (a + " " + b + '\n')
                        print("修改成功!")
                    elif account != a and account in content:
                        new_file += i
                    else:
                        print("账号错误!")
                        bool1 = "False"
        if new_file != '':
            with open('db.txt', 'w', encoding='utf-8') as f1:
                f1.write(new_file)
                f1.write("\n")
                break


def delete():
    bool1 = "True"
    while bool1 == "True":
        account = input("请输入账号:").strip()
        passport = input("请输入密码:").strip()
        new_file = ""
        with open('db.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            f.seek(0)
            for i in f:
                if i.strip('\n') != "":
                    a, b = i.strip('\n').split(" ")
                    if account == a and passport == b:
                        new_file += ""
                    elif account != a and account in content:
                        new_file += i
                    else:
                        print("错误!")
                        bool1 = "False"
        with open('db.txt', 'w', encoding='utf-8') as f1:
            f1.write(new_file)
            f1.write("\n")
            print("\033[31m注销成功!\033[0m")
            break


def inner(name):
    def outer(*args, **kwargs):
        if check():
            print("error!")
        else:
            res = name(*args, **kwargs)
            print("结束")
            return res

    return outer


@inner
def copy(name):  # 只能在当前文件夹
    a, b = name.split('.')
    if b is not None and b != 'jpg' and 'png':
        with open(name, 'rb') as f, open(f'{a}copy.mp4', 'wb') as f1:  # 对照片视频用二进制b
            content = f.read()
            f1.write(content)
        print("复制完成!")
    elif b == 'jpg' or 'png':
        with open(name, 'rb') as f, open(f'{a}copy.{b}', 'wb') as f1:  # 对照片视频用二进制b
            content = f.read()
            f1.write(content)
        print("复制完成!")
    else:
        print("输入错误!")


@inner
def copy_T(name):  # 只能在当前文件夹
    a, b = name.split('.')
    if b is not None:
        with open(name, 'r', encoding='utf-8') as f, open(f'{a}copy.{b}', 'w', encoding='utf-8') as f1:
            content = f.read()
            f1.write(content)
        print("复制完成!")
    else:
        print("输入错误!")


@inner
def mail():
    content = input("请输入邮件内容:")
    m = 0
    with open('邮件.txt', 'w', encoding='utf-8') as f:
        for i in content:
            m += 1
            if m == 66:
                m = 0
                f.write(i + '\n')
            else:
                f.write(i)
    print("写入完成")


# def compare(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
#
#
# a, b = input("请输入两个数字:").strip().split(" ")
# compare(a, b)


if __name__ == '__main__':
    hello = """
    |----------欢迎进入系统-------|
    |\033[31m请选择操作：\033[0m                 |
    |\033[32m1.注册账号\033[0m                  |
    |\033[33m2.登录账号\033[0m                  |
    |\033[34m3.修改密码\033[0m                  |
    |\033[35m4.注销账户\033[0m                  |
    |\033[36m5.退出系统\033[0m                  |
    |__________________________|
    """
    print(hello)
    x = '进入系统'
    while x == '进入系统':
        act = input("请输入选择的操作：").strip()
        if act == '注册账号':
            new()
        elif act == '登录账号':
            check()
        elif act == '修改密码':
            change()
        elif act == '注销账户':
            delete()
        else:
            print("退出成功!")
            break
    hello1 = """
    |----------欢迎使用----------|
    |\033[31m请选择操作：\033[0m                 |
    |\033[32m1.写邮件\033[0m                    |
    |\033[33m2.复制文件\033[0m                  |
    |__________________________|
    """
    print(hello1)
    act1 = input("请输入选择的操作：").strip()
    if act1 == '写邮件':
        mail()
    elif act1 == '复制文件':
        list1 = ['txt', 'py', 'md', 'srt', 'cpp', 'c', 'java', 'html', 'js', 'css']
        name = input("请输入文件名：").strip()
        a1 = name.split('.')[1]
        if a1 in list1:
            copy_T(name)
        else:
            copy(name)




