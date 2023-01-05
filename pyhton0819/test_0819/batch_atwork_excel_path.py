# _*_ coding:utf-8 _*_

import multiprocessing
import random
import time
import sys
import numpy as np
import requests
import urllib3
from urllib.parse import unquote
from Email import Mailer
from excel_util import ExcelUtil

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 获取登录token
def login_token(ip):
    login_url = 'http://%s:10107/cas/v1/tickets' % ip
    params = {'username': 'admin', 'password': 'smai123', 'appCode': 'console', 'service': 'http://127.0.0.1'}
    data = requests.post(url=login_url, data=params, headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=False)
    print(data.json()['data'])
    login_url = 'http://%s:10106/v1/app/login?ticket=%s&service=http://127.0.0.1' % (ip,data.json()['data'])
    print(login_url)
    data_token = requests.get(url=login_url, verify=False)
    print(22222222222222)
    return data_token.json()['data']['token']

# 上传图片，并返回图片的url
def upload_pictures(pictures, data_token):
    filepath = r'C:\project\tupian\%s' %pictures
    upload_url_api = 'http://100.100.142.176:10280/v1/app/consts/upload/file?bucketName=default&folderPrefix=task'
    files = {"file": (filepath, open(filepath, "rb"))}
    up = requests.post(upload_url_api,headers={'SAAS-TOKEN': data_token}, files=files)
    return up.json()['data']

def add_monitor_json(bk_name, monitor_id, rois1,upload_pictures, tp, event_dict_type):
    print(upload_pictures, 1122334455)
    if len(np.array(rois1).shape) == 1:
        rois = [rois1]
        print(111111111111111111)
    else:
        rois = rois1
        print(rois, 2222222111231162222222)
    if 'jdc' in event_dict_type:
        # return {"analyze_config":{"violations":upload_pictures,"rois":rois,"trafficFlowViolations":[],"ptz_pos":None},"name":"%s" % bk_name,"stream_id":"%s" % monitor_id,"extra":{"sub_org_code":"1000","snapshotSize":720393,"organizationPath":"/1000"},"ptz_pos":"","stream_on":"OFF","type":"jdc"}
        return {"analyze_config":{"violations":upload_pictures,"rois":rois,"trafficFlowViolations":[],"enable_tracking_debug":False,"ptz_pos":None},"name":"%s" % bk_name,"stream_id":"%s" % monitor_id,"extra":{"scene_id": "common", "sub_org_code":"1000","snapshotSize":476518,"organizationPath":"/1000"},"ptz_pos":"","stream_on":"ON","snapshot":"%s" % tp,"type":"%s" % event_dict_type}
    if 'jtsj' in event_dict_type:
        if upload_pictures[0]['code'] == '2115':
            upload_pictures[0]['code'] = '2417'
        return {"analyze_config": {"violations": upload_pictures, "rois": rois, "enable_tracking_debug": False},"name": "%s" % bk_name, "stream_id": "%s" % monitor_id, "ptz_pos": "", "stream_on": "ON","snapshot": "%s" % tp,"extra": {"scene_id": "common", "org_code": "1000", "sub_org_code": "1000", "snapshotSize": 349527,"organizationPath": "/1000"}, "type": "%s" % event_dict_type}
    if 'jmsj' in event_dict_type:
        # return {"analyze_config":{"violations":[{"code":"19","on":True,"roi":[{"id":1,"data":[36,72,2520,52,2460,1392,56,1392]}],"enable_vehicle_detect":False,"cooling_second":10,"name":"区域入侵","ptz_pos":None,"render":True}],"trafficFlowViolations":[],"enable_tracking_debug":True,"render":0,"ptz_pos":None},"name":bk_name,"stream_id":monitor_id,"extra":{"sub_org_code":"1000","snapshotSize":774223,"organizationPath":"/1000","eventTypeCaptures":[{"img":"http://100.100.142.227:9000/default/static/event/2021/1214/17/kx5xl5nf10.jpg","eventType":"19","eventTypeName":"区域入侵"}]},"ptz_pos":"","stream_on":"ON","snapshot":"http://100.100.142.227:9000/default/static/task/2021/1214/17/kx5xjwkl55.jpg","type":"flow"}
        return {"analyze_config": {"violations": upload_pictures, "rois": rois, "enable_tracking_debug": True},"name": "%s" % bk_name, "stream_id": "%s" % monitor_id, "ptz_pos": "", "stream_on": "ON","snapshot": "%s" % tp,"extra": {"scene_id": "common", "org_code": "1000", "sub_org_code": "1000", "snapshotSize": 349527,"organizationPath": "/1000"}, "type": "%s" % event_dict_type}
    if 'sgjg' in event_dict_type:
        return {"analyze_config":{"violations":upload_pictures,"trafficFlowViolations":[],"enable_tracking_debug":True,"ptz_pos":None},"name": "%s" % bk_name, "stream_id": "%s" % monitor_id,"extra":{"sub_org_code":"1000","snapshotSize":375450,"organizationPath":"/1000","eventTypeCaptures":[{"img":"http://100.100.152.113:9000/default/static/event/2022/0112/11/kyb08do619.jpg","eventType":"2307","eventTypeName":"占道施工"}]},"stream_on":"ON","snapshot": "%s" % tp,"type": "%s" % event_dict_type}
    if 2 == rois[-1]:
        print([rois.pop(-1)],4444444)
        return {"analyze_config":{"violations":upload_pictures,"rois":rois,"enable_tracking_debug":True},"name":"%s" % bk_name,"stream_id":"%s" % monitor_id,"ptz_pos":"","stream_on":"ON","snapshot":"%s" % tp,"extra":{"scene_id":"common","org_code":"1000","sub_org_code":"1000","snapshotSize":349527,"organizationPath":"/1000"},"type":"%s" % event_dict_type}
