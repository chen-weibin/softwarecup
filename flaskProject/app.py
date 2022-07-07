# -*- codeing = utf-8 -*-
# @Time : 2022/5/10 20:31
# @File :app.py.py
# @Software:PyCharm
import datetime
import json
import os
import random
import string
from datetime import date, timedelta
from flask import Flask, render_template, request,make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

import constants
import pymysql
from flask import Flask
from flask_cors import cross_origin
import infer
import expand
from flask_cors import *



pymysql.install_as_MySQLdb()

app = Flask(__name__,static_folder='/')
CORS(app,supports_credentials=True)
app.config.from_object(constants)
db=SQLAlchemy(app)

# temp={}
baseurl="static/"

class ChangeDetectionInput(db.Model):
    cd_id = db.Column(db.String(255), primary_key=True,nullable=False)
    id = db.Column(db.String(255),nullable=False)
    input_path = db.Column(db.String(255), nullable=False)

class ChangeDetectionResult(db.Model):
    id = db.Column(db.String(255), nullable=False)
    cd_id1= db.Column(db.String(50),  nullable=False)
    cd_id2 = db.Column(db.String(50), nullable=False)
    result_path = db.Column(db.String(255), nullable=False)
    result_kuang1= db.Column(db.String(255), nullable=False)
    result_kuang2 = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False,primary_key=True)


class User(db.Model):
    id = db.Column(db.String(255), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    mail=db.Column(db.String(255), nullable=False)
    account=db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

class TargetExtraction(db.Model):
    target_id = db.Column(db.String(255), primary_key=True, nullable=False)
    id = db.Column(db.String(255), nullable=False)
    input_path = db.Column(db.String(255), nullable=False)



class TargetExtractionResult(db.Model):
    target_id = db.Column(db.String(50), primary_key=True, nullable=False)
    id = db.Column(db.String(50), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=True)
    result_mix_path = db.Column(db.String(255), nullable=False)

class yoloinput(db.Model):
    jiance_id = db.Column(db.String(50), primary_key=True,nullable=False)
    id = db.Column(db.String(50),nullable=False)
    input_path = db.Column(db.String(255), nullable=False)

class yoloresult(db.Model):
    jiance_id = db.Column(db.String(50), primary_key=True,nullable=False)
    id = db.Column(db.String(50),nullable=False)
    path = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=True)

class classifiinput(db.Model):
    c_id = db.Column(db.String(50), primary_key=True,nullable=False)
    id = db.Column(db.String(50),nullable=False)
    input_path = db.Column(db.String(255), nullable=False)

class classifiresult(db.Model):
    c_id = db.Column(db.String(50), primary_key=True,nullable=False)
    id = db.Column(db.String(50),nullable=False)
    path = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=True)

class targetExtractionExample(db.Model):
    path1 = db.Column(db.String(255),primary_key=True, nullable=False)
    path2 = db.Column(db.String(255), nullable=False)

db.create_all()

