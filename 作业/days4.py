name = ["张三", "李四", "王五"]

account = input("请输入用户名:")
password = input("请输入密码(三位数):")

while True:
    if account == "admin" and password == "123":
        print(f"恭喜{account}登陆成功!")
        break
    else:
        if account != "admin" and password == "123":
            print("用户名错误!")
        elif account == "admin" and password != "123":
            print("密码错误!")
        else:
            print("用户名和密码都错误!")
        account = input("请输入用户名:")
        password = input("请输入密码(三位数):")

name1 = input("请输入姓名:")

while True:
    if name1 in name:
        print(f"{name1}已经注册!")
    elif name1 == "赵鑫杰":
        print(f"{name1}注册成功!")
        break
    else:
        print(f"注册失败!")
    name1 = input("请输入姓名:")