# 添加布控
def add_monitor(ip, data_token, bk_name,monitor_id, rois,upload_pictures, tp, event_type, at_list=None, start_state= '1'):
    if start_state == '1':
        monitor_url = 'http://%s:10280/v1/app/task?start=true' %ip
    else:
        monitor_url = 'http://%s:10280/v1/app/task?start=false' % ip
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'SAAS-TOKEN': data_token
       }
    params = add_monitor_json(bk_name, monitor_id, rois,upload_pictures, tp, event_type)
    if 'fjdc' == event_type:
        params['analyze_config'].pop('rois')
    print(params,'布控json数据')
    # 添加布控
    am = requests.post(url=monitor_url, headers=headers, json=params,verify=False)
    print('布控返回结果', am.json())
    if '+' in bk_name:
        url = f'http://{ip}:10280/v1/app/task?page=1&size=50&type={event_type}&nameLike={bk_name.split("+")[1]}'
    else:
        url = f'http://{ip}:10280/v1/app/task?page=1&size=50&type={event_type}&nameLike={bk_name}'
    print(url,33333333444444444444)
    # 查看布控信息
    sc = requests.get(url=url, headers=headers, verify=False)
    if [] == sc.json():
        sc = requests.get(url=url, headers=headers, verify=False)
    # atwork的详细数据  先隐藏
    if at_list != None:
        print(am.json(), at_list[1], at_list[3], 44444444444444444444)
        print(event_type, at_list[1], at_list[3], 2222222222222222222, event_type)
        print(sc.json(), 3333333333333333333333)
        return am.json(), event_type, sc.json()['data'][0]['id']
    else:
        return am.json()

# 同步摄像头
def synchronizing_camera(ip, data_token):
    for i in range(30):
        monitor_url = 'http://%s:10280/v1/portal/organization/camera/sync' % ip
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'SAAS-TOKEN': data_token
        }
        sc = requests.get(url=monitor_url, headers=headers,verify=False)
        if 'OK' in sc.json()['message']:
            print('摄像头同步成功')
            return sc.json()
        else:
            time.sleep(10)
            print(sc.json(), f'摄像头没有同步{i}次')
            if i == 9:
                print(sc.json(), f'摄像头已等待{i}次，没有同步成功，结束运行')
                return
# 开启取证视频
def forensics_video(data_token, v_ip,monitor_id, monitor_type):
    forensics = f'http://{v_ip}:10280/v1/app/task'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'SAAS-TOKEN': data_token
       }
    params = {"id":"%s" % monitor_id,"extra":{"scene_id":"common","sub_org_code":"1000","org_code":"1000","organizationPath":"/1000","snapshotSize":510449,"createBy":1,"updateBy":1,"appCode":"console","evidenceDownload":"ON"},"type":"%s" % monitor_type}
    fv = requests.put(url=forensics, headers=headers, json=params,verify=False)
    return fv.json()

# 获取布控信息
def obtain_monitor(ip, data_token, monitor_id, monitor_type):
    for i in range(100):
        try:
            monitor_url = 'http://%s:10280/v1/app/task?page=1&size=500&type=%s' % (ip, monitor_type)
            headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'SAAS-TOKEN': data_token
            }
            sc = requests.get(url=monitor_url, headers=headers, verify=False)
            for i in sc.json()['data']:
                if monitor_id == i['name']:
                    return i
        except Exception as e:
            time.sleep(1)
            print(f'已寻找布控列表{i}次')

# 获取布控状态
def monitor_state(ip, data_token, stream_id, monitor_type):
    global ms
    monitor_url = 'http://%s:10280/v1/app/task?page=1&size=50&type=%s&stream_id=%s' % (ip, monitor_type, stream_id)
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'SAAS-TOKEN': data_token
    }
    for i in range(30):
        ms = requests.get(url=monitor_url, headers=headers, verify=False)
        if 'running' == ms.json()['data'][0]['status']:
            return ms.json()['data'][0]['id'],ms.json()['data'][0]['type'], ms.json()['data'][0]['name']+'【布控运行成功】'
        elif 'retrying' == ms.json()['data'][0]['status']:
            print('已寻找【' + ms.json()['data'][0]['id'] + '】第【' + str(i + 1) + '】次，状态为：【' + ms.json()['data'][0]['status'] + '】')
            time.sleep(1)
        else:
            print('已寻找【'+ms.json()['data'][0]['id']+'】第【'+str(i+1)+'】次，状态为：【'+ms.json()['data'][0]['status']+'】')
            time.sleep(1)
    else:
        status = modification_control(ip, data_token, 'stop', ms.json()['data'][0]['id'], monitor_type)
        if '启动失败' in status:
            print('已等待【'+str(i+1)+'】秒，状态为：【'+ms.json()['data'][0]['status']+'】，布控启动失败')
            return ms.json()['data'][0]['id'], ms.json()['data'][0]['type'], ms.json()['data'][0]['name']+'【布控启动失败】'
        elif '停止失败' in status:
            print('已等待【'+str(i+1)+'】秒，状态为：【'+ms.json()['data'][0]['status']+'】，布控停止失败')
            return ms.json()['data'][0]['id'], ms.json()['data'][0]['type'], ms.json()['data'][0]['name']+'【布控停止失败】'
        elif '启动成功' in status:
            print('已等待【'+str(i+1)+'】秒，状态为：【'+ms.json()['data'][0]['status']+'】，布控启动成功')
            return ms.json()['data'][0]['id'], ms.json()['data'][0]['type'], ms.json()['data'][0]['name']+'【布控启动成功】'
        elif '停止成功' in status:
            print('已等待【'+str(i+1)+'】秒，状态为：【'+ms.json()['data'][0]['status']+'】，布控停止成功')
            return ms.json()['data'][0]['id'], ms.json()['data'][0]['type'], ms.json()['data'][0]['name']+'【布控停止成功】'

