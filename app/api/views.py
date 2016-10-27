# coding: utf-8

import os
import requests
from app import rds
from . import api
from flask import render_template
from flask import jsonify, request

MUMEIURL = os.getenv("MUMEIURL")

# test views
@api.route('/sid/')
def from_name_get_sid():
    sids = []; orgs = {}
    name = request.args.get("name") or "朱承浩"
    _sids = eval(rds.hget('info', name) or "[2014210761]")
    """
    {'sids': [{'deptName': '', 'orgName': '', 'sid':''}, ....]} 
    """
    for sid in _sids:
        r = requests.get(MUMEIURL.format(sid=sid))
        _json = r.json()  # dict
        for json in _json:
            value = json.get('orgName')
            if value not in orgs:
                orgs[value] = 1
            else:
                count = orgs.get(value)
                orgs[value] = count+1
        bestorg = sorted(orgs.iteritems(), key=lambda d:d[1], reverse=True)
        sid_dict = {
            'sid': sid,
            'deptName': _json[0].get('deptName'),
            'orgName': bestorg[0]
        }
        sids.append(sid_dict)
    return jsonify({'sids': sids})
