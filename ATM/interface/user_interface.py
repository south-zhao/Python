from db import db_handle
from lib import common


def register_interface(username, password):

    data = db_handle.select(username)

    if data:
        return False, '用户存在'
    password = common.get_pwd_md5(password)
    user_data = {
        'username': username,
        'password': password,
        'balance': 10000000,
        # 流水   多条数据  列表
        'flow': [],
    }

    db_handle.save(user_data)
    return True, f'用户{username}注册成功'


def login_interface(username, password):

    data = db_handle.select(username)

    if data:
        password = common.get_pwd_md5(password)
        if password == data.get('password'):
            return True, f'{username}登陆成功'
        return False, f'{username}登陆失败'
    return False, f'{username}不存在'


def check_balance_interface(user):

    data = db_handle.select(user)

    if data:
        return True, data.get('balance')
    return False, 'error'


def withdraw_interface(username, money):

    data = db_handle.select(username)
    if data:
        balance = int(data.get('balance'))
        money = float(money * 1.05)
        if balance >= money:
            balance -= money
            data['balance'] = balance
            # 记录流水
            flow = f"{username}提现{money}, 可用{data['balance']}"
            data['flow'].append(flow)
            db_handle.save(data)
            return True, flow
        return False, 'error'
    return False, "错误"


def repay_interface(username, money):
    data = db_handle.select(username)
    if data:
        data['balance'] += int(money)
        flow = f"{username},充值{money}, 可用{data['balance']}"
        db_handle.save(data)
        return True, flow
    return False, "错误"


def transfer_interface(login_flag, money, to_user):
    to_user_data = db_handle.select(to_user)

    if to_user_data:
        data = db_handle.select(login_flag)
        if data:
            if data['balance'] >= int(money):
                data['balance'] -= int(money)
                flow = f"{to_user}转{money}, 余额{data['balance']}"
                data['flow'].append(flow)
                db_handle.save(data)
                to_user_data['balance'] += int(money)
                flow = f"{login_flag}  {money}   {data['balance']}"
                to_user_data['flow'].append(flow)
                db_handle.save(data)
                return True, '成功'
            return False, '不够'
        return False, 'error'
    return False, '不存在'


def check_flow_interface(login_flag):
    data = db_handle.select(login_flag)
    if data:
        if data.get('flow'):
            return True
        return
    return False, '错误'




