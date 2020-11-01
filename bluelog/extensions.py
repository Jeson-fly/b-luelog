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


db = SQLAlchemy()
mail = Mail()
bootstrap=Bootstrap()
moment = Moment()
ckeditor=CKEditor()