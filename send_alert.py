import requests
import os

TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = '-1002473651392'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
requests.post(url, data={'chat_id': CHAT_ID, 'text': '❗️콜,리스트 정리 해야합니다❗️'})
