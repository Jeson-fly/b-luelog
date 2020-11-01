#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: auth.py
@time: 2020/11/1 7:27
@desc:
'''
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)


@auth_bp.before_request
def get_user():
    print("auth应用，验证用户")


@auth_bp.route("/index", methods=["GET"])
def index():
    return "auth的主页"