# @app.route('/')
# def test():
#     return render_template('upload.html')
#
# # @app.route('/shuangchuan',methods=[ 'POST'])
# # @cross_origin(supports_credentials=True)
# # def files():
# #     file = request.files.get("file")
# #     pic = file.read()
# #     print(pic)
# #     ip=request.remote_addr
# #     if file is None:
# #         return {
# #             'message': "文件上传失败"
# #         }
# #     file_name = file.filename.replace(" ", "")
# #     img_path=os.path.join('static/' + file_name)
# #     with open(img_path,'wb+') as fp:
# #         fp.write(pic)
# #         fp.flush()
# #     data={"url":img_path," category":"ChangeDetection","http":str(ip)}
# #     return "1"
#
#
# # @app.route("/history/<string:ip>/")
# # def cd_his(ip):
# #     cd = ChangeDetection.query.filter(ChangeDetection.ip==ip).all()
# #     con=[]
# #     for each in cd:
# #       a= (each.__dict__)
# #       del a['_sa_instance_state']
# #       con.append(json.dumps(a))
# #
# #     return {"data":con}
# @app.route("/login")
# @cross_origin(supports_credentials=True)
# def login():
#     mail=request.args.get("mail")
#     username = request.args.get("username")
#     password = request.args.get("password")
#     mail = request.args.get("mail")
#     newinput =User(name=username,password=password,mail=mail)
#     db.session.add(newinput)
#     db.session.commit()
#
#
# @app.route("/resgiter")
# @cross_origin(supports_credentials=True)
# def resgiter():
#     mail=request.args.get("mail")
#     username = request.args.get("username")
#     password = request.args.get("password")
#     mail = request.args.get("mail")
#
#
#
#
#
#
#
#
# @app.route("/changedetection/before/<string:id>",methods=[ 'POST'])
# @cross_origin(supports_credentials=True)
# def cd_before(id):
#     file = request.files.get("file")
#     if file is None:
#         return {
#             'message': "文件上传失败"
#         }
#     pic = file.read()
#     # print(pic)
#     img_path=os.path.join(baseurl + id + '.png')
#     response = client.put_object(
#         Bucket='ruanjianbei-1307454689',
#         Body=pic,
#         Key=id+'.png',
#         StorageClass='STANDARD',
#         EnableMD5=False
#     )
#     newinput=ChangeDetectionInput(cd_id=id,id=1,input_path=img_path)
#     db.session.add(newinput)
#     db.session.commit()
#     temp.update({id:img_path})
#     return "1"
#
# @app.route("/changedetection/after/<string:id>",methods=[ 'POST'])
# @cross_origin(supports_credentials=True)
# def cd_after(id):
#     file = request.files.get("file")
#     if file is None:
#         return {
#             'message': "文件上传失败"
#         }
#     pic = file.read()
#     # print(pic)
#     img_path=os.path.join(baseurl + id + '.png')
#     response = client.put_object(
#         Bucket='ruanjianbei-1307454689',
#         Body=pic,
#         Key=id+'.png',
#         StorageClass='STANDARD',
#         EnableMD5=False
#     )
#     newinput=ChangeDetectionInput(cd_id=id,id=1,input_path=img_path)
#     db.session.add(newinput)
#     db.session.commit()
#     temp.update({id: img_path})
#     return "1"
#
# @app.route("/changedetection/detection/")
# @cross_origin(supports_credentials=True)
# def detection():
#     id1=request.args.get("id1")
#     id2 = request.args.get("id2")
#     result=ChangeDetectionInput.query.filter(or_(ChangeDetectionInput.cd_id==id1 , ChangeDetectionInput.cd_id==id2))
#     img_path=""
#     for each in result:
#         img_path=each.input_path
#     return {"path":img_path}
#
# @app.route("/home/history")
# @cross_origin(supports_credentials=True)
# def history():
#     return {"data":[{"id":"123","label":"123","time":"123","title":"123"}
#                     ,{"id":"1234","label":"1234","time":"1234","title":"1234"}]}
#
#
# @app.route("/home/graph")
# @cross_origin(supports_credentials=True)
# def graph():
#     return {"变化检测":[1,2,3,4,5,6,7],"地物分类":[1,2,3,4]}

@app.route("/login",methods=[ 'POST'])
@cross_origin(supports_credentials=True)
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    print(request.json)
    result = User.query.filter(User.name == username).filter(User.password == password)
    user_id = None
    for each in result:
        user_id = each.id

    if (user_id != None):
        return {"token":user_id}

    else:
        return {"token":-1}

@app.route("/registered",methods=[ 'POST'])
@cross_origin(supports_credentials=True)
def register():
    user = request.json.get("user")
    password = request.json.get("password")
    mail=request.json.get("email")
    account = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    newinput = User(name=account, password=password, mail=mail, date=start,account=user)
    db.session.add(newinput)
    db.session.commit()
    result1 = User.query.filter(User.name == user)
    current_id=None
    for each in result1:
        current_id=each.id
    return {"username":account,"token":current_id}
#
# @app.route("/changedetection/after",methods=[ 'POST'])
# @cross_origin(supports_credentials=True)
# def cd_after():
#     user_id=None
#     id=request.args.get("id")
#     user_id=request.cookies.get("xmut")
#     play_id=999999
#     if (user_id == None):
#         user_id=play_id
#     file = request.files.get("file")
#     if file is None:
#         return {
#             'message': "文件上传失败"
#         }
#     pic = file.read()
#     # print(pic)
#     img_path=os.path.join(baseurl + id + '.png')
#     with open(img_path, 'wb+') as fp:
#         fp.write(pic)
#         fp.flush()
#     newinput=ChangeDetectionInput(cd_id=int(id),id=user_id,input_path=img_path)
#     db.session.add(newinput)
#     db.session.commit()
#     return {"state":"1"}
#
# @app.route("/changedetection/before/<string:id>",methods=[ 'POST'])
# @cross_origin(supports_credentials=True)
# def cd_before(id):
#     user_id=None
#     user_id=request.cookies.get("xmut")
#     play_id=999999
#     if (user_id == None):
#         user_id=play_id
#     file = request.files.get("file")
#     if file is None:
#         return {
#             'message': "文件上传失败"
#         }
#     pic = file.read()
#     img_path=os.path.join(baseurl + id + '.png')
#     with open(img_path, 'wb+') as fp:
#         fp.write(pic)
#         fp.flush()
#     newinput=ChangeDetectionInput(cd_id=int(id),id=user_id,input_path=img_path)
#     db.session.add(newinput)
#     db.session.commit()
#     return {"state":1}

