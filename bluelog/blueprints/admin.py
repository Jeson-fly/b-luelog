#!/usr/bin/env python
# encoding: utf-8

'''
@adminor: lining
@file: admin.py
@time: 2020/11/1 7:27
@desc:
'''

from flask import Blueprint
from flask_login import login_required

admin_bp = Blueprint('admin', __name__)


@admin_bp.before_request
@login_required
def login_protect():
    pass

@admin_bp.route("/index", methods=["GET"])
def index():
    return "admin的主页"