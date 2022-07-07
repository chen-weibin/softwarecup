import requests
from paddlers.deploy import Predictor
import cv2
import json
def inference(A,B,name):
    predictor = Predictor("static_models/inference_model",use_gpu=False)
    res = predictor.predict((A,B))
    # print(res)

    # label_map = []
    # for row in res['label_map']:
    #     label_map.append([])
    #     for col in row:
    #         label_map[-1].append(col)
    # # score_map = []
    # # for row in res['score_map']:
    # #     score_map.append([])
    # #     for col in row:
    # #         score_map[-1].append([round(col[0], 4), round(col[1], 4)])
    # newres = {
    #     'label_map': label_map,
    #     # 'score_map': score_map
    # }
    # with open('static/aa.json', "w", encoding="utf-8") as f:
    #     json.dump(newres, f, ensure_ascii=False, indent=4)
    # with open('static/aa.json', 'w+') as file:
    #     json.dump(res, file)
    cm_1024x1024 = res['label_map'] * 255
    cv2.imwrite(name, cm_1024x1024)

def target(A,name):
    predictor = Predictor("static_models/target",use_gpu=False)
    res = predictor.predict(A)
    cm_1024x1024 = res['label_map'] * 255
    cv2.imwrite(name, cm_1024x1024)

def diwuinfer(A,name):
    predictor = Predictor("static_models/inference_diwu",use_gpu=False)
    res = predictor.predict(A)
    cm_1024x1024 = res['label_map'] * 255
    cv2.imwrite(name, cm_1024x1024)

def ppyolo(A,path):
    predictor = Predictor("static_models/inference_jiance",use_gpu=False)
    res = predictor.predict(A)
    # print(res)
    li=[]
    for each in res:
        li.append(each["bbox"])
    a=cv2.imread(A)
    for i in range(0,1):
        cv2.rectangle(a, (int(li[i][0]), int(li[i][1])), (int(li[i][2]+li[i][0]), int(li[i][3]+li[i][1])), (0, 255, 0), 3)
    cv2.imwrite(path,a)

# inference("static/A.png","static/B.png","static/1234.png")
# print(diwuinfer("demo_data/img-3.png", "demo_data/diwu.png"))
# ppyolo("demo_data/playground_111.jpg", "demo_data/diwu.png")
