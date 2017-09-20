#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    :version: V1.1.1.17-9-8
    :author: Liuliping
    :file: manage.py
    :time: 17-9-8
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from data.exts import db
from data.models import User

manager = Manager(app)

# 模型->迁移文件->表
# 1.绑定app, db
migrate = Migrate(app, db)

# 2.把MigrateCommend命令添加到manger中
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
