#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/8/11 9:12
# @Author :wqh
# @File : task.py
# @Software : PyCharm



# 预警列表
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 15)


def login():
    try:
        browser.get('http://10.19.0.11:10107/cas/login?service=http://10.19.0.11:10280/?appCode=console')
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
    try:
        ji_shu_input = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mainRoot"]//ul//*[contains(text(), "技术服务")]')))
        ji_shu_input.click()

        time.sleep(3)
        bu_kong=wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[contains(text(), "布控管理")]')
        ))
        bu_kong.click()

        time.sleep(3)
        ji_to=wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="115$Menu"]/li[1]/span[2]')
        ))
        ji_to.click()
        browser.refresh()
        time.sleep(5)

        task=wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[contains(text(), "新建任务")]')
        ))
        task.click()

        time.sleep(2)
        camera=wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="rc_select_0"]')
        ))
        camera.click()

        time.sleep(2)
        search_camera=wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//input[@class="ant-input ant-input-sm"]')
        ))
        search_camera.send_keys('行人闯入')

        time.sleep(2)
        search_task=wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//span[@class="ant-input-group-addon"]')
        ))
        search_task.click()

        time.sleep(3)
        select_pedestrian=wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@class="ant-tree-list-holder-inner"]/div[last()]')
        ))
        select_pedestrian.click()

        time.sleep(2)
        button_pedestrion=wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@class="ant-space ant-space-horizontal ant-space-align-end"]/div[last()]')
        ))
        button_pedestrion.click()

        time.sleep(3)
        draw=wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@class="ant-space-item"]/a//span')
        ))
        draw.click()

        # time.sleep(2)
        # pic=wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, '//*[@id="landmarkBox"]/div[@class="landmark drawing"]')
        # ))

        time.sleep(4)
        huizhi=wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[contains(text(), "绘制")]/following-sibling::div/div')
        ))
        huizhi.click()

    except TimeoutException:
        click_test()


login()
click_test()

