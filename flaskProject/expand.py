
import requests
from paddlers.deploy import Predictor
import cv2
import numpy as np
import json
# 目标检查  2变化检测
def inference(A,B,resname):
    predictor = Predictor("static_models/inference_model",use_gpu=False)
    res = predictor.predict((A,B))
    pre = cv2.imread(A)
    newres = np.zeros((len(res["label_map"]), len(res["label_map"][0]), 3), dtype=np.uint8)
    mixres = np.zeros((len(res["label_map"]), len(res["label_map"][0]), 3), dtype=np.uint8)
    blank = np.zeros((len(res["label_map"]), len(res["label_map"][0])), dtype=np.uint8)
    for i in range(len(res["label_map"])):
        for j in range(len(res["label_map"][i])):
            if res['label_map'][i][j] == 0:
                newres[i][j] = [50, 40, 30]
                mixres[i][j] = pre[i][j]
                blank[i][j] = 0
            else:
                newres[i][j] = [233, 167, 97]
                mixres[i][j] = [255, 115, 0]
                blank[i][j] = 255
    cv2.imwrite(resname, newres)
    # cv2.imwrite(mixname, mixres)
    contours, hierarchy = cv2.findContours(blank, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours)

# 1目标提取
def target(A,resname,mixname):
    predictor = Predictor("static_models/target",use_gpu=False)
    res = predictor.predict(A)
    pre = cv2.imread(A)
    newres = np.zeros((len(res["label_map"]),len(res["label_map"][0]), 3), dtype=np.uint8)
    mixres = np.zeros((len(res["label_map"]),len(res["label_map"][0]), 3), dtype=np.uint8)
    temp= 0
    for i in range(len(res["label_map"])):
        for j in range(len(res["label_map"][i])):
            if res['label_map'][i][j] == 0:
                mixres[i][j] = pre[i][j]
                newres[i][j] = [50, 40, 30]  # [50, 40, 30] [124, 217, 32]
            else:
                temp += 1# [210, 210, 210]   [255, 127, 81]
                newres[i][j] = [233, 167, 97]   #  [50, 40, 30]  [255, 159, 56]215, 140, 59
                mixres[i][j] = [255, 115, 0]   #[255, 127, 81]
                # cm[i][j] = 255
    cv2.imwrite(resname, newres)
    cv2.imwrite(mixname, mixres)
    return temp
    # r1 = cv2.morphologyEx(cm, cv2.MORPH_CLOSE, k, iterations=5)
    # cv2.imwrite('static/1.png', r1)
    # mix = np.zeros((1024, 1024, 3), dtype=np.uint8)
    # for i in range(1024):
    #     for j in range(1024):
    #         if r1[i][j] == 0:
    #             mix[i][j] = pre[i][j]
    #         else:
    #             mix[i][j] = [255, 115, 0]
    # cv2.imwrite('static/11.png', mix)
    # k = np.ones((10, 10), np.uint8)
    # cm = np.zeros((1024, 1024), dtype=np.uint8)
    # for i in range(1024):
    #     for j in range(1024):
    #         if res['label_map'][i][j] == 0:
    #             cm[i][j] = 0
    #         else:
    #             cm[i][j] = 255

    # cv2.imshow('r1', r1)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    # cm_1024x1024 = res['label_map'] * 255
    # cv2.imwrite(name, cm_1024x1024)

# 4地物分类
def diwuinfer(A,name):
    predictor = Predictor("static_models/inference_diwu",use_gpu=False)
    res = predictor.predict(A)
    names=[0,0,0,0]
    newres = np.zeros((len(res["label_map"]), len(res["label_map"][0]), 3), dtype=np.uint8)
    for i in range(len(res["label_map"])):
        for j in range(len(res["label_map"][i])-1):
            index = res['label_map'][i][j]
            if index == 4:
                newres[i][j] = [0, 0, 0]
            elif index == 2:
                names[1]+=1
                newres[i][j] = [0, 222, 255]#黄色
            elif index == 1:
                names[0]+=1
                newres[i][j] = [255, 0, 60] #蓝色
            elif index == 3:
                names[2]+=1
                newres[i][j] = [142, 255, 30]#绿色
            else:
                names[3] += 1
                newres[i][j] = [0, 0, 255]  #红色
    cv2.imwrite("static/diwufenlei.png", newres)
    img = cv2.imread("static/diwufenlei.png")
    img1 = cv2.imread(A)
    a = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 0:
                a = 1
            else:
                img1[i][j][0] = img[i][j][0]
                img1[i][j][1] = img[i][j][1]
                img1[i][j][2] = img[i][j][2]
    # for i in range(0,4):
    #     names[i]=round(len(img)*len(img[1])/names[i],2)
    cv2.imwrite(name, img1)
    return names,len(img)*len(img[1])


# 3目标检测
def ppyolo_playground(A,path):
    predictor = Predictor("static_models/inference_jiance",use_gpu=False)
    res = predictor.predict(A)
    more = []
    for i in range(len(res)):
        if res[i]['score'] >= 0.500:
            more.append(res[i])
        else:
            break
    pre = cv2.imread(A)
    for rect in more:
        x1 = int(rect['bbox'][0])
        y1 = int(rect['bbox'][1])
        x2 = int(rect['bbox'][2]) + x1
        y2 = int(rect['bbox'][3]) + y1
        cv2.rectangle(pre, (x1, y1), (x2, y2), (255, 115, 0), 3)
    cv2.imwrite(path, pre)
    tabel = []
    for i in range(len(res)):
        item = {
            'id': i,
            'category': res[i]['category'],
            'score': res[i]['score']
        }
        tabel.append(item)
    return more,tabel
    # for i in range(0,1):(
    #     cv2.rectangle(a, (int(li[i][0]), int(li[i][1])), (int(li[i][2]+li[i][0]), int(li[i][3]+li[i][1])), (0, 255, 0), 3)
    # cv2.imwrite(path,a)
