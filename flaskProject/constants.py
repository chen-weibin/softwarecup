# -*- codeing = utf-8 -*-
# @Time : 2022/5/10 20:30
# @File :constants.py.py
# @Software:PyCharm
# 填写数据库相关信息
HOSTNAME = ''  # 填写服务器ip
PORT = ''
DATABASE = ''
USERNAME = ''
PASSWORD = ''
DB_URI = ''.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
