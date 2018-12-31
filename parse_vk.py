import requests
import time
import re
from pymongo import MongoClient
from vk_token import token

group = -55074079
url = 'https://api.vk.com/method/'
offset = 700
wrong_text = ['.com', '.ru', '.cc', 'club', '@', 'http', 'сохрани', 'подборк', 'в комментарии', 'cохраняйте']

def get_sources(url, token, offset):
    method = 'wall.get'
    payload = { 'owner_id': group, 'count': '100', 'offset': offset, 'v': '5.52', 'access_token': token}

    return requests.get(url + method, params=payload)

def check_text(text):
    for item in wrong_text:
        if text.find(item) != -1:
            return False
    return True


def add_posts_to_database():
    res = get_sources(url, token, offset).json()['response']['items']
    client = MongoClient()
    database = client.posts_database
    posts = database.posts
    post_id = 308
    watermark = 'vk.com/roditeli_m'

    for item in res:
        time.sleep(0.3)
        text = item['text']
        checked_text = check_text(text)
        try:
            image_link = item['attachments'][0]['photo']['photo_604']
        except KeyError:
            continue
        image_name = re.findall('\w+', image_link)[-2]

        if not text or not checked_text:
            continue

        post = {'text': text, 'image_link': image_link, 'post_id': str(post_id), 'watermark': watermark }
        posts.insert_one(post)
        print(post_id)
        post_id += 1

add_posts_to_database()