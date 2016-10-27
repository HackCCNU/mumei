# coding: utf-8

import os
import redis
from flask import Flask

rds = redis.StrictRedis(host=os.getenv('REDISHOST'), port=6389, db=0)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key is here'

from api import api
app.register_blueprint(api, url_prefix="/api")

from . import views
