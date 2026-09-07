import requests
import os

alerts = [
    {
        "token": os.environ['BOT_TOKEN'],
        "chat_id": "-1002473651392",
        "text": "❗️콜,리스트 정리 해야합니다❗️"
    },
    {
        "token": os.environ['BOT_TOKEN_2'],
        "chat_id": "-1002964487598",
        "text": "❗️콜,리스트 정리 해야합니다❗️"
    },
]

for a in alerts:
    url = f"https://api.telegram.org/bot{a['token']}/sendMessage"
    requests.post(url, data={"chat_id": a["chat_id"], "text": a["text"]})
