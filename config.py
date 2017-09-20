#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    :version: V1.1.1.17-9-8
    :author: Liuliping
    :file: config.py
    :time: 17-9-8
"""
import os

DEBUG = True
SECRET_KEY = os.urandom(24)

USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test_flask'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