# @app.route("/changedetection/detection/")
# @cross_origin(supports_credentials=True)
# def detection1():
#     user_id = request.cookies.get("xmut")
#     play_id = 999999
#     if (user_id == None):
#         user_id = play_id
#     id1 = request.args.get("id1")
#     id2 = request.args.get("id2")
#     baseurl = "static/"
#     img1 = None
#     img2 = None
#     result1 = ChangeDetectionInput.query.filter(ChangeDetectionInput.cd_id == int(id1))
#     result2 = ChangeDetectionInput.query.filter(ChangeDetectionInput.cd_id == int(id2))
#     for each in result1:
#         img1 = each.input_path
#     for each in result2:
#         img2 = each.input_path
#     infer.inference(img1, img2, baseurl + str(id1) + str(id2) + '.png')
#     start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     newinput = ChangeDetectionResult(id=user_id, cd_id1=int(id1), cd_id2=int(id2),
#                                      result_path=baseurl + str(id1) + str(id2) + '.png', date=start)
#     db.session.add(newinput)
#     db.session.commit()
#     return {"resimg":"http://127.0.0.1:5000/"+baseurl + str(id1) + str(id2) + '.png'}
#
# @app.route("/targetextraction/img",methods=[ 'POST'])
# @cross_origin(supports_credentials=True)
# def TargetExtraction():
#     user_id=None
#     user_id=request.cookies.get("xmut")
#     id=request.args.get("id")
#     print(id)
#     print(type(id))
#     play_id=999999
#     if (user_id == None):
#         user_id=play_id
#     file = request.files.get("file")
#     if file is None:
#         return {
#             'message': "文件上传失败"
#         }
#     pic = file.read()
#     # print(pic)
#     img_path=os.path.join(baseurl + id + '.png')
#     with open(img_path, 'wb+') as fp:
#         fp.write(pic)
#         fp.flush()
#     newinput=TargetExtraction(target_id=str(id),id=user_id,input_path=img_path)
#     db.session.add(newinput)
#     db.session.commit()
#     infer.target(img_path, baseurl + id + 'target' + '.png')
#     start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     newinput = TargetExtractionResult(target_id=id, id=user_id, path=baseurl + str(id) + 'target' + '.png', date=start)
#     db.session.add(newinput)
#     db.session.commit()
#     return {"resimg":"http://127.0.0.1:5000/"+baseurl + id + 'target' + '.png'}

# @app.route("/TargetExtraction/Extraction/")
# @cross_origin(supports_credentials=True)
# def detection():
#     user_id = request.cookies.get("id")
#     play_id = 999999
#     if (user_id == None):
#         user_id = play_id
#     id = request.args.get("id")
#     baseurl = "static/"
#     img = None
#     result = TargetExtraction.query.filter(TargetExtraction.target_id == int(id))
#     for each in result:
#         img = each.input_path
#     infer.target(img, baseurl + id + 'target' + '.png')
#     start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     newinput = TargetExtractionResult(target_id=int(id), id=user_id, path=baseurl + str(id) + 'target' + '.png', date=start)
#     db.session.add(newinput)
#     db.session.commit()
#     return baseurl + id + 'target' + '.png'
# @app.route("/targetdetection/img",methods=[ 'POST'])
# @cross_origin(supports_credentials=True)
# def targetdetection():
#     user_id=None
#     user_id=request.cookies.get("xmut")
#     id=request.args.get("id")
#     play_id=999999
#     if (user_id == None):
#         user_id=play_id
#     file = request.files.get("file")
#     if file is None:
#         return {
#             'message': "文件上传失败"
#         }
#     pic = file.read()
#     # print(pic)
#     img_path=os.path.join(baseurl + id + '.png')
#     with open(img_path, 'wb+') as fp:
#         fp.write(pic)
#         fp.flush()
#     newinput=yoloinput(jiance_id=id,id=user_id,input_path=img_path)
#     db.session.add(newinput)
#     db.session.commit()
#     infer.ppyolo(img_path, baseurl + id + 'ppyolo' + '.png')
#     start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     newinput = yoloresult(jiance_id=id, id=user_id, path=baseurl + str(id) + 'ppyolo' + '.png', date=start)
#     db.session.add(newinput)
#     db.session.commit()
#     return {"resimg":"http://127.0.0.1:5000/"+baseurl + id + 'target' + '.png'}
#
# @app.route("/terrainclassification/<string:id>",methods=[ 'POST'])
# @cross_origin(supports_credentials=True)
# def diwudetection(id):
#     user_id=None
#     user_id=request.cookies.get("id")
#     play_id=999999
#     if (user_id == None):
#         user_id=play_id
#     file = request.files.get("file")
#     if file is None:
#         return {
#             'message': "文件上传失败"
#         }
#     pic = file.read()
#     # print(pic)
#     img_path=os.path.join(baseurl + id + '.png')
#     with open(img_path, 'wb+') as fp:
#         fp.write(pic)
#         fp.flush()
#     newinput=diwu(diwu_id=id,id=user_id,input_path=img_path)
#     db.session.add(newinput)
#     db.session.commit()
#     infer.diwuinfer(img_path, baseurl + id + 'diwu' + '.png')
#     start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     newinput = diwuResult(diwu_id=int(id), id=user_id, path=baseurl + str(id) + 'diwu' + '.png', date=start)
#     db.session.add(newinput)
#     db.session.commit()
#     return {"resimg":"http://127.0.0.1:5000/"+baseurl + id + 'diwu' + '.png'}

