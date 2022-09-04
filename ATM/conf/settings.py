#  配置信息
# 配置你的用户数据保存在哪里
# 配置信息，我们通常用纯大写保存
import os
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
# 定位到项目的最外面的项目
USER_DATA_PATH = os.path.join(BASE_PATH, 'db', 'user_data')

# 目录在不同的系统分隔符不同


SALT = '我是小赵'



