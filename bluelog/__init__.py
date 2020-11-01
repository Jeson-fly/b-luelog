#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: __init__.py
@time: 2020/10/31 20:33
@desc:
'''
import os

from flask import Flask



def creat_app():
    app = Flask(__name__)
    config_name=os.getenv(,"development")
    app.config.from_object()

    register_blueprint(app)

def register_blueprint(app):
    app.
