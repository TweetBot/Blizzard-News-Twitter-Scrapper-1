import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your Blizzard News Scrapper Bot is live & running..."

def run():
    # app.run(host="0.0.0.0", port=8080)
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)

def alive():
    server = Thread(target=run)
    server.start()
