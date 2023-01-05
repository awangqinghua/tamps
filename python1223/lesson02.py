#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/12/23 10:06
# @Author   : wqh
# @Email    : 867075698@qq.com
# @File     : lesson02.py
# @Software : PyCharm


# 日期输入框操作

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.12306.cn/index/')
wait = WebDriverWait(browser, 15)

# 选择出发地-深圳
sz_js = 'var a = arguments[0]; a.readOnly=false;a.value="周口"'
sz = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//*[@id='fromStationText']")
))
browser.execute_script(sz_js, sz)

time.sleep(1)
# 选择结束地-上海
sh_js = 'var a = arguments[0]; a.readOnly=false;a.value="上海"'
sh = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//*[@id='toStationText']")
))
browser.execute_script(sh_js, sh)


# 选择日期
js = 'var a = arguments[0]; a.readOnly=false;a.value="\\2022-12-19\"'
WebDriverWait(browser, 15).until(EC.visibility_of_element_located(
    (By.XPATH, "//*[@id='train_date']")
))


browser.execute_script(js, loc)  # 执行


# now_10="2022-12-23"
# browser.execute_script('var a = arguments[0]; a.readOnly=false;a.value=arguments[1]', loc, now_10)


time.sleep(1)
# 点击查询
cha_xun = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="search_one"]')
))
cha_xun.click()
