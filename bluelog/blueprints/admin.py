#!/usr/bin/env python
# encoding: utf-8

'''
@adminor: lining
@file: admin.py
@time: 2020/11/1 7:27
@desc:
'''

from flask import Blueprint

admin_bp = Blueprint('admin', __name__)


@admin_bp.before_request
def get_user():
    print("admin应用，验证用户")
    return None

@admin_bp.route("/index", methods=["GET"])
def index():
    return "admin的主页"