# 修改布控状态
def modification_control(ip, data_token, task_state,stream_id, monitor_type):
    global ms
    modification_url = f'http://{ip}:10280/v1/app/task/{task_state}?ids={stream_id}&type={monitor_type}'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'SAAS-TOKEN': data_token
    }
    ms_stop = requests.get(url=modification_url, headers=headers, verify=False).json()
    print(ms_stop)
    for i in range(30):
        monitor_url = f'http://{ip}:10280/v1/app/task?page=1&size=50&type={monitor_type}&id={stream_id}'
        ms = requests.get(url=monitor_url, headers=headers, verify=False)
        time.sleep(3)
        if 'stop' == task_state:
            if 'stopped' == ms.json()['data'][0]['status']:
                return '停止成功'
            else:
                print('已停止【'+ms.json()['data'][0]['id']+'】第【'+str(i+1)+'】次，状态为：【'+ms.json()['data'][0]['status']+'】')
                time.sleep(1)
                if i+1 == 30:
                    return '停止失败'
        elif 'start' == task_state:
            if 'running' == ms.json()['data'][0]['status']:
                return '运行成功'
            else:
                print('已启动【'+ms.json()['data'][0]['id']+'】第【'+str(i+1)+'】次，状态为：【'+ms.json()['data'][0]['status']+'】')
                time.sleep(1)
                if i+1 == 30:
                    return '运行失败'

# 删除布控
def delete_Control(ip, data_token, stream_id, monitor_type):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'SAAS-TOKEN': data_token
    }
    delete_url = f'http://{ip}:10280/v1/app/task/delete?ids={stream_id}&type={monitor_type}'
    delete_task = requests.get(url=delete_url, headers=headers, verify=False)
    if 'OK' == delete_task.json()['codeName']:
        return '删除成功'
    else:
        return '删除失败'
# 通过任务编号获取预警列表信息，把matedata中的模型id和判断标准都传进行，
def warning_list(ip, data_token,task_id, monitor_type, mate_data):
    print(mate_data, 11111111111111,type(mate_data[0]))
    # 机动车抓拍
    motorsnap_list = [2228, '2228']
    # 机动车违法
    motorevent_list = [2221, 2222, 2223, 2224, 2225, 2226, 2227,'2221', '2222', '2223', '2224', '2225', '2226', '2227']
    if mate_data[0] in motorsnap_list:
        tag_type = 'motorsnap'
    elif mate_data[0] in motorevent_list:
        tag_type = 'motorevent'
    else:
        tag_type = 'normal'
    print(tag_type, 11111111111111)
    monitor_url = f'http://{ip}:10280/v1/app/events?type={monitor_type}&marking=init&eventTypeList={mate_data[0]}&taskId={task_id}&page=1&size=36&tag1={tag_type}&authMenuCode=svc&authTaskType={monitor_type}&authMarking=init'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'SAAS-TOKEN': data_token
    }
    early_warning = None  # 预警列表
    filter_list = None  # 过滤列表
    for i in range(300):
        if '头盔' in mate_data[1]:
            # 摩托车预警列表
            monitor_url = f'http://{ip}:10280/v1/app/events?type=jdc&marking=init&taskId={task_id}&page=1&size=36&tag1=motorevent&authMenuCode=svc&authTaskType=jdc&authMarking=init'
            # 过滤预警列表
            monitor_url1 = f'http://{ip}:10280/v1/app/events?type=jdc&marking=filtered&page=1&size=36&taskId={task_id}&authMenuCode=svc&authTaskType=jdc&authMarking=filtered'
            if early_warning  == None:
                ms = requests.get(url=monitor_url, headers=headers, verify=False)
                if ms.json()['data'] != []:
                    for j in ms.json()['data']:
                        if str(mate_data[0]) == j['eventType']:
                            try:
                                early_warning = str(j['eventType'])
                                break
                            except Exception as e:
                                print(e, '捕获的异常数据1')
                                return j['eventType'], j['displayName']
                else:
                    time.sleep(0.5)
                    print('已等待【' + str(i + 1) + '】秒，没有找到：【' + task_id + '】的预警信息')
            if filter_list  == None:
                ms = requests.get(url=monitor_url1, headers=headers, verify=False)
                if ms.json()['data'] != []:
                    for j in ms.json()['data']:
                        if str(mate_data[0]) == j['eventType']:
                            try:
                                filter_list = str(j['eventType'])
                                break
                            except Exception as e:
                                print(e, '捕获的异常数据1')
                                return j['eventType'], j['displayName']
                else:
                    time.sleep(0.5)
                    print('已等待【' + str(i + 1) + '】秒，没有找到：【' + task_id + '】的过滤信息')
            if i == 299:
                if early_warning != None and filter_list != None:
                    return early_warning, '预警和过滤都找到了'
                elif early_warning != None and filter_list == None:
                    return early_warning, '预警找到了，过滤没有找到'
                elif early_warning == None and filter_list != None:
                    return filter_list,  '预警没有找到，过滤找到了'
        else:
            try:
                ms = requests.get(url=monitor_url, headers=headers, verify=False)
                # print(ms.json(),11111111111111111)
                if ms.json()['data'] != []:
                    for j in ms.json()['data']:
                        if str(mate_data[0]) == j['eventType']:
                            try:
                                return j['eventType'], j['displayName'], j['plateNumber']
                            except Exception as e:
                                print(e, '捕获的异常数据1')
                                return j['eventType'], j['displayName']
                else:
                    time.sleep(1)
                    print('已等待【'+str(i+1)+'】秒，没有找到：【'+task_id+'】的预警信息')
            except Exception as e:
                print(e, '捕获的异常数据2')
                print('寻找预警信息，接口报错，进行循环寻找预警')
    else:
        return '已等待【'+str(i+1)+'】秒，没有找到：【'+task_id+'】的预警信息，没有产生预警信息'
