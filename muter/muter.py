from flask import Flask
import requests

from .utils import make_celery

app = Flask(__name__)
app.config.from_object('muter.settings')

celery = make_celery(app)


@celery.task()
def ping():
    requests.post('http://requestb.in/16qybxr1')


@app.route('/do_it')
def do_it():
    ping.apply_async(countdown=20)
    return 'I will do something'
