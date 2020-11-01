#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: blog.py
@time: 2020/11/1 7:27
@desc:
'''


from flask import Blueprint

blog_bp=Blueprint('blog',__name__)

@blog_bp.before_request
def get_user():
    print("blog应用，验证用户")



@blog_bp.route("/index",methods=["GET"])
def index():
    return "blog的主页"