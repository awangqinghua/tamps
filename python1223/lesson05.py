#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/1/6 17:01
# @Author   : wqh
# @Email    : 867075698@qq.com
# @File     : lesson05.py
# @Software : PyCharm


from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://10.19.0.14:10107/cas/login?service=http://10.19.0.14:10280/?appCode=console")
browser.maximize_window()
browser.implicitly_wait(10)

browser.find_element_by_id("username").send_keys("admin")
browser.find_element_by_id("password").send_keys("Supremind0717")
browser.find_element_by_name("submit").click()

# 点击技术服务
time.sleep(1)
browser.find_element_by_xpath('//*[@id="mainRoot"]/section/header/div[1]/ul/li[6]').click()

# 点击非机动车违法
time.sleep(1)
browser.find_element_by_xpath('//*[@id="105$Menu"]/li[2]').click()

# 点击预警列表
time.sleep(1)
browser.find_element_by_xpath('//*[@id="1033$Menu"]/li[1]').click()
time.sleep(1)
browser.refresh()

time.sleep(1)
res = browser.find_element_by_xpath('//*[@id="app_main_layout"]/main/div[2]/div[2]/div/div/div[1]/div/div')

# 点击事件中心
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="mainRoot"]/section/section/aside/div/ul/li[1]/div/span[2]').click()
#
# # 点击布控管理
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="mainRoot"]/section/section/aside/div/ul/li[4]/div[1]/span[2]').click()
#
# # 点击非机动车违法
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="115$Menu"]/li[2]/span[2]').click()
