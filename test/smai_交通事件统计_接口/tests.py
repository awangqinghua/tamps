#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/12/12 14:27
# @Author   : wqh
# @Email    : 867075698@qq.com
# @File     : tests.py
# @Software : PyCharm


import pandas as pd

df = pd.read_excel(r'D:\tamps\data\data1130\1206.xlsx', engine='openpyxl')

res = df.设备编号
report = []
for i in res:
    report.append(i)
print(report)
