import requests
import os

TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = '-100247365139'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
requests.post(url, data={'chat_id': CHAT_ID, 'text': '콜 보내야함'})
