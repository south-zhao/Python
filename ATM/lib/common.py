# 存放通用的功能
import hashlib
from conf import settings
from core import src


def get_pwd_md5(password):
    # 对密码进行加密
    obj = hashlib.md5()
    salt = settings.SALT
    obj.update(salt.encode('utf-8'))
    obj.update(password.encode('utf-8'))
    return obj.hexdigest()


def login_auth(func):
    def inner(*args, **kwargs):
        if src.login_flag:
            res = func(*args, **kwargs)
            return res
        print('未登录')
        src.login()
    return inner



