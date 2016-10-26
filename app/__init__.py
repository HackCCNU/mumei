# coding: utf-8

import redis
from flask import Flask

rds = redis.StrictRedis(host="redis", port=6389, db=0)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key is here'


from . import views, forms
