#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/12/6 11:01
# @Author   : wqh
# @Email    : 867075698@qq.com
# @File     : get_mp4.py
# @Software : PyCharm


# 获取qtp网页mp4视频
import requests


def test_login():
    header = {"Content-Type": "application/json", "User-Agent": "Chrome/103.0.0.0 Safari/537.36",
              "Referer": "http://10.19.0.6/"}
    login_url = 'http://10.19.0.6/api/users/login/'
    date = {"username": "admin", "password": "smai123"}
    data = requests.post(url=login_url, json=date, headers=header)
    return data.json()


token = test_login()['token']

headers = {"Accept": "application/json, text/plain, */*",
           "User-Agent": "Chrome/103.0.0.0 Safari/537.36",
           "Referer": "http://10.19.0.6/",
           "token": token,
           "Cookie": "token=" + token,
           "Host": "10.19.0.6"}


def get_list(page_url):
    response = requests.get(url=page_url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']


for a in range(1, 3):
    url = f'http://10.19.0.6/api/video/manage/all/algorithm/?name=&task_template=&monitor=&product=&point=&' \
          f'sample_type=0&event_name=44&event_code=&size=10&page={a}'
    data = get_list(url)

    for i in data:
        res = str(i['video_path'])
        names = (i['video_path'][-13:-4])
        video = requests.get(url=res, headers=headers).content
        with open(f"E:temp/mp4/{names}.mp4", "wb") as f:
            f.write(video)
