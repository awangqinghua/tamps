#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/3/14 17:15
# @Author :wangqinghua
# @File : Motor _vehicleViolation.py
# @Software : PyCharm


import requests
import pprint
import re
# from smai_交通事件统计_接口.do_excel import test_key
from smai_交通事件统计_接口.get_data import GetDate
# from smai_交通事件统计_接口.do_excel import DeExcel


# 先获取execution的value
def execution():
    url = 'http://10.5.1.156:10107/cas/login?service=http://10.5.1.161:10280/?appCode=console'
    res = requests.get(url).text
    pattre = '<input.*?execution.*?value="(.*?)"'
    res = re.search(pattre, res, re.S)
    if res:
        executions = res.group(1)
    return executions
execut =execution()


class TestLogin:

    def login_token(self):
        login_url = 'http://10.5.1.156:10107/cas/v1/tickets'
        params = {'username': 'admin', 'password': 'smai123', 'appCode': 'console', 'service': 'http://10.5.1.156:10280/?appCode=console',
                  "execution": execut,"_eventId":"submit"}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = requests.post(url=login_url, data=params, headers=headers, verify=False)
        login_urls = 'http://10.5.1.156:10280/v1/app/login?ticket=%s&service=http://10.5.1.156:10280/?appCode=console&__timestamp__=1647334702837' % (data.json()['data'])
        res = requests.get(login_urls)
        if res.json()['data']['token']:
            setattr(GetDate, "COOKIES", res.json()['data']['token'])
        else:
            print("获取token失败")

        return res.json()['data']['token']


cookies = TestLogin().login_token()
print(cookies)


# 获取数据
# test_data = test_key()
# print(test_data)


# 查询是否有异常停车
# class TestBus:
#
#     def error_bus(self):
#          for i in test_data:
#              # 交通事件-预警列表过滤
#             request_url = "http://10.5.1.156:10280/v1/app/events"
#             params = {"type": "jtsj", "marking": "init", "eventTypeList":2455,"page": 1, "taskId": i, "size": "60", "eventTimeStart": "2022-03-29 20:00:00",
#                       "eventTimeEnd": "2022-03-30 23:59:00", "authMenuCode": "svc", "authTaskType": "jtsj", "authMarking": "init",
#                       "__timestamp__": "1648616106263"}
#             headers = {"Content-Type": "application/json",
#                        "User-Agent": "Chrome/92.0.4515.107 Safari/537.36",
#                        "SAAS-TOKEN": cookies}
#             res = requests.get(url=request_url, params=params, headers=headers, verify=False)
#
#             if res.json()['data'] == []:
#                 print("否")
#             else:
#                 print(res.json()['data'][0]['eventTime'])
                # print('是')



            # 交通事件-过滤事件
            # request_url = "http://10.5.1.156:10280/v1/app/events"
            # headers = {"Content-Type": "application/json",
            #            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            #            "SAAS-TOKEN": cookies}
            # params = {"type": "jtsj", "marking": "filtered", "eventTypeList":2455,"page": 1, "taskId": i, "size": "36", "eventTimeStart": "2022-03-29 20:00:00",
            #           "eventTimeEnd": "2022-03-30 23:59:59", "authMenuCode": "svc", "authTaskType": "jtsj", "authMarking": "filtered",
            #           "__timestamp__": "1648616106263"}
            # res = requests.get(url=request_url, params=params, headers=headers, verify=False)
            # if res.json()['data'] == []:
            #      print("不在")
            # else:
            #     # print('模型检测')
            #     print(res.json()['data'][0]['eventTime'])


# TestBus().error_bus()









# if __name__ == '__main__':
#         import re
#         url = 'http://10.5.1.161:10107/cas/login?service=http://10.5.1.161:10280/?appCode=console'
#         res = requests.get(url).text
#         pattre = '<input.*?execution.*?value="(.*?)"'
#         res = re.search(pattre, res, re.S)
#         if res:
#             print(res.group(1))




