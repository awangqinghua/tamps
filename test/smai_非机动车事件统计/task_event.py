#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/3/14 17:15
# @Author :wqh
# @File : Motor _vehicleViolation.py
# @Software : PyCharm


from smai_非机动车事件统计.get_variable import *
from smai_非机动车事件统计.do_excel import test_key


token = TestLogin().test_login()
# print(token)


class TestBus:

    def test_bus(self):

        for i in test_key():
            """
            预警列表过滤
            """
            request_url = f"{start_url()}:10280/v1/app/events"
            params = {"type": test_type(), "marking": "init", "taskId": i,
                      "page": 1, "size": 36, "tag1": "normal",
                      "eventTimeStart": test_start_time(), "eventTimeEnd": test_end_time(),
                      "authMenuCode": "svc", "authTaskType": test_type(), "authMarking": "init",
                      "__timestamp__": test_time()}
            headers = {"Content-Type": "application/json", "User-Agent": "Chrome/92.0.4515.107 Safari/537.36",
                       "SAAS-TOKEN": token,
                       "Referer": "http://47.97.184.108:10280/main/svc/events/fjdc/tag/normal/init"}

            res = requests.get(url=request_url, params=params, headers=headers, verify=False)
            if not res.json()['data']:
                print("否")
            else:
                print('是')


class TestBu:

    def test_bu(self):
        for i in test_key():
            # 过滤列表
            request_url = f"{start_url()}:10280/v1/app/events"
            params = {"type": test_type(), "marking": "filtered", "page": "1", "size": "36", "tag1": "normal",
                      "taskId": i, "eventTimeStart": test_start_time(), "eventTimeEnd": test_end_time(),
                      "authMenuCode": "svc", "authTaskType": test_type(), "authMarking": "filtered",
                      "__timestamp__": test_time()}
            headers = {"Content-Type": "application/json", "User-Agent": "Chrome/92.0.4515.107 Safari/537.36",
                       "SAAS-TOKEN": token}

            res = requests.get(url=request_url, params=params, headers=headers, verify=False)
            if not res.json()['data']:
                print("否")
            else:
                print('是')


# TestBus().test_bus()
TestBu().test_bu()