def ppyolo_overpass(A,path):
    predictor = Predictor("static_models/inference_jiance(2)",use_gpu=False)
    res = predictor.predict(A)
    more = []
    for i in range(len(res)):
        if res[i]['score'] >= 0.200:
            more.append(res[i])
        else:
            break
    pre = cv2.imread(A)
    for rect in more:
        x1 = int(rect['bbox'][0])
        y1 = int(rect['bbox'][1])
        x2 = int(rect['bbox'][2]) + x1
        y2 = int(rect['bbox'][3]) + y1
        cv2.rectangle(pre, (x1, y1), (x2, y2), (0, 115, 255), 3)
    cv2.imwrite(path, pre)
    tabel = []
    for i in range(len(res)):
        item = {
            'id': i,
            'category': res[i]['category'],
            'score': res[i]['score']
        }
        tabel.append(item)
    return more,tabel
    # for i in range(0,1):(
    #     cv2.rectangle(a, (int(li[i][0]), int(li[i][1])), (int(li[i][2]+li[i][0]), int(li[i][3]+li[i][1])), (0, 255, 0), 3)
    # cv2.imwrite(path,a)
def ppyolo_oiltank(A,path):
    predictor = Predictor("static_models/inference_jiance(3)",use_gpu=False)
    res = predictor.predict(A)
    more = []
    for i in range(len(res)):
        if res[i]['score'] >= 0.200:
            more.append(res[i])
        else:
            break
    pre = cv2.imread(A)
    for rect in more:
        x1 = int(rect['bbox'][0])
        y1 = int(rect['bbox'][1])
        x2 = int(rect['bbox'][2]) + x1
        y2 = int(rect['bbox'][3]) + y1
        cv2.rectangle(pre, (x1, y1), (x2, y2), (234, 255, 0), 3)
    cv2.imwrite(path, pre)
    tabel = []
    for i in range(len(res)):
        item = {
            'id': i,
            'category': res[i]['category'],
            'score': res[i]['score']
        }
        tabel.append(item)
    return more,tabel
    # for i in range(0,1):(
    #     cv2.rectangle(a, (int(li[i][0]), int(li[i][1])), (int(li[i][2]+li[i][0]), int(li[i][3]+li[i][1])), (0, 255, 0), 3)
    # cv2.imwrite(path,a)
def ppyolo_aircraft(A,path):
    predictor = Predictor("static_models/inference_jiance(4)",use_gpu=False)
    res = predictor.predict(A)
    more = []
    for i in range(len(res)):
        if res[i]['score'] >= 0.500:
            more.append(res[i])
        else:
            break
    pre = cv2.imread(A)
    for rect in more:
        x1 = int(rect['bbox'][0])
        y1 = int(rect['bbox'][1])
        x2 = int(rect['bbox'][2]) + x1
        y2 = int(rect['bbox'][3]) + y1
        cv2.rectangle(pre, (x1, y1), (x2, y2), (255,255, 255), 3)
    cv2.imwrite(path, pre)
    tabel = []
    for i in range(len(res)):
        item = {
            'id': i,
            'category': res[i]['category'],
            'score': res[i]['score']
        }
        tabel.append(item)
    return more,tabel
    # for i in range(0,1):(
    #     cv2.rectangle(a, (int(li[i][0]), int(li[i][1])), (int(li[i][2]+li[i][0]), int(li[i][3]+li[i][1])), (0, 255, 0), 3)
    # cv2.imwrite(path,a)


def bitexpand(path1,path2,path3,path4,path5):
    img = cv2.imread(path1)
    img1 = cv2.imread(path2)
    img2 = cv2.imread(path3)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img1 = cv2.drawContours(img1, contours, -1, (127,255,0), 2)  # img为三通道才能显示轮廓
    img2 = cv2.drawContours(img2, contours, -1, (127,255,0), 2)  # img为三通道才能显示轮廓
    cv2.imwrite(path4, img1)
    cv2.imwrite(path5, img2)

# print(inference("demo_data/val_27.png", "demo_data/valB_27.png", "demo_data/res_27.png", "demo_data/mixed_27.png"))
# print(target("demo_data/img-42.png", "demo_data/res.png", "demo_data/target_42.png"))
# print(diwuinfer("demo_data/3324.jpg", "demo_data/diwu_3324.png"))
# a,b=ppyolo_aircraft("demo_data/9845.jpg","demo_data/ppyolo.png")
# print(len(a)==0)
# print(b)
# # bitexpand("demo_data/res_22.png","demo_data/val_22.png", "demo_data/valB_22.png","demo_data/img_22kuang1.png","demo_data/img_22kuang2.png")
# ppyolo_aircraft("demo_data/aircraft_1045.jpg","demo_data/ppyolo-aircraft_1045.jpg")
# ppyolo_oiltank("demo_data/oiltank_415.jpg","demo_data/ppyolo-oiltank_415.jpg")
# print(ppyolo_playground("demo_data/playground_22.png", "demo_data/ppyolo-playground_22.png"))
# a,b=ppyolo_overpass("demo_data/overpass_370.jpg","demo_data/ppyolo-overpass_370.jpg")
# print(a)
# print(b)