import os
import time

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BALE_TOKEN = os.getenv("BALE_TOKEN")
TG_CHANNEL = os.getenv("TG_CHANNEL")
BALE_CHANNEL = os.getenv("BALE_CHANNEL")

print("Sync Bot Started...")

last_sent = set()

def send_to_telegram(text):
    import requests
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TG_CHANNEL, "text": text})

def send_to_bale(text):
    import requests
    url = f"https://tapi.bale.ai/bot{BALE_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": BALE_CHANNEL, "text": text})

def fetch_fake_bale_posts():
    """
    فعلاً شبیه‌سازی می‌کنیم چون API عمومی بله محدود است
    بعداً واقعی‌اش می‌کنیم
    """
    return []

while True:
    posts = fetch_fake_bale_posts()

    for post in posts:
        if post not in last_sent:
            send_to_telegram(post)
            last_sent.add(post)

    time.sleep(10)
