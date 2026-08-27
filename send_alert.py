import requests
import os

TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = '-5137059226'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
requests.post(url, data={'chat_id': CHAT_ID, 'text': '콜 보내야함'})