# 添加vmr摄像头
def vmr_video(ip, device,vmr_name,atwork_video):
    name_list = []
    print(ip, device, vmr_name, atwork_video, 999999999999)
    for i in requests.get('http://%s:8900/v2/sub_device?device_id=%s' % (ip, device), headers={'X-VMR-TOKEN': 'AAAAB3NzaC1yc2EAAAADAQABAAABAQC8GYJuIKu/2RROHiXOnMy1uZfGXz5pvb/N1Pcws8tdwMmTIqFMt'}).json()['data']['content']:
        name_list.append(i['attribute']['name'])
    if vmr_name not in name_list:
        print(atwork_video,2341231231231)
        data = {"device_id": "%s" % device, "attribute": {"name": "%s" % vmr_name, "upstream_url":"%s" % atwork_video, "discovery_protocol": 2, "vendor": 1}, "channel": 0, "type": 1, "user_data": "{}", "cache_flag": 1, "capability":{}}
        print(data,123121312)
        vmr1 = requests.post('http://%s:8900/v2/sub_device' % ip, headers={'X-VMR-TOKEN': 'AAAAB3NzaC1yc2EAAAADAQABAAABAQC8GYJuIKu/2RROHiXOnMy1uZfGXz5pvb/N1Pcws8tdwMmTIqFMt'}, json=data)
        print(ip, device, vmr_name, atwork_video, 88888888888888)
        print(vmr1,999911999)
        print(vmr1.json())
        if 0 == vmr1.json()['code']:
            print('摄像头已添加')
        elif 20400 == vmr1.json()['code']:
            print('摄像头添加失败')
        return vmr1.json()['data']['attribute']['name'], vmr1.json()['data']['id']
    else:
        print('摄像头已存在，跳过添加摄像头')
        for i_id in requests.get('http://%s:8900/v2/sub_device?device_id=%s' % (ip, device), headers={'X-VMR-TOKEN': 'AAAAB3NzaC1yc2EAAAADAQABAAABAQC8GYJuIKu/2RROHiXOnMy1uZfGXz5pvb/N1Pcws8tdwMmTIqFMt'}).json()['data']['content']:
            if vmr_name == i_id['attribute']['name']:
                return i_id['attribute']['name'],i_id['id']

atwork_url = 'http://atwork.atom.supremind.io'
atwork_header = {
    # 云地址:https://atwork.op.qt.supremind.info/
    # 内网地址:http://atwork.atom.supremind.io/
    'Authorization': 'idToken eyJhbGciOiJSUzI1NiJ9.eyJhdWQiOlsiYXRvbSIsImFwaXNlcnZlciIsImxhYmVseCIsImFuYWx5emVyIl0sImVtYWlsIjoiXCJsaXpoZW5Ac3VwcmVtaW5kLmNvbVwiIiwiZXhwIjoxNjQ3NDA5MTIwLCJpYXQiOjE2NDQ4MTcxMjAsImlzcyI6ImhvZG9yIiwianRpIjoiMzI5OTM2OTAtMDExMy00Y2NiLWI3NWYtZjFkNWU2MzNhMWMyIiwic3ViIjoiXCIyNzlcIiIsInVwc3RyZWFtX3Rva2VuIjoiMTFlNDdhYzkwNjI0MTAzNmZlOTkwMzMzOGI2MGNkNTUzMTNhZDlhNzFhMzhiZjk1MzQyN2VhMGNlMDNkYzFlNCIsInVzZXJuYW1lIjoiXCJsaXpoZW5cIiJ9.0s6r7aByl86VKo9lS0Iwvs08wXS3k25cvvOTrpnEReUHOGjq9rQoFbRJA0r_bqLcHGED_bGB1CBy1YNLSR2lA6A-vyLPtHywrS7qP90epEMkbsyA0P42kb_i6QKWOTv-CBLIx8iwjNMzXEGRRANacSGjeu5ocu0tygbtPbjvMZyC_FiNDoh0uc_XIHzPS0QNW6winlXvkhiLDOaPkK8EJVAqOeZOLOKrKNKvYthPl_PaTmLBEUAose7v3fBMLEAfgCA5_JnvMXxNF885aTtcjr_bLF8hZjGd9M7x7Ndx2wJueXPSfgpXtmu4q78A6Nyjh8yorDTAnSWwlGq0amZgeA',
    'Content-Type': 'application/json',
    'Origin': atwork_url}