@app.route("/targetextraction/img",methods=[ 'POST'])
@cross_origin(supports_credentials=True)
def targetextraction():
    str123=""
    user_id=None
    user_id=request.args.get("token")
    id=request.args.get("id")
    play_id = 999999
    if (user_id == None):
        user_id=play_id
    file = request.files.get("file")
    baseurl = "static/"
    if file is None:
        return {
            'message': "文件上传失败"
        }
    pic = file.read()
    # print(pic)
    img_path=os.path.join(baseurl + id + '.png')
    with open(img_path, 'wb+') as fp:
        fp.write(pic)
        fp.flush()
    newinput=TargetExtraction(target_id=id,id=user_id,input_path=img_path)
    db.session.add(newinput)
    db.session.commit()
    nums=expand.target(img_path, baseurl + id + 'target' + '.png',baseurl + id + 'mix_target' + '.png')
    start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    newinput = TargetExtractionResult(target_id=id, id=user_id, path=baseurl + str(id) + 'target' + '.png', date=start, result_mix_path=baseurl + id + 'mix_target' + '.png')
    db.session.add(newinput)
    db.session.commit()
    if nums>1048576:
        str123+="道路占比遥感图的一半"
    else:
        str123 += "道路占比不到遥感图的一半"
    return {"resimg1":"http://127.0.0.1:5000/"+baseurl + id + 'target' + '.png',"resimg2":"http://127.0.0.1:5000/"+baseurl + id + 'mix_target' + '.png',"str":str123}

@app.route("/targetdetection/img",methods=[ 'POST'])
@cross_origin(supports_credentials=True)
def targetdetection():
    user_id=None
    user_id=request.args.get("token")
    id=request.args.get("id")
    play_id = 999999
    if (user_id == None):
        user_id=play_id
    file = request.files.get("file")
    baseurl = "static/"
    if file is None:
        return {
            'message': "文件上传失败"
        }
    pic = file.read()
    # print(pic)
    img_path=os.path.join(baseurl + id + '.png')
    with open(img_path, 'wb+') as fp:
        fp.write(pic)
        fp.flush()
    newinput=yoloinput(jiance_id=id,id=user_id,input_path=img_path)
    db.session.add(newinput)
    db.session.commit()
    resimg1=baseurl + id + 'jiance_playground' + '.png'
    ishaveplayground = False
    ishaveoiltank = False
    ishaveoverpass = False
    ishaveaircraft = False
    more,table=expand.ppyolo_playground(img_path, baseurl + id + 'jiance_playground' + '.png')
    ishaveplayground = True
    if(len(more)==0):
        ishaveplayground = False
        resimg1 = baseurl + id + 'jiance_overpass' + '.png'
        more, table = expand.ppyolo_overpass(img_path, baseurl + id + 'jiance_overpass' + '.png')
        ishaveoverpass = True
        if(len(more)==0):
            ishaveoverpass = False
            resimg1 = baseurl + id + 'jiance_oiltank' + '.png'
            more, table = expand.ppyolo_oiltank(img_path, baseurl + id + 'jiance_oiltank' + '.png')
            ishaveoiltank = True
            if(len(more)==0):
                ishaveoiltank = False
                resimg1 = baseurl + id + 'jiance_aircraft' + '.png'
                more, table = expand.ppyolo_aircraft(img_path, baseurl + id + 'jiance_aircraft' + '.png')
                ishaveaircraft=True
    if(len(more)==0):
        ishaveaircraft = False
    start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    newinput = yoloresult(jiance_id=id, id=user_id, path=resimg1, date=start)
    db.session.add(newinput)
    db.session.commit()
    return {"playground":{"ishave":ishaveplayground,"resimg":"http://127.0.0.1:5000/"+resimg1,"more":more,"table":table},
            "overpass":{"ishave":ishaveoverpass,"resimg":"http://127.0.0.1:5000/"+resimg1,"more":more,"table":table},
            "oiltank":{"ishave":ishaveoiltank,"resimg":"http://127.0.0.1:5000/"+resimg1,"more":more,"table":table},
            "aircraft":{"ishave":ishaveaircraft,"resimg":"http://127.0.0.1:5000/"+resimg1,"more":more,"table":table}}

