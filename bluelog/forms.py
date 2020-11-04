#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: forms.py
@time: 2020/11/1 20:53
@desc: 表单
'''

from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms.validators import DataRequired, Length, ValidationError, Optional, URL, Email

from bluelog.models import Category
from flask_ckeditor import CKEditorField


# 登陆表单
class LoginForm(FlaskForm):
    username = wtf.StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = wtf.PasswordField('Password', validators=[DataRequired(), Length[8, 128]])
    remember = wtf.BooleanField('Remember me')
    submit = wtf.SubmitField('Login')


# 文章表单
class PostForm(FlaskForm):
    title = wtf.StringField("Title", validators=[DataRequired(), Length(1, 60)])
    category = wtf.SelectField("Category", coerce=int, default=1)
    body = CKEditorField("Body", validators=[DataRequired()])
    submit = wtf.SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name) for category in
                                 Category.query.order_by(Category.name).all]


#分类表单
class CategoryForm(FlaskForm):
    name = wtf.StringField('Name', validators=[DataRequired(), Length(1, 30)])
    submit = wtf.SubmitField()

    def validate_name(self, field):
        if Category.query.filter_by(name=field.data).first():
            raise ValidationError('Name already in use.')


#评论表单
class CommentForm(FlaskForm):
    author = wtf.StringField('Name', validators=[DataRequired(), Length(1, 30)])
    email = wtf.StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    site = wtf.StringField('Site', validators=[Optional(), URL(), Length(0, 255)])
    body = wtf.TextAreaField('Comment', validators=[DataRequired()])
    submit = wtf.SubmitField()


class AdminCommentForm(CommentForm):
    author = wtf.HiddenField()
    email = wtf.HiddenField()
    site = wtf.HiddenField()

#