# 获取atwork所有文件
def atwork_data(file_name='', batch='', cameraPosition='', customer='', eventType=None, oreType=None, number=500, batch_type='空'):
    global list_jpg
    atwork_list = []
    data1 = {
        "fileName": file_name,
        "batch": batch,
        "cameraPosition": cameraPosition,
        'oreType': oreType,
        'customer': '%s' %customer,
        # "volume": "supreop-metal-volume-aliyun"
        # 'eventType': {"logic":1,'values':eventType}
    }
    data = requests.post(url=f'{atwork_url}/api/metal/search_with_download_url', json=data1,headers=atwork_header, verify=False)
    if file_name != '':
        if [] != data.json()['data']['items']:
            for i in data.json()['data']['items']:
                for j in i['files']:
                    if 'mp4' in j:
                        ret3 = unquote(j, encoding='utf-8')
                        atwork_list.append(ret3)
                        print(ret3,1213123333333333333333333333)
                        if 'https' in atwork_url:
                            atwork_list.append(ret3.replace('https://librarian.op.qt.supremind.info', 'http://100.100.142.234'))
                        else:
                            atwork_list.append(ret3.replace('atwork-fs.atom.supremind.io','100.100.142.234'))
                    # elif 'metadata.json' in j:
                    #     data1 = requests.get(url='%s' % j, headers=atwork_header, verify=False).json()
                    #     atwork_data(file_name='', batch='', cameraPosition='', customer='', eventType=None,oreType=None, number=500, batch_type='空')
                    else:
                        atwork_list.append(j)
        else:
            print(file_name,'没有拿到atwork数据，添加失败')
        return atwork_list
    elif batch != '' or customer != '' or cameraPosition != '':
        list_jpg1 = []
        int_num = 0
        print(123131231223, len(data.json()['data']['items']))
        if batch_type == '1':
            for i in data.json()['data']['items']:
                # print(i, type(i['files']),len(set(i['files'])))
                list_jpg = []
                for i_data in set(i['files']):
                    if 'metadata.json' in i_data:
                        print(i_data,2233445566)
                        try:
                            data1 = requests.get(url='%s' % i_data, headers=atwork_header, verify=False).json()
                            list_jpg.append(data1['raw']['event_meta']['code'])
                            int_num += 1
                            print(int_num, data1['raw']['event_meta']['code'])
                        except Exception as e:
                            pass
                    if 'feature.jpg' in i_data:
                        if 'https' in atwork_url:
                            list_jpg.append(i_data.replace('https://librarian.op.qt.supremind.info', 'http://100.100.142.234'))
                        else:
                            list_jpg.append(i_data.replace('atwork-fs.atom.supremind.io','100.100.142.234'))
                if len(list_jpg) >= 1:
                    list_jpg1.append(list(set(list_jpg)))
                if len(list_jpg1) >= int(number):
                    break
            return list_jpg1
        elif batch_type == '2' or batch_type == '3' or batch_type == '空':
            if [] != data.json()['data']['items']:
                for i in data.json()['data']['items']:
                    for j in i['files']:
                        if 'mp4' in j:
                            atwork_list.append(j.split('?u=')[0].split('/')[-1])
            else:
                print(file_name, '没有拿到atwork数据，添加失败')
            return atwork_list

# 获取数据json数据
def atwork_json(at_json):
    atwork_list = []
    print(at_json,121321312321)
    data1 = requests.get(url='%s' %at_json, headers=atwork_header, verify=False).json()
    try:
        atwork_list.append('自动-' + data1['key'].rsplit('/')[-1])
    except Exception as e:
        print(e, '捕获的异常数据3')
        print(at_json,33333333333)
        atwork_list.append(data1['key'].rsplit('/')[-1])
    try:
        atwork_list.append(data1['event']['task_config']['rois'])
    except Exception as e:
        try:
            atwork_list.append(data1['event']['task_config']['violations'][0]['roi'])
        except Exception as e:
            atwork_list.append([[72, 93, 1836, 66, 1812, 1029, 66, 1038]])
            print(e, '捕获的异常数据4')
    atwork_list.append(data1['event']['task_config']['violations'])
    atwork_list.append(data1['product_code'])
    atwork_list.append(data1['raw'])
    return atwork_list

def batch_atwork_vmr(at_v_list=None, at_v1=None, vmr_ip1=None, device_id1=None):
    if at_v_list != None:
        print(at_v_list,4444555555)
        at_v = at_v_list[5]
        vmr_ip = at_v_list[12]
        device_id = at_v_list[14]
        print(at_v,vmr_ip,device_id, 66666666)
    elif at_v1 != None:
        at_v = at_v1
        vmr_ip = vmr_ip1
        device_id = device_id1
    try:
        # 存放测试结果
        atwork = atwork_data(at_v)
        if [] == atwork:
            return
        print(f'视频是1【{at_v}】')
    except Exception as e:
        print(e, '捕获的异常数据5')
        print(at_v + ':视频出错了111', at_v_list)
        return
    # matedata预警数据
    mate_list = []
    if [] != atwork:
        atwork_list = atwork_json([i for i in atwork if 'metadata.json' in i][0])
        print(atwork_list[4],3333333)
        mate_list.append(atwork_list[4]['event_meta']['eventType'])
        mate_list.append(atwork_list[4]['event_meta']['eventTypeDesc'])
        try:
            mate_list.append(atwork_list[4]['event_meta']['code'])
        except Exception as e:
            try:
                mate_list.append(atwork_list[2]['event_meta']['code'])
            except Exception as e:
                try:
                    mate_list.append(atwork_list[4]['code'])
                except Exception as e:
                    try:
                        mate_list.append(atwork_list[2][0]['code'])
                    except Exception as e:
                        print(e, '捕获的异常数据6')
                        mate_list.append('保留字段')
        print(vmr_ip, device_id, atwork_list[0], 322222222222333333)
        vmr_id = vmr_video(vmr_ip, device_id, atwork_list[0], [i for i in atwork if '.mp4' in i][0])
        print(vmr_id)

