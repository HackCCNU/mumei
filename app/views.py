# coding: utf-8
import os
from . import app, rds
from flask import render_template

urlprefix = os.getenv("MUMEIURLPRE")

@app.route('/')
def index():
    name_urls = {}
    # name_sids = rds.hgetall('info')
    names = rds.hkeys('info')
    for name in names:
        urls = []
        for sid in eval(rds.hget('info', name)):
            url = urlprefix.format(sid=sid)
            urls.append(url)
        name_urls[name] = urls
    return render_template('index.html', name_urls=name_urls)
