#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: auth.py
@time: 2020/11/1 7:27
@desc:
'''
from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import current_user, login_user, login_required, logout_user

from bluelog.models import Admin
from bluelog.forms import LoginForm
from bluelog.utils import redirect_back

auth_bp = Blueprint('auth', __name__)


@auth_bp.before_request
def get_user():
    print("auth应用，验证用户")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("blog.index"))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            # 验证用户名和密码
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return redirect_back()
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('auth/login.html', form=form)


@auth_bp.route("/logout")
@login_required  # 用于视图保护，后面会详细介绍
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect_back()
