import os
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive"

print("Bot started...")

while True:
    time.sleep(60)