@app.route("/terrainclassification/img",methods=[ 'POST'])
@cross_origin(supports_credentials=True)
def diwu():
    lindi=False
    gendi=False
    jianzhu=False
    qita=False
    user_id = None
    user_id = request.args.get("token")
    id = request.args.get("id")
    play_id = 999999
    if (user_id == None):
        user_id = play_id
    file = request.files.get("file")
    baseurl = "static/"
    if file is None:
        return {
            'message': "文件上传失败"
        }
    pic = file.read()
    # print(pic)
    img_path = os.path.join(baseurl + id + '.png')
    with open(img_path, 'wb+') as fp:
        fp.write(pic)
        fp.flush()
    newinput = classifiinput(c_id=id, id=user_id, input_path=img_path)
    db.session.add(newinput)
    db.session.commit()
    variety,pixels=expand.diwuinfer(img_path, baseurl + id + 'diwu' + '.png')
    start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    newinput = classifiresult(c_id=id, id=user_id, path=baseurl + id + 'diwu' + '.png', date=start)
    db.session.add(newinput)
    db.session.commit()
    print(pixels)
    if variety[0] >0:
        lindi=True
        variety[0]=round(variety[0]/pixels*100,4)

    if variety[1] >0:
        gendi=True
        variety[1] = round( variety[1]/pixels*100 ,4)

    if variety[2] >0:
        jianzhu=True
        variety[2] = round(variety[2]/pixels*100, 4)
        print(variety[2])

    if variety[3] >0:
        qita=True
        variety[3] = round( variety[3]/pixels*100, 4)

    return {"resimg": "http://127.0.0.1:5000/" + baseurl + str(id) + 'diwu' + '.png',"lingdi":{"ishave":lindi,"person":variety[0]},"gendi":{"ishave":gendi,"person":variety[1]},"jianzhu":{"ishave":jianzhu,"person":variety[2]},"qita":{"ishave":qita,"person":variety[3]}}

@app.route("/changedetection/before",methods=[ 'POST'])
@cross_origin(supports_credentials=True)
def before():
    user_id = None
    user_id = request.args.get("token")
    id = request.args.get("id")
    play_id = 999999
    if (user_id == None):
        user_id = play_id
    file = request.files.get("file")
    baseurl = "static/"
    if file is None:
        return {
            'message': "文件上传失败"
        }
    pic = file.read()
    # print(pic)
    img_path = os.path.join(baseurl + id + '.png')
    with open(img_path, 'wb+') as fp:
        fp.write(pic)
        fp.flush()
    newinput = ChangeDetectionInput(cd_id=id, id=user_id, input_path=img_path)
    db.session.add(newinput)
    db.session.commit()
    return {"state":1}

@app.route("/changedetection/after",methods=[ 'POST'])
@cross_origin(supports_credentials=True)
def after():
    user_id = None
    user_id = request.args.get("token")
    id = request.args.get("id")
    play_id = 999999
    if (user_id == None):
        user_id = play_id
    file = request.files.get("file")
    baseurl = "static/"
    if file is None:
        return {
            'message': "文件上传失败"
        }
    pic = file.read()
    # print(pic)
    img_path = os.path.join(baseurl + id + '.png')
    with open(img_path, 'wb+') as fp:
        fp.write(pic)
        fp.flush()
    newinput = ChangeDetectionInput(cd_id=id, id=user_id, input_path=img_path)
    db.session.add(newinput)
    db.session.commit()
    return {"state":1}


