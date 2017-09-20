#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    :version: V1.1.1.17-9-8
    :author: Liuliping
    :file: views.py
    :time: 17-9-8
"""
from app import app
from flask import render_template, request, redirect, url_for, session, g
from data.models import User, Question, Answer
from data.exts import db
from app.decorators import login_required
from sqlalchemy import or_


@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by('-create_time').all()
    }
    return render_template('index.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            # session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'手机号码或者密码错误，请确认后再登录'


@app.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 手机号码验证，是否已注册
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u'该手机号码已经被注册,请更换手机号码'
        else:
            if password1 != password2:
                return u'两次密码不同，请核对'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        questions = Question(title=title, content=content)
        questions.author = g.user
        db.session.add(questions)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/search')
def search():
    q = request.args.get('q')
    questions = Question.query.filter(or_(Question.title.contains(q),
                                          Question.content.contains(q))).order_by('-create_time')
    return render_template('index.html', questions=questions)


@app.route('/detail/<question_id>')
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question_model)


@app.route('/add_answer/', methods=['POST'])
@login_required
def add_answer():
    content = request.form.get('answer_content')
    question_id = request.form.get('question_id')
    answer = Answer(content=content)
    answer.author = g.user
    questions = Question.query.filter(Question.id == question_id).first()
    answer.question = questions
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('login')


@app.context_processor
def my_context():
    if hasattr(g, 'user'):
        return {'user': g.user}
    return {}


# before_requset -> 视图函数 -> context_processor
@app.before_request
def my_defore():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user
