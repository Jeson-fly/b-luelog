#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: blog.py
@time: 2020/11/1 7:27
@desc:
'''

from flask import Blueprint, render_template, request, current_app, abort, make_response

from bluelog.models import Post
from bluelog.utils import redirect_back

blog_bp = Blueprint('blog', __name__)


@blog_bp.before_request
def get_user():
    print("blog应用，验证用户")


@blog_bp.route('/')
def index():
    page = request.args.get("page",1,type=int)
    per_page=current_app.config["BLUELOG_POST_PER_PAGE"]
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page,per_page=per_page) #分页对象
    posts=pagination.items #当前页数的记录列表
    # posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("blog/index.html",**locals())


@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')


@blog_bp.route("/category/<int:category_id>")
def show_category(category_id):
    return render_template("blog/category.html")


@blog_bp.route("post/<int:post_id>")
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("blog/post.html",**locals())


@blog_bp.route("/change_theme/<theme_name>")
def change_theme(theme_name):
    if theme_name not in current_app.config["BLUELOG_THEMES"].keys():
        abort(404)
    response = make_response(redirect_back())
    response.set_cookie("theme",theme_name,max_age=30*24*60*60)
    return response