@app.route("/changedetection/detection")
@cross_origin(supports_credentials=True)
def detection():
    user_id = None
    user_id = request.args.get("token")
    before = request.args.get("before")
    after=request.args.get("after")
    play_id = str(999999)
    if (user_id == None):
        user_id = play_id
    resimg1=baseurl + before + after + '.png'
    reskuang1=baseurl + before + after+'kuang1' + '.png'
    reskuang2=baseurl + before + after+'kuang2' + '.png'
    before_path = db.session.query(ChangeDetectionInput.input_path).filter(ChangeDetectionInput.cd_id==before).all()[0].input_path
    after_path = db.session.query(ChangeDetectionInput.input_path).filter(ChangeDetectionInput.cd_id ==after).all()[0].input_path
    nums=expand.inference(before_path, after_path, resimg1)
    expand.bitexpand(resimg1,before_path,after_path,reskuang1,reskuang2)
    start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    newinput = ChangeDetectionResult(id=user_id, cd_id1=before, cd_id2=after,
                                     result_path=resimg1, date=start,result_kuang1=reskuang1,result_kuang2=reskuang2)
    db.session.add(newinput)
    db.session.commit()
    return {"resimg1":"http://127.0.0.1:5000/"+resimg1,"resimg2":"http://127.0.0.1:5000/"+reskuang1,"resimg3":"http://127.0.0.1:5000/"+reskuang2
            ,"nums":nums}

@app.route("/home/user")
@cross_origin(supports_credentials=True)
def user():
    id=request.args.get("token")
    a=db.session.query(func.count(ChangeDetectionResult.id).label("user_count")).filter(ChangeDetectionResult.id == id).all()[0].user_count
    a+=db.session.query(func.count(TargetExtractionResult.id).label("user_count")).filter(TargetExtractionResult.id == id).all()[0].user_count
    a+=db.session.query(func.count(yoloresult.id).label("user_count")).filter(yoloresult.id == id).all()[0].user_count
    a+=db.session.query(func.count(classifiresult.id).label("user_count")).filter(classifiresult.id == id).all()[0].user_count
    res = db.session.query(User.name, User.account, User.date).filter(User.id == id).all()[0]
    name=res[0]
    account=res[1]
    date=res[2]
    return {"user":name,"username":account,"jointime":date,"times":a}

@app.route("/targetextraction/example")
@cross_origin(supports_credentials=True)
def target_example():
    return {"data":[{"resimg1":"http://127.0.0.1:5000/demo_data/img-269.png","resimg2":"http://127.0.0.1:5000/demo_data/target_269.png"},
                    {"resimg1":"http://127.0.0.1:5000/demo_data/img-3.png","resimg2":"http://127.0.0.1:5000/demo_data/target_3.png"},
                    {"resimg1":"http://127.0.0.1:5000/demo_data/img-4.png","resimg2":"http://127.0.0.1:5000/demo_data/target_4.png"},
                    {"resimg1":"http://127.0.0.1:5000/demo_data/img-13.png","resimg2":"http://127.0.0.1:5000/demo_data/target_13.png"},
                    {"resimg1":"http://127.0.0.1:5000/demo_data/img-105.png","resimg2":"http://127.0.0.1:5000/demo_data/target_105.png"}]}


@app.route("/changedetection/example")
@cross_origin(supports_credentials=True)
def change_example():
    return {"data":[{"resimg1":"http://127.0.0.1:5000/demo_data/val_22.png","resimg2": "http://127.0.0.1:5000/demo_data/valB_22.png","resimg3":"http://127.0.0.1:5000/demo_data/res_22.png","resimg4":"http://127.0.0.1:5000/demo_data/img_22kuang1.png","resimg5":"http://127.0.0.1:5000/demo_data/img_22kuang2.png","nums":25},
                    {"resimg1":"http://127.0.0.1:5000/demo_data/val_21.png","resimg2": "http://127.0.0.1:5000/demo_data/valB_21.png","resimg3":"http://127.0.0.1:5000/demo_data/res_21.png","resimg4":"http://127.0.0.1:5000/demo_data/img_21kuang1.png","resimg5":"http://127.0.0.1:5000/demo_data/img_21kuang2.png","nums":80},
                    {"resimg1":"http://127.0.0.1:5000/demo_data/val_20.png","resimg2": "http://127.0.0.1:5000/demo_data/valB_20.png","resimg3":"http://127.0.0.1:5000/demo_data/res_20.png","resimg4":"http://127.0.0.1:5000/demo_data/img_20kuang1.png","resimg5":"http://127.0.0.1:5000/demo_data/img_20kuang2.png","nums":170},
                    {"resimg1":"http://127.0.0.1:5000/demo_data/val_27.png","resimg2": "http://127.0.0.1:5000/demo_data/valB_27.png","resimg3":"http://127.0.0.1:5000/demo_data/res_27.png","resimg4":"http://127.0.0.1:5000/demo_data/img_27kuang1.png","resimg5":"http://127.0.0.1:5000/demo_data/img_27kuang2.png","nums":126},
                    {"resimg1":"http://127.0.0.1:5000/demo_data/val_28.png","resimg2": "http://127.0.0.1:5000/demo_data/valB_28.png","resimg3":"http://127.0.0.1:5000/demo_data/res_28.png","resimg4":"http://127.0.0.1:5000/demo_data/img_28kuang1.png","resimg5":"http://127.0.0.1:5000/demo_data/img_28kuang2.png","nums":77}]}

