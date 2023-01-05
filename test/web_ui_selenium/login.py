#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/12/16 15:54
# @Author   : wqh
# @Email    : 867075698@qq.com
# @File     : login.py
# @Software : PyCharm


from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.implicitly_wait(10)
browser.get('http://100.100.152.116:10281/')
browser.find_element_by_id("username").send_keys('admin')
browser.find_element_by_id("password").send_keys('smai123')
browser.find_element_by_xpath('//*[@id="rc-tabs-0-panel-acountLogin"]/form/div[3]/div/div/div/button').click()

time.sleep(3)
browser.find_element_by_xpath('//*[@id="root"]/section/aside/div/ul/li[4]/div/span/span/span[2]').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="root"]//li//*[contains(text(), "流量态势")]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="rc_select_2"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main_layout"]/main/main/div/div[1]/form/div/div/div[2]'
                              '/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div').click()

time.sleep(1)
browser.find_element_by_xpath('//*[@class="ant-row"]//button[@class="ant-btn ant-btn-primary"]').click()
