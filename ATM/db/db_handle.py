from conf import settings
import os
import json


def select(username):
    user_path = os.path.join(settings.USER_DATA_PATH, f'{username}.json')
    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_data = json.load(f)
        return user_data


def save(user_data):
    username = user_data.get('username')
    user_path = os.path.join(settings.USER_DATA_PATH, f'{username}.json')
    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False)







