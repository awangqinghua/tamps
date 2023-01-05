#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/9/26 17:53
# @Author   : qinghua
# @Email    : 867075698@qq.com
# @File     : 对比.py
# @Software : PyCharm

from do_excel_mysql.mysql_s import DeExcel
from do_excel_mysql.do_excels import DeExcels

s = DeExcel(r"D:\tamps\data\大型车占用主车道.xlsx", "Sheet1").get_data() # 788
r = DeExcels(r"D:\tamps\data\大型车负.xlsx", "Sheet1").get_data()  # 50
video_paths = []
for i in s:
    video_paths.append(i)
video_path = []
for i in r:
    video_path.append(i['video_path'])
for i in range(787):
    for sg in video_path:
        res = ''
        if sg in video_paths[i].values():
            import json
            res_mg = json.dumps(video_paths[i], ensure_ascii=False)
            res += res_mg+'\n'
            with open(r'/data/data0728/res.text', 'a', encoding='utf-8') as f:
                f.write(res)




