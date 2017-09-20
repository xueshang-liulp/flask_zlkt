#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    :version: V1.1.1.17-9-8
    :author: Liuliping
    :file: __init__.py
    :time: 17-9-8
"""
from flask import Flask
import config


app = Flask(__name__)
app.config.from_object(config)

from app import views

