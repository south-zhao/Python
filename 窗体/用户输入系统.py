import easygui as eg

filed = ["*用户名", "*真实姓名", "固定电话", "*年龄", "*手机号码", "QQ", "邮件", "*账号", "*密码"]
f = []

while True:
    errmsg = ""
    for i in range(len(filed)):
        option = filed[i].strip()
        if option[0] == "*":
            errmsg += ('【%s】为必填项\n\n' % filed[i])
    f = eg.multpasswordbox(errmsg, '账户中心', filed, f)#f = eg.multenterbox(errmsg, '账户中心', filed, f)
    for i in range(len(filed)):
        option = filed[i].strip()
        if option[0] == "*" and f[i].strip() == "":
            f = eg.multpasswordbox(errmsg, '账户中心', filed, f)#f = eg.multenterbox(errmsg, '账户中心', filed, f)
    break
print("用户资料", f)
