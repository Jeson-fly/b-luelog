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
from bluelog.blueprints.admin import admin_bp
from bluelog.blueprints.auth import auth_bp
from bluelog.blueprints.blog import blog_bp
from bluelog.settings import config
from bluelog.extensions import db, mail, moment, bootstrap, ckeditor


def create_app():
    app = Flask("bluelog")
    config_name = os.getenv('FLASK_CONFIG', "development")
    app.config.from_object(config[config_name])

    register_blueprints(app)  # 注册蓝图
    register_errors(app)  # 注册错误模板
    register_extensions(app)  # 注册扩展程序
    register_commands(app)  # 注册shell命令
    register_shell_context(app)  # 注册shell上下文处理函数
    register_tempalte_context(app)  # 注册模板上下文处理函数


    return app

# 注册shell命令
def register_commands(app):
    pass


# 注册shell上下文处理函数
def register_shell_context(app):
    pass


# 注册模板上下文处理函数
def register_tempalte_context(app):
    pass


# 注册扩展程序
def register_extensions(app):
    db.init_app(app)
    moment.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    ckeditor.init_app(app)


# 注册蓝图函数
def register_blueprints(app):
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp, url_prefix='/blog')


# 注册错误模板函数
def register_errors(app):
    pass
