from interface import user_interface
from lib import common


# 注册功能
def register():  # 视图层
    # 1. 接受输入
    # 2.基本的判断
    # 3. 对输入处理
    # 4. 结果给用户
    while True:
        # 1.接受用户的信息
        username = input('请输入你的账号:').strip()
        password = input('请输入你的密码:').strip()
        re_password = input('请再次输入你的密码:').strip()
        if password == re_password:
            #  如果一致 就可以注册
            # 成功了没有  提示信息
            # user_path = os.path.join(settings.USER_DATA_PATH, f'{username}.json')
            # if os.path.exists(user_path):
            #     print("已经有了")
            #     continue
            # # 意味着没有注册，现在可以开始注册
            # # 文件里面要保存什么数据
            # password = common.get_pwd_md5(password)
            # data = {
            #     'username': username,
            #     'password': password,
            #     'balance': 10000000,
            #     # 流水   多条数据  列表
            #     'flow': [],
            # }
            # # 保存这份文件
            # with open(user_path, 'w', encoding='utf-8') as f:
            #     json.dump(data, f, ensure_ascii=False)
            # print(f'用户{username}注册成功!')
            # break
            # # return   # 后面的代码没必要执行了
            flag, msg = user_interface.register_interface(username, password)
            if flag:
                print(msg)
                break
            print(msg)
            continue
        print('不同')

        # if len(password) < 8:
        #     print('账户不能少于8位')


login_flag = False


# 登录功能
def login():
    global login_flag
    while True:
        username = input('请输入你的账号:').strip()
        password = input('请输入你的密码:').strip()
        flag, msg = user_interface.login_interface(username, password)
        if flag:
            print(msg)
            login_flag = username
            break
        print(msg)


# 查看余额
@common.login_auth
def check_balance():
    global login_flag
    flag, msg = user_interface.check_balance_interface(login_flag)
    if flag:
        print(f'{login_flag}  {msg}')
    else:
        print(msg)


# 提现功能
@common.login_auth
def withdraw():
    while True:
        money = input("金额").strip()
        if not money.isdigit():
            print("重新输入")
            continue
        flag, msg = user_interface.withdraw_interface(login_flag)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 还款功能
@common.login_auth
def repay():
    while True:
        money = input("金额").strip()
        if not money.isdigit():
            print("重新输入")
            continue
        flag, msg = user_interface.repay_interface(login_flag)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 转账功能
@common.login_auth
def transfer():
    global login_flag
    while True:
        to_user = input('请输入你的账号:').strip()
        money = input("金额").strip()
        if not money.isdigit():
            print("重新输入")
            continue
        if to_user == login_flag:
            print()
            continue
        flag, msg = user_interface.transfer_interface(login_flag, money, to_user)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 查看流水
@common.login_auth
def check_flow():
    flag, msg = user_interface.check_flow_interface(login_flag)
    if flag:
        for x in msg:
            print(x)
    else:
        print(msg)


# 退出
def out():
    print("""退出系统
    欢迎下次登录
    """)


func_dic = {
    '1': register,  # 内存地址
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': out,
}


# 只要自己不尴尬，尴尬的就是别人
# 反正都认识我，怕什么
# 主要的函数，核心逻辑从这里开始  英语的口语
def run():
    # ATM机   执行了一个功能  就结束了吗？  继续可以触发功能  死循环
    print('''
            +++++++ATM+++++++++
            1. 注册功能
            2. 登录功能
            3. 查看余额
            4. 提现功能
            5. 还款功能
            6. 转账功能
            7. 查看流水
            8. 退出系统
            +++++++++++++++++++
            ''')
    while True:  # 死循环
        # 1. 给用户提示有这么多功能可以选择

        # 2. 接受用户的输入，去触发对应的功能
        choice = input('请输入功能的编号:').strip()
        # 接下来要做的是？  根据用户输入的功能编号触发对应的功能？
        #    一个功能就是一个函数  OK吗 ？ 更好的方式
        # 执行函数的本质  是什么   函数的内存地址()
        # 函数的内存地址  [register,login]
        # 先判断，用户输入的是不是字典中的那个功能，如果不是，就不继续了
        # 如果是，就触发功能

        # func_dic.get(choice)()  # 有可能发生什么现像  报错
        if choice not in func_dic:  # 执行了吧
            print('请输入正确的功能编号')
            continue
        # 触发对应的功能
        if choice == '8':
            return
        else:
            func_dic.get(choice)()  # 意味着肯定能执行

# 333   对于基础知识点的灵活运用
# ATM 项目中  升华
