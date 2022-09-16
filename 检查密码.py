# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/9/16 19:24
# @Author : south(南风)
# @File : 检查密码.py
# Describe: 检查你的密码强度
# -*- coding: utf-8 -*-

import string


def check(pwd):
    if len(pwd) < 6 or len(pwd) > 12:
        return '你的密码不符合规范'

    d = {1: 'weak', 2: 'below middle', 3: 'above middle', 4: 'strong'}

    r = [False] * 4

    for i in pwd:
        if not r[0] and i in string.digits:
            r[0] = True
        elif not r[1] and i in string.ascii_lowercase:
            r[1] = True
        elif not r[2] and i in string.ascii_uppercase:
            r[2] = True
        elif not r[3] and i in ',.!;?<>':
            r[3] = True

    return d.get(r.count(True), 'error')


if __name__ == '__main__':
    password = input("请输入你的密码:")
    res = check(password)
    print(res)


