# coding: utf-8
from . import api, rds
from flask import render_template
from flask import jsonify, request


# test views
@api.route('/sid/')
def from_name_get_sid():
    name = request.args.get("name")
    sids = eval(rds.hget('info', name))
    return jsonify(sids)
