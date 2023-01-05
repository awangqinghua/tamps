#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/11/29 15:17
# @Author   : qinghua
# @Email    : 867075698@qq.com
# @File     : get_variable.py
# @Software : PyCharm

import requests
import re
import time


# 设置url
def start_url():
    new_url = "http://47.97.184.108"
    return new_url


# 获取时间戳
def test_time():
    times = int(time.time()*1000)
    return times


# 先获取execution的value,再获取登录token
def execution():
    url = f'{start_url()}:10107/cas/login?service={start_url()}:10280/?appCode=console'
    res = requests.get(url).text
    patter = '<input.*?execution.*?value="(.*?)"'
    res = re.search(patter, res, re.S)
    if res:
        executions = res.group(1)
    return executions


class TestLogin:

    def test_login(self):
        login_url = f'{start_url()}:10107/cas/v1/tickets'
        data = {'username': 'admin', 'password': 'smai123',
                  'appCode': 'console', 'service': f'{start_url()}:10280/?appCode=console',
                  "execution": execution(), "_eventId": "submit"}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = requests.post(url=login_url, data=data, headers=headers, verify=False)
        login_urls = f'{start_url()}:10280/v1/app/login?ticket=%s&service=' \
                     f'{start_url()}:10280/?appCode=console&__timestamp__={test_time()}' % (data.json()['data'])
        res = requests.get(login_urls)
        if res.json()['data']['token']:
            setattr(GetDate, "COOKIES", res.json()['data']['token'])
        else:
            print("获取token失败")

        return res.json()['data']['token']


# 先赋值cookies为None
class GetDate:
    COOKIES = None


def test_type():
    types = "fjdc"
    return types


# 设置开始到结束时间
def test_start_time():
    event_time_star = "2022-12-19 15:00:00"
    return event_time_star


def test_end_time():
    event_time_end = "2022-12-19 17:20:00"
    return event_time_end


if __name__ == '__main__':

    print(TestLogin().test_login())
