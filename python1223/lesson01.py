#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/12/23 9:31
# @Author   : wqh
# @Email    : 867075698@qq.com
# @File     : lesson01.py
# @Software : PyCharm


# 预警列表
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time
# from web_ui_1206 import do_excel

import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] '
                           '- %(levelname)s: %(message)s', level=logging.INFO)

# texts = do_excel.test_key()
# print(texts)

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 15)

new_url = 'http://10.4.0.113'


def login():
    try:
        browser.get('http://47.97.184.108:10107/cas/login?service=http://47.97.184.108:10280/?appCode=console')
        browser.maximize_window()
        input_username = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        input_username.send_keys('admin')
        input_password = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        input_password.send_keys('smai123')

        browser_click = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#fm1 > input.btn.btn-block.btn-submit')))
        browser_click.click()

    except TimeoutException:
        login()


def click_test():
    ji_shu_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mainRoot"]//ul//*[contains(text(), "技术服务")]')))
    ji_shu_input.click()

    time.sleep(2)
    fei_jidong = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="/main/svc/events$Menu"]/li[4]/div[1]/span[2]')
    ))
    fei_jidong.click()

    browser.refresh()
    time.sleep(5)
    zha_kai = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[contains(text(), "展开")]')))
    zha_kai.click()

    time.sleep(1)
    js = 'var a = arguments[0]; a.readOnly=false;a.value="2022-12-19 17:00:00"'
    loc = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="eventTimes"]')
    ))

    browser.execute_script(js, loc)  # 执行，第一种写法

    time.sleep(1)

    js_end = 'var c = arguments[0]; c.readOnly=false;c.value="2022-12-19 17:05:00"'
    loc_end = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="app_main_layout"]/main/main/div[1]/form/div/div[3]/div/div[2]/div/div/div/div[3]/input')
    ))

    browser.execute_script(js_end, loc_end)  # 执行，第一种写法s

    time.sleep(10)
    # 点击查询
    select_task = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         '//*[@id="root"]//*[@class="ant-row ant-row-start"]/div[last()]'
         '//*[@class="ant-space-item"]/div/div[2]/button')))
    select_task.click()


# 开始测试
#     logging.info("===【开始测试】===")
#     for i in texts:
#         input_task_id = wait.until(EC.presence_of_element_located(
#             (By.XPATH, '//*[@id="taskId"]')
#         ))
#         input_task_id.send_keys(i)
#
#         # 点击查询
#         select_task = wait.until(EC.element_to_be_clickable(
#             (By.XPATH,
#              '//*[@id="root"]//*[@class="ant-row ant-row-start"]/div[last()]'
#              '//*[@class="ant-space-item"]/div/div[2]/button')))
#         select_task.click()
#
#         # 查看共N条
#         time.sleep(1)
#         one_times = wait.until(EC.presence_of_element_located(
#             (By.XPATH, '//*[@class="ant-layout-content"]//*[@class="index_funcGroup__3zZ-Z"]/div/div/span')
#         )).text
#         time.sleep(1)
#         if int(one_times) != 0:
#             time_out = wait.until(EC.presence_of_element_located(
#                 (By.XPATH, '//*[@class="ant-spin-nested-loading"]//*[@class="ant-row"]/div[last()]'
#                            '//*[@class="ant-descriptions-view"]//tr[3]//span[2]/span')
#             ))
#             if time_out.text:
#                 print(f'任务编号:{i} 第一次预警事件时间：{time_out.text}'[-8:])
#         elif int(one_times) == 0:
#             print('')
#         else:
#             print('没找到')
#         input_task_id.send_keys(Keys.CONTROL, "a")
#         input_task_id.send_keys(Keys.DELETE)
#         time.sleep(0.5)
#     browser.quit()
#     # 结束测试
#     logging.info("===【结束测试】===")


login()
click_test()
