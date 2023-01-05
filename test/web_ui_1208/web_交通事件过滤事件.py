#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/12/2 16:55
# @Author   : qh
# @Email    : 867075698@qq.com
# @File     : web_交通事件过滤事件.py
# @Software : PyCharm


# 针对过滤事件
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time
from web_ui_1208 import do_excel


import logging
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] '
                           '- %(levelname)s: %(message)s',level=logging.INFO)

texts = do_excel.test_key()
# print(texts)

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 15)

new_url = 'http://10.19.0.11'


def login():
    try:
        browser.get('http://10.19.0.11:10107/cas/login?service=http://10.19.0.11:10280/?appCode=console')
        browser.maximize_window()
        input_username = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        input_username.send_keys('admin')
        input_password = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        input_password.send_keys('Supremind0717')

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
    guo_lv = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="105$Menu"]/li[8]/div[1]/span[2]')
    ))
    guo_lv.click()

    time.sleep(2)
    ji_dong = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="105$Menu"]/li[1]/div/span[2]')
    ))
    ji_dong.click()

    # 点击过滤列表-交通事件
    time.sleep(2)
    ji_tongs = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="1040$Menu"]/li[4]/span[2]')
    ))
    ji_tongs.click()

    browser.refresh()
    time.sleep(5)
    zha_kai = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[contains(text(), "展开")]')))
    zha_kai.click()

    # 选择时间
    # 点击开始时间框
    time.sleep(3)
    start_time = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="eventTimes"]')
    ))
    start_time.click()

    # 选择12.09日
    time.sleep(3)
    click_query_time = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="ant-picker-date-panel"]//table[@class="ant-picker-content"]/tbody/tr[2]/td[5]')
    ))
    click_query_time.click()

    # 点击开始时间确定
    time.sleep(2)
    click_start_time = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="ant-picker-footer"]/ul[@class="ant-picker-ranges"]//button')
    ))
    click_start_time.click()

    # 选择12.09日
    time.sleep(2)
    click_querys_time = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="ant-picker-date-panel"]//table[@class="ant-picker-content"]/tbody/tr[2]/td[5]')
    ))
    click_querys_time.click()

    # 点击结束时间确定
    time.sleep(2)
    click_end_time = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="ant-picker-footer"]/ul[@class="ant-picker-ranges"]//button')
    ))
    click_end_time.click()

    time.sleep(2)
    logging.info("===【开始测试】====")
    for i in texts:
        input_task_id = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="taskId"]')
        ))
        input_task_id.send_keys(i)

        # 点击查询
        select_task = wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             '//*[@id="root"]//*[@class="ant-row ant-row-start"]/div[last()]'
             '//*[@class="ant-space-item"]/div/div[2]/button')))
        select_task.click()

        time.sleep(1)
        one_times = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@class="index_funcGroup__3zZ-Z"]/div[@class="index_bigLayoutRow__1v09i"]//div[4]//span')
        )).text
        time.sleep(1)
        if int(one_times) != 0:
            time_out = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@class="ant-spin-nested-loading"]//*[@class="ant-row"]/div[last()]'
                           '//*[@class="ant-descriptions-view"]//tr[4]//span[2]/span')
            ))
            if time_out.text:
                print(f'任务编号:{i} 第一次预警事件时间：{time_out.text}'[-8:])
        elif int(one_times) == 0:
            print('没有触发预警事件')
        else:
            print('其他异常报错')

        input_task_id.send_keys(Keys.CONTROL, "a")
        input_task_id.send_keys(Keys.DELETE)
        time.sleep(0.5)
    browser.quit()
    logging.info("===【结束测试】===")


login()
click_test()
