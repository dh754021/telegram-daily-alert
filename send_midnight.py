import requests
import os

TOKEN = os.environ['BOT_TOKEN_3']
CHAT_ID = '-1004357701385'
THREAD_ID = '2'

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "message_thread_id": THREAD_ID,
    "text": "🍀오늘 하루는 어땠나요?🍀"
})
print(response.text)