@app.route("/home/graph")
@cross_origin(supports_credentials=True)
def graph():
    id = request.args.get("token")
    xaxis = []
    yaxisChange = []
    yaxisClassification = []
    yaxisdiwu = []
    yaxisppyolo = []
    for i in range(0, 15):
        today = (date.today() + timedelta(days=int(-i))).strftime("%Y-%m-%d")
        yesterday = (date.today() + timedelta(days=int(-i) + 1)).strftime("%Y-%m-%d")
        a = db.session.query(func.count(ChangeDetectionResult.id).label("user_count")).filter(
            ChangeDetectionResult.date >= today).filter(ChangeDetectionResult.date <= yesterday).filter(
            ChangeDetectionResult.id == id).all()[0].user_count
        b = db.session.query(func.count(classifiresult.id).label("user_count")).filter(
            classifiresult.date >= today).filter(classifiresult.date <= yesterday).filter(
            classifiresult.id == id).all()[0].user_count
        c = db.session.query(func.count(yoloresult.id).label("user_count")).filter(yoloresult.date >= today).filter(
            yoloresult.date <= yesterday). \
            filter(yoloresult.id == id).all()[0].user_count
        d = db.session.query(func.count(TargetExtractionResult.id).label("user_count")).filter(TargetExtractionResult.date >= today).filter(
            TargetExtractionResult.date <= yesterday). \
            filter(TargetExtractionResult.id == id).all()[0].user_count
        xaxis.append(today)
        yaxisClassification.append(b)
        yaxisChange.append(a)
        yaxisdiwu.append(d)
        yaxisppyolo.append(c)
    return {
        "xaxis":xaxis,
        "yaxisChange": yaxisChange,
        "yaxisClassification": yaxisClassification,
        "yaxisdiwu":yaxisdiwu,
        "yaxisppyolo":yaxisppyolo
    }
@app.route("/home/history")
@cross_origin(supports_credentials=True)
def history():
    id = request.args.get("token")
    li = []
    a = db.session.query(ChangeDetectionResult.result_path, ChangeDetectionResult.result_kuang1,
                         ChangeDetectionResult.date).filter(ChangeDetectionResult.id == id).all()
    b = db.session.query(yoloresult.path, yoloresult.date).filter(yoloresult.id == id).all()
    c = db.session.query(classifiresult.path, classifiresult.date).filter(yoloresult.id == id).all()
    d = db.session.query(TargetExtractionResult.path, TargetExtractionResult.result_mix_path,
                         TargetExtractionResult.date).filter(TargetExtractionResult.id == id).all()
    for i in range(0, len(a)):
        dic = {}
        dic.update({"label": '变化检测', "labelColor": 'change-detection', "resimg1": a[i][0], "resimg2": a[i][1],
                    "time": a[i][2]})
        li.append(dic)

    for i in range(0, len(b)):
        dic = {}
        dic.update({"label": '目标检测',
                    "labelColor": 'target-detection', "resimg": b[i][0], "time": b[i][1]})
        li.append(dic)

    for i in range(0, len(c)):
        dic = {}
        dic.update({"label": '地物分类',
                    "labelColor": 'terrain-classification', "resimg": c[i][0], "time": c[i][1]})
        li.append(dic)

    for i in range(0, len(d)):
        dic = {}
        dic.update({"label": '目标提取',
                    "labelColor": 'target-extraction', "resimg1": d[i][0], "resimg2": d[i][1], "time": d[i][2]})
        li.append(dic)
    return {"data":li}

