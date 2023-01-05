#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/8/11 16:49
# @Author :wangqinghua
# @File : 闪马人车非大数据.py
# @Software : PyCharm



#提前登录一次再关闭页面操作

import requests

url='http://100.100.142.194/proxy/loki/login'

data={"username":"admin","password":"admin123"}

headers={"Referer":"http://100.100.142.194/login","user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"}
res=requests.post(url,json=data,headers=headers).json()['token']
# print(res)


head={"Referer":"http://100.100.142.194/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0","Origin":"http://100.100.142.194",
      "Authorization":f"Bearer {res}","Host":"100.100.142.194",
      "Content-Type":"application/json"}
seates_res='http://100.100.142.194/proxy/loki/api/face/captures'
datas={"Type":1,"Payload":{"GenderID":[],"NationID":[],"HatID":[],
                           "GlassID":[],"MaskID":[],"SensorID":[],
                           "Time":{"StartTimestamp":1653235200000,"EndTimestamp":1653321599000},
                           "Total":0,"OrderBy":"ts","Limit":100,"Offset":0,
                           "MaxPageCount":1000}}



ress=requests.post(url=seates_res,json=datas,headers=head)
import pprint
# pprint.pprint(ress.json())
face_id=(ress.json()['Rets'][0]['FaceReID'])
print(face_id)



headsss={"Referer":"http://100.100.142.194/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
         "Authorization":f"Bearer {res}","Host":"100.100.142.194",
         "Connection":"keep-alive","Pragma":"no-cache","Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"}
urlid=f'http://100.100.142.194/proxy/loki/api/face/capture/{face_id}'

datasss={"ts":1653299172923,"_":1660269069440}
url_id=requests.post(url=urlid,json=datasss,headers=headsss)
pprint.pprint(url_id.status_code)