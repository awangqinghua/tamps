#!/usr/bin/env python
# @Time     : 2022-06-25 20:58
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : class_06252社招.py
# @Software : PyCharm


import requests

# 列表页真正的url

list_url='https://careers.tencent.com/tencentcareer/api/post/Query'
pageIndex=1
list_params={
'timestamp': '1596719107828',
'keyword': 'python',
'pageIndex': pageIndex,
'pageSize': 10,
'language': 'zh-cn',
'area': 'us'
}
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


def get_job_list(pageIndex):
    list_params['pageIndex']=pageIndex
    res=requests.get(list_url,params=list_params,headers=head)
    if res.status_code==200:
        data=res.json()
        return data
    else:
        print('请求列表页失败。')

# 抓取第一页，目的是获取工作总数，以便知道需要抓取多少页
data=get_job_list(1)
pagenum=int(data['Data']['Count']/10)


def get_ids(data):
    # 从列表页中解析并找到所有工作的PostId

    p_list = data['Data']['Posts']
    id_list = []
    for p in p_list:
        post_id = p.get('PostId')
        id_list.append(post_id)
    return id_list


# 收集全部工作的postid到一个列表中
postid_list=[]
for i in range(pagenum):
    # print('开始下载第%d页'%(i+1))
    data=get_job_list(i+1)
    id_list=get_ids(data)
    postid_list.extend(id_list)


#详情页真正的url

detail_url='https://careers.tencent.com/tencentcareer/api/post/ByPostId'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
postid=''
detail_params={
'timestamp': '1596720223424',
'postId': postid,
'language': 'zh-cn'
}


def get_detail(postid):
    # 请求每个工作的详情页
    detail_params['postId']=postid
    res=requests.get(detail_url,params=detail_params,headers=headers)
    if res.status_code==200:
        data=res.json()
        return data
    else:
        print('下载{}详情页失败。'.format(postid))


def parse_detail(data):
    # 从每个工作的详情页数据中提取所需内容，写入txt文件

    title = data['Data']['RecruitPostName']
    location = data['Data']['LocationName']
    requirement = data['Data']['Requirement']
    job = '\n'.join([title, location, requirement, '*' * 50])
    with open('ten_cent4.txt', 'a', encoding='utf-8') as f:
        f.write(job)
        f.write('\n')


for i in postid_list:
    data=get_detail(i)
    if data:
        parse_detail(data)