def batch_atwork(at_v_list, delete_control, return_dict):
    at_v = at_v_list[5]
    vmr_ip = at_v_list[12]
    device_id = at_v_list[14]
    data_Token = at_v_list[17]
    try:
    # 存放测试结果
        atwork = atwork_data(at_v)
        data_token = data_Token
        if [] == atwork:
            return_dict[at_v] = '视频没有找到' + '---' + at_v + '---' + '保留字段' + '---' + '测试失败' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])  # at_v_list[10]工作表
            return
        print(f'视频是2【{at_v}】')
    except Exception as e:
        print(e, '捕获的异常数据7')
        print(at_v + ':视频出错了222')
        return_dict[at_v] = '视频出错了' + '---' + at_v + '---' + '保留字段' + '---' + '测试失败' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
        return
    # matedata预警数据
    mate_list = []
    if [] != atwork:
        atwork_list = atwork_json([i for i in atwork if 'metadata.json' in i][0])
        mate_list.append(atwork_list[4]['event_meta']['eventType'])
        mate_list.append(atwork_list[4]['event_meta']['eventTypeDesc'])
        try:
            mate_list.append(atwork_list[4]['event_meta']['code'])
        except Exception as e:
            try:
                mate_list.append(atwork_list[2]['event_meta']['code'])
            except Exception as e:
                try:
                    mate_list.append(atwork_list[4]['code'])
                except Exception as e:
                    try:
                        mate_list.append(atwork_list[2][0]['code'])
                    except Exception as e:
                        print(e, '捕获的异常数据8')
                        mate_list.append('保留字段')
        print(vmr_ip, device_id, atwork_list[0],322222222222333333)
        vmr_id = vmr_video(vmr_ip, device_id, atwork_list[0], [i for i in atwork if '.mp4' in i][0])
        print(vmr_id)
        # 同步摄像头
        # synchronizing_camera(vmr_ip, data_token)
        # 添加布控
        event_dict_type = ''
        event_dict = {'机动车': 'jdc', '摩托车': 'jdc', '非机动车': 'fjdc', '街面事件': 'jmsj', '交通事件': 'jtsj', '施工监管': 'sgjg'}
        if '非机动车' in ex.sheet_names()[-1]:
            event_dict_type = event_dict['非机动车']
        elif '摩托车' in ex.sheet_names()[-1]:
            event_dict_type = event_dict['摩托车']
        elif '机动车' in ex.sheet_names()[-1]:
            event_dict_type = event_dict['机动车']
        elif '街面事件' in ex.sheet_names()[-1]:
            event_dict_type = event_dict['街面事件']
        elif '交通事件' in ex.sheet_names()[-1]:
            event_dict_type = event_dict['交通事件']
        elif '施工监管' in ex.sheet_names()[-1]:
            event_dict_type = event_dict['施工监管']
        print(222, event_dict_type, 7777777777777777777777777, at_v_list)
        print(23141234124, vmr_ip, data_token, atwork_list[0], vmr_id[1], atwork_list[1], atwork_list[2], [i for i in atwork if 'raw.jpg' in i][0], event_dict_type, at_v_list,2341231341234131234)
        am = add_monitor(vmr_ip, data_token, atwork_list[0], vmr_id[1], atwork_list[1], atwork_list[2], [i for i in atwork if 'raw.jpg' in i][0], event_dict_type, at_v_list)
        # print(am[0],12345678)
        try:
            if 0 == am[0]['code']:
                print('布控创建成功，开启取证视频')
                fv = forensics_video(data_token, vmr_ip,am[0]['data']['id'], am[1])
                sp = fv['data']
                if '开启' == fv['data']['extra']['evidenceDownload']['text']:
                    print(atwork_list[0], '取证视频开启成功')
            elif '数据重复' == am[0]['message']:
                print('布控重复，搜索布控id')
                # 启动布控
                status = modification_control(vmr_ip, data_token, 'start', am[2], am[1])
                print(status, '运行状态')
                # 获取布控信息
                sp = obtain_monitor(vmr_ip, data_token, atwork_list[0], am[1])
                fv = forensics_video(data_token, vmr_ip, sp['id'], am[1])
                print(fv,5555555555566666666666)
                print(sp['id'], am[1],111111111111111111111)
                time.sleep(1)
                try:
                    if '开启' == fv['data']['extra']['evidenceDownload']['text']:
                        print(atwork_list[0], '取证视频开启成功')
                except Exception as e:
                    print(e, '捕获的异常数据9')
                    print(fv['error'], 33445566888)
                    return_dict[at_v] = '视频没有找到' + '---' + at_v + '---' + '保留字段' + '---' + fv['error'] + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
        except Exception as e:
            print(e, '捕获的异常数据10')
            print(am[0]['error'], 33445566)
            return_dict[at_v] = '视频没有找到' + '---' + at_v + '---' + '保留字段' + '---' + am[0]['error'] + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
    try:
        ms = monitor_state(vmr_ip, data_token, sp['stream_id'], am[1])
        ms_name = ms[2]
        print(ms)
    except Exception as e:
        print(e, '捕获的异常数据11')
        ms_name = '布控启动失败'
    if '布控运行成功' in ms_name:
        arly_warning = warning_list(vmr_ip, data_token, ms[0], ms[1], mate_list)
        print(type(arly_warning[0]), type(str(mate_list[0])),arly_warning, str(mate_list[0]), 21234123412341234123)
        if at_v_list[3] == '正样本':
            if '3' == str(len(arly_warning)):
                if arly_warning[0] == str(mate_list[0]):
                    if arly_warning[2] == str(mate_list[2]):
                        modification_control(vmr_ip, data_token, 'stop', ms[0], ms[1])
                        print(arly_warning)
                        print(mate_list)
                        print('断言成功1', ms[0], at_v_list[3], mate_list, arly_warning)
                        return_dict[at_v] = ms[0] + '---' + at_v + '---' + arly_warning[2] + '---' + '测试通过' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
                    elif arly_warning[2] != str(mate_list[2]) and arly_warning[2].strip() != '':
                        modification_control(vmr_ip, data_token, 'stop', ms[0], ms[1])
                        print(arly_warning)
                        print(mate_list)
                        print('断言成功2', ms[0], at_v_list[3], mate_list, arly_warning, f'测试失败车牌号不对1234{mate_list[2]}')
                        return_dict[at_v] = ms[0] + '---' + at_v + '---' + arly_warning[2] + '---' + f'测试失败车牌号不对123{mate_list[2]}' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
                    else:
                        modification_control(vmr_ip, data_token, 'stop', ms[0], ms[1])
                        print(arly_warning)
                        print(mate_list)
                        print('断言成功3', ms[0], at_v_list[3], mate_list, arly_warning)
                        return_dict[at_v] = ms[0] + '---' + at_v + '---' + '保留字段' + '---' + '测试通过' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
            else:
                print(modification_control(vmr_ip, data_token, 'stop', ms[0], ms[1]))
                print('断言成功4', ms[0], at_v_list[3], mate_list, arly_warning)
                return_dict[at_v] = ms[0] + '---' + at_v + '---' + '保留字段' + '---' + '测试失败' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
        if at_v_list[3] == '负样本':
            if '没有产生预警信息' in arly_warning:
                modification_control(vmr_ip, data_token, 'stop', ms[0], ms[1])
                print('断言成功5', ms[0], at_v_list[3], mate_list, arly_warning)
                return_dict[at_v] = ms[0] + '---' + at_v + '---' + '保留字段' + '---' + '测试通过' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
            elif arly_warning[0] == str(mate_list[0]):
                modification_control(vmr_ip, data_token, 'stop', ms[0], ms[1])
                print(arly_warning)
                print(mate_list)
                print('断言成功6', ms[0], at_v_list[3], mate_list, arly_warning)
                if '预警和过滤都找到了' in arly_warning[1]:
                    return_dict[at_v] = ms[0] + '---' + at_v + '---' + '保留字段' + '---' + f'测试失败【{arly_warning[1]}】' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
                elif '预警找到了，过滤没有找到' in arly_warning[1]:
                    return_dict[at_v] = ms[0] + '---' + at_v + '---' + '保留字段' + '---' + f'测试失败【{arly_warning[1]}】' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
                elif '预警没有找到，过滤找到了' in arly_warning[1]:
                    return_dict[at_v] = ms[0] + '---' + at_v + '---' + '保留字段' + '---' + f'测试通过【{arly_warning[1]}】' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
                else:
                    return_dict[at_v] = ms[0] + '---' + at_v + '---' + '保留字段' + '---' + '测试失败' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
        if 'yes' == delete_control:
            delete_Control(vmr_ip, data_token, ms.json()['data'][0]['id'], ms[1])
    # 布控只有运行失败后，才会执行该代码
    elif '布控启动失败' in ms_name:
        print('布控启动失败')
        try:
            modification_control(vmr_ip, data_token, 'stop', ms[0], ms[1])
            return_dict[at_v] = '布控启动失败'+ms[0] + '---' + at_v + '---' + '保留字段' + '---' + '测试失败布控任务启动失败' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
        except Exception as e:
            print(e, '捕获的异常数据13')
            return_dict[at_v] = '布控启动失败'+ms[0] + '---' + at_v + '---' + '保留字段' + '---' + '测试失败布控任务停止失败' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
    elif '布控停止成功' in ms_name:
        print('布控停止成功')
        try:
            modification_control(vmr_ip, data_token, 'stop', ms[0], ms[1])
            return_dict[at_v] = '布控停止成功'+ms[0] + '---' + at_v + '---' + '保留字段' + '---' + '测试失败布控停止成功' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])
        except Exception as e:
            print(e, '捕获的异常数据13')
            return_dict[at_v] = '布控停止成功'+ms[0] + '---' + at_v + '---' + '保留字段' + '---' + '测试失败布控停止成功' + '---' + str(at_v_list[10]) + '---' + str(at_v_list[0])

