from flask import Flask, render_template
from threading import Thread
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
@app.route('/')
def index():
    return "SpikeSpiegel"

def run():
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

def keep_alive():
    t = Thread(target=run)
    t.start() 
