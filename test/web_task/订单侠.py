#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/8/11 19:39
# @Author :wangqinghua
# @File : 订单侠.py
# @Software : PyCharm



#提前登录一次再关闭页面操作

from selenium import webdriver
import time

url = 'https://www.dingdanxia.com/user/login/index.html'
driver = webdriver.Chrome()
driver.get(url)

# 添加Cookie
# 将 fiddler 中抓到的 cookie 放到对应值中
driver.add_cookie({'name': 'PHPSESSID', 'value': '0r9b2ajh54j2rlvt24q8q1suup'})


# 刷新页面
driver.refresh()

driver.implicitly_wait(3)

# 如果不加cookie 执行该步操作，则会提示登录
# driver.find_element_by_xpath('//*[@id="index-page"]/body/div[2]/div/div[2]/form/button').click()

time.sleep(5)
driver.quit()