if __name__ == '__main__':
    # path_list = ['3s9H14-Q5rMAoUT5lI2XSQ==_0.mp4','9v0wkrKF4m6H-jcs_0wy0g==_0.mp4','A9C8E-3aVPCPkvlQCI5Stw==_0.mp4','CHHQjAIg8W-jjyT5xMfzOA==_0.mp4','dGYY4jx4LcniHS3dtbL2eg==_0.mp4']
    # vmr_ip = '100.100.142.202'
    # device_id = 'QN00116868c68468c2315'
    # concurrency = '20'
    # at_v_str = '31010419051181202006_1620594243_1620594363.mp4'
    # at_v_list = at_v_str.split(',')
    # delete_control = 'no'
    # print(vmr_ip, device_id, at_v_list)
    # for i in at_v_list:
    #     batch_atwork(vmr_ip, device_id, i, delete_control, 'sadf')
    '''
    1、获取所有的excel中所有的sheet
    2、获取每个sheet的所有数据
    3、循环运行每个sheet的数据，测试结果已【{sheet: 测试结果}】
    '''
    try:
        excel_path_data = sys.argv[1]
        number = sys.argv[2]
        mailto = sys.argv[3]
        carbon_copy = sys.argv[4]
        print(mailto,55555555555555222222222)
        print(excel_path_data, number,12331231231231235555555555555555555)
    except Exception as e:
        mailto = 'lizhen@supremind.com'
        carbon_copy = 'no'
        excel_path_data = '/jenkinscicd/布控测试集/0217-116-fu-mtc.xls'
        number = '20'
    at_v_list = []
    server_ip = []
    ex = ExcelUtil(excel_path=excel_path_data)
    ex.sheet_names()
    print(ex.get_lines(), ex.sheet_names())  # 获取行数
    for sheet_int, sheet_name in enumerate(ex.sheet_names()):
        if '服务器' in sheet_name:
            ex = ExcelUtil(excel_path=excel_path_data, index=sheet_int)
            for token in ex.get_data():
                if 'web服务器' not in token and 'no' not in token:
                    print(token,3333333)
                    token.append(login_token(token[1]))
                    server_ip.append(token)
    print(server_ip,44444444444444)
        # 添加token
        # 通过服务器的ip获取布控的视频
    for server_j in server_ip:
        for sheet_int, sheet_name in enumerate(ex.sheet_names()):
            if sheet_name == server_j[0]:
                ex = ExcelUtil(excel_path=excel_path_data, index=sheet_int)
                print(int(server_j[4]),666666666)
                if -1 == int(server_j[4]):
                    print(ex.get_data(),4444444)
                    print(len(ex.get_data()) - 1,33333333)
                    index1 = random.sample(range(1, len(ex.get_data())), len(ex.get_data()) - 1)
                else:
                    if int(server_j[4]) >= len(ex.get_data()):
                        print(len(ex.get_data()) - 1, 33333333)
                        index1 = random.sample(range(1, len(ex.get_data())), len(ex.get_data()) - 1)
                    else:
                        index1 = random.sample(range(1, len(ex.get_data())), int(server_j[4]))
                        print(sheet_int,server_j[4],index1, 1111111)
                        print(len(ex.get_data()) - 1, server_j[4], 22222223333333)
                for i, j in enumerate(ex.get_data()):
                    print(index1,444444555555555)
                    print(i, j, 222222222)
                    if 0 != i and i in index1:
                        j.append(sheet_int)
                        j.append(server_j[0])
                        j.append(server_j[1])
                        j.append(server_j[2])
                        j.append(server_j[3])
                        j.append(server_j[4])
                        j.append(server_j[5])
                        j.append(server_j[6])
                        at_v_list.append(j)
    concurrency = number
    delete_control = 'no'
    print('视频数量：', len(at_v_list), at_v_list)
    # 并发脚本
    for i_v in at_v_list:
        batch_atwork_vmr(i_v)
    synchronizing_camera(at_v_list[0][12], at_v_list[0][17])
    concurrency_number = []  # 并发的脚本
    integer = 0
    concurrency_int = int(concurrency)  # 并发数
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    for j_int, j in enumerate(at_v_list):
        concurrency_number.append(j)
        if len(concurrency_number) % concurrency_int == 0:
            jobs = []
            for i in concurrency_number:
                p = multiprocessing.Process(target=batch_atwork, args=(i, delete_control, return_dict))
                jobs.append(p)
                p.is_alive()
                p.start()
            for proc in jobs:
                proc.join()
            concurrency_number = []
            integer += 1
        # 当并发的数不足余数的时候，走下面的代码
        elif int(len(at_v_list) / concurrency_int) == integer and j_int+1 == len(at_v_list):
            print(f'不足{concurrency_int}，运行剩余')
            jobs = []
            for i in concurrency_number:
                p = multiprocessing.Process(target=batch_atwork, args=(i, delete_control, return_dict))
                jobs.append(p)
                p.is_alive()
                p.start()
            for proc in jobs:
                proc.join()
            concurrency_number = []
            integer += 1
    success_list = []
    fail_list = []
    not_video = []
    error_list = []
    for i in return_dict.values():
        if '测试通过' in i:
            success_list.append(i)
        elif '测试失败' in i:
            fail_list.append(i)
        elif '视频没有找到' in i:
            not_video.append(i)
        else:
            error_list.append(i)
    # print(f'测试通过{len(success_list)}条用例：', success_list)
    # print(f'测试失败{len(fail_list)}条用例', fail_list)
    # print(f'视频没有找到{len(not_video)}条用例', not_video)
    # print(f'出错{len(error_list)}条用例', error_list)
    # print(f'写入excel表格:{success_list+fail_list+not_video+error_list}', 'excel表格内容')
    data_list = success_list+fail_list+not_video+error_list
    case_list = []
    print(33334444442222222, data_list,33334444442222222)
    for j in data_list:
        print(len(j.split('---')), j, at_v_list, 111111111)
        str1 = ex.get_case_list(j, at_v_list)
        print(str1, 33344444444444444)
        print(j.split('---')[1], 55555555555)
        case_list.append(str1[0])
        case_list.append(str1[1])
        case_list.append(str1[2])
    print(case_list, 121231231231)
    date_time = ex.write_value(case_list)
    # print(f'时间是{date_time}')
    if carbon_copy == 'yes':
        mailto_list = [mailto, 'lizhen@supremind.com', 'yuwei@supremind.com', 'fanjiamin@supremind.com']
    elif carbon_copy == 'no':
        mailto_list = [mailto, 'zhulijun@supremind.com']
    # print(mailto_list,888888899999999999)
    mail_title = 'Hey subject'
    mail_content = '结束结果'
    file_path = '%s测试结果.xls' % date_time
    mm = Mailer(mailto_list, mail_title, mail_content, file_path)
    res = mm.sendMail()
    print(res)