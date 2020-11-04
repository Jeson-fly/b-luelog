#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: extensions.py
@time: 2020/10/31 20:32
@desc:
'''

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_wtf import CSRFProtect


db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
ckeditor = CKEditor()
login_manager = LoginManager()
csrf = CSRFProtect()

@login_manager.user_loader
def load_user(user_id):
    from bluelog.models import Admin
    user = Admin.query.get(user_id)
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'warning'
login_manager.login_message = u"请先登录"
