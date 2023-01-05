#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/8/9 9:50
# @Author :wangqinghua
# @File : 0809腾讯社招网.py
# @Software : PyCharm

import time
import requests

headers = {"User-Agent": "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
statu_url = 'https://careers.tencent.com/tencentcareer/api/post/Query'
list_params = {'timestamp': '1660020360333', 'keyword': 'java', 'pageIndex': 1, 'pageSize': 10, 'language': 'zh-cn',
               'area': 'us'}


# 返回总页数
def get_job_list(pag_dex):
    list_params['pageIndex'] = pag_dex
    res = requests.get(statu_url, params=list_params, headers=headers)
    if res.status_code == 200:
        data = res.json()
        return data
    else:
        print('请求列表页失败。')


counts = int(get_job_list(1)['Data']['Count'] / 10 + 1)

datas = get_job_list(1)


def post_id(dates):
    res = dates['Data']['Posts']
    list_id = []
    for response in res:
        posts_id = response.get('PostId')
        list_id.append(posts_id)
    return list_id


# 测试获取第一页所有的post_id
# print(post_id(data))


# 收集全部工作的postid到一个列表中
pods_list = []
for i in range(counts):
    # print('开始下载第%d页'%(i+1))
    data = get_job_list(i + 1)
    id_list = post_id(data)
    pods_list.extend(id_list)

# 详情页真正的url

detail_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
postid = ''
detail_params = {
    'timestamp': '1596720223424',
    'postId': postid,
    'language': 'zh-cn'
}


def get_detail(postids):
    # 请求每个工作的详情页
    detail_params['postId'] = postids
    res = requests.get(detail_url, params=detail_params, headers=headers)
    if res.status_code == 200:
        date = res.json()
        return date
    else:
        print('下载{}详情页失败。'.format(postid))


def parse_detail(data):
    # 从每个工作的详情页数据中提取所需内容，写入txt文件
    time.sleep(1)
    title = data['Data']['RecruitPostName']
    location = data['Data']['LocationName']
    requirement = data['Data']['Requirement']
    job = '\n'.join([title, location, requirement, '*' * 50])
    with open(r'E:/temp/ten_cent4.txt', 'a', encoding='utf-8') as f:
        f.write(job)
        f.write('\n')


for i in postid_list:
    data = get_detail(i)
    if data:
        parse_detail(data)
    elif data == "" or data == None or data == 'null':
        print('下载完成')
    else:
        print("下载超时")
