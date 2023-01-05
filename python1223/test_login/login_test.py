#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/1/5 10:35
# @Author   : wqh
# @Email    : 867075698@qq.com
# @File     : login_test.py
# @Software : PyCharm


class LoginTest:

    # def __init__(self,a,b):
    #     self.a = a
    #     self.b = b

    def teacher(self, a, b):
        print("{}今年{}岁".format(a, b))

    @staticmethod
    def teachers(*args):
        print("我喜欢吃的有：{}".format(args))


# LoginTest().teacher("小明", 20)

cc = ["培根", "火腿", "三明治", "烤红薯"]
for i in cc:
    i.split(',')
    LoginTest().teachers(i)


