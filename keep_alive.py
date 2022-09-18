from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "The Bot Host is online!"

def run():
  app.run(host="0.0.0.0", port=1000)

def keep_alive():
  server = Thread(target=run)
  server.start()