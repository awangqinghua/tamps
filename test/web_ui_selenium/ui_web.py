#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/7/11 14:56
# @Author :wangqinghua
# @File : ui_web.py
# @Software : PyCharm


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 15)


def login():
    browser.get('http://10.5.1.156:10107/cas/login?service=http://10.5.1.156:10280/?appCode=console')
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


def click_test():
    try:
        ji_shu_input = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mainRoot"]//ul//*[contains(text(), "技术服务")]')))
        ji_shu_input.click()

        time.sleep(2)
        fei_wef = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[contains(text(), "非机动车违法")]')))
        fei_wef.click()
        time.sleep(6)
        yu_ji = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="/main/svc/events/fjdc/tag/normal$Menu"]//span[contains(text(), "预警列表")]')
        ))
        yu_ji.click()
        zha_kai = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[contains(text(), "展开")]')))
        zha_kai.click()

        time.sleep(1)
        start_time = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="eventTimes"]')
        ))
        start_time.click()

        click_start_time = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//td[@title='2022-07-12' "
                       "and @class='ant-picker-cell ant-picker-cell-in-view ant-picker-cell-in-range']")
        ))
        click_start_time.click()
        confirm = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-sm"]')
        ))
        confirm.click()
        time.sleep(2)
        click_end_time = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//td[@title="2022-07-12"]')
        ))
        click_end_time.click()

        time.sleep(2)
        confirms = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-sm"]')
        ))
        confirms.click()

        input_task_id = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//input[@id="taskId"]')
        ))
        input_task_id.send_keys("fjdc_1000_bqk3eeylknb4")
        time.sleep(2)
        select_task = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[contains(text(), "查 询")]')))
        select_task.click()
    except TimeoutException:
        click_test()


def get_detail(html):
    time.sleep(5)
    soup = BeautifulSoup(html, 'lxml')
    res = soup.find('div', attrs={'class_': 'ant-spin-container'})
    row = res.find('div', attrs={'class_': 'ant-row'})

    pass


login()
click_test()


