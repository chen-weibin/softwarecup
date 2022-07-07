# -*- codeing = utf-8 -*-
# @Time : 2022/5/10 20:30
# @File :constants.py.py
# @Software:PyCharm
HOSTNAME = '119.3.109.142'
PORT = '3306'
DATABASE = 'ruanjianbei'
USERNAME = 'root'
PASSWORD = '177018946931817614090[sb]'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