@app.route("/targetdetection/example")
@cross_origin(supports_credentials=True)
def targetdetectionexample():
    return {"data":
                [{"playground":{"ishave":True,"resimg1":"http://127.0.0.1:5000/demo_data/playground_22.png","resimg2":"http://127.0.0.1:5000/demo_data/ppyolo-playground_22.png"},
                 "overpass":{"ishave":False},"oiltank":{"ishave":False},"aircraft":{"ishave":False}},
            {"playground":{"ishave":False},
             "overpass":{"ishave":True,"resimg1":"http://127.0.0.1:5000/demo_data/overpass_370.jpg","resimg2":"http://127.0.0.1:5000/demo_data/ppyolo-overpass_370.jpg"},"oiltank":{"ishave":False},"aircraft":{"ishave":False}},
                 {"playground": {"ishave": False},
                  "overpass": {"ishave": False},
                  "oiltank": {"ishave": True,"resimg1": "http://127.0.0.1:5000/demo_data/oiltank_415.jpg",
                               "resimg2": "http://127.0.0.1:5000/demo_data/ppyolo-oiltank_415.jpg"}, "aircraft": {"ishave": False}},
                 {"playground": {"ishave": False},
                  "overpass": {"ishave": False},
                  "oiltank": {"ishave": False},
                  "aircraft": {"ishave": True,"resimg1": "http://127.0.0.1:5000/demo_data/aircraft_1045.jpg",
                              "resimg2": "http://127.0.0.1:5000/demo_data/ppyolo-aircraft_1045.jpg"}},
                 {"playground": {"ishave": False},
                  "overpass": {"ishave": False},
                  "oiltank": {"ishave": False},
                  "aircraft": {"ishave": True, "resimg1": "http://127.0.0.1:5000/demo_data/aircraft_1095.jpg",
                               "resimg2": "http://127.0.0.1:5000/demo_data/ppyolo-aircraft_1095.jpg"}}
                 ]
            }

@app.route("/terrainclassification/example")
@cross_origin(supports_credentials=True)
def diwuexample():
    return {
        "data": [
            {
                "resimg1": "http://localhost:5000/demo_data/9879.jpg",
                "resimg2": "http://localhost:5000/demo_data/diwu_9879.png",
                "lingdi": {"ishave": False, "person": 0},
                "gendi": {"ishave": False, "person": 0},
                "jianzhu": {"ishave": False, "person": 0},
                "qita": {"ishave": True, "person": 2.60},
            },
            {
                "resimg1": "http://localhost:5000/demo_data/9908.jpg",
                "resimg2": "http://localhost:5000/demo_data/diwu_9908.png",
                "lingdi": {"ishave": True, "person": 0.79},
                "gendi": {"ishave": False, "person": 0},
                "jianzhu": {"ishave": True, "person": 0.02},
                "qita": {"ishave": False, "person": 0},
            },
            {
                "resimg1": "http://localhost:5000/demo_data/9927.jpg",
                "resimg2": "http://localhost:5000/demo_data/diwu_9927.png",
                "lingdi": {"ishave": True, "person": 0.21},
                "gendi": {"ishave": False, "person": 0},
                "jianzhu": {"ishave":False, "person": 0},
                "qita": {"ishave": False, "person": 0},
            },
            {
                "resimg1": "http://localhost:5000/demo_data/9953.jpg",
                "resimg2": "http://localhost:5000/demo_data/diwu_9953.png",
                "lingdi": {"ishave": True, "person": 56.37},
                "gendi": {"ishave": False, "person": 0},
                "jianzhu": {"ishave": False, "person": 0},
                "qita": {"ishave": True, "person": 19.21},
            },
            {
                "resimg1": "http://localhost:5000/demo_data/9975.jpg",
                "resimg2": "http://localhost:5000/demo_data/diwu_9975.png",
                "lingdi": {"ishave": False, "person": 0},
                "gendi": {"ishave": False, "person": 0},
                "jianzhu": {"ishave": True, "person": 0.323},
                "qita": {"ishave": False, "person": 0},
            }
        ]
    }

if __name__ == '__main__':
    app.run()




# {"data":[{"resimg1":"http://127.0.0.1:5000/demo_data/img-269.png","resimg2":"http://127.0.0.1:5000/demo_data/target_269.png"}
# 'data1': []}
# {
#     'play': {
#         'live': True,
#         'data': {
#             'resimg': 'dfldkfl',
#             'more': ldfkldkf
#         }
#     },
#     'youguan': {
#         live: False
#     },
#     'ss': {},
#     'se': {}
# }