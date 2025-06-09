import os
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

@app.route("/")
def home():
    send_alert("✅ KayzNFTs Sniper Bot is now connected and live on Render!")
    return "Bot is live!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
