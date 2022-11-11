# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/9/16 21:58
# @Author : south(南风)
# @File : name.py
# Describe: 自动生成大量随机信息
# -*- coding: utf-8 -*-
from random import choice, randint
from pypinyin import lazy_pinyin, pinyin
import jieba
import string
import codecs

StringBase = '\u7684\u4e00\u4e86\u662f\u6211\u4e0d\u5728\u4eba'


def get_email():
    suffix = ['.com', '.org', '.net', '.cn']
    characters = string.ascii_letters + string.digits + '_'
    username = ''.join((choice(characters) for i in range(randint(6, 12))))
    domain = ''.join((choice(characters) for i in range(randint(3, 6))))
    return username + '@' + domain + choice(suffix)


def get_tel():
    return ''.join((str(randint(0, 9)) for i in range(11)))


def get_name_addr(flag):
    """
    :return:flag=1返回姓名 flag=0返回地址
    """
    if flag == 1:
        range_start, range_end = 2, 5
    elif flag == 0:
        range_start, range_end = 10, 30
    result = ''.join((choice(StringBase) for i in range(randint(range_start, range_end))))
    return result


def get_sex():
    return choice(('男', '女'))


def get_age():
    return str(randint(18, 100))


def main(filename):
    with codecs.open(filename, 'w', encoding="utf-8") as f:
        f.write("Name   Sex   Age   TelNo   Address   Email\n")

        for i in range(200):
            name = get_name_addr(1)
            sex = get_sex()
            age = get_age()
            tel = get_tel()
            address = get_name_addr(0)
            email = get_email()
            line = '   '.join([name, sex, age, tel, address, email]) + '\n'
            f.write(line)


def output(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.split('   ')
            for i in line:
                print(i, end="   ")
            print()


# if __name__ == '__main__':
#     filename = 'information.txt'
#     main(filename)
#     output(filename)


# x = '分词的准确度直接影响了后续文本处理和挖掘算法的最终效果'
# res = jieba.lcut(x)
# print(res)

# res1 = lazy_pinyin('赵鑫杰')
res1 = lazy_pinyin('赵鑫杰', 1)
print(res1)


