#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    :version: V1.1.1.17-9-8
    :author: Liuliping
    :file: exts.py
    :time: 17-9-8
"""
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
