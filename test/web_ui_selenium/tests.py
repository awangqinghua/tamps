#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/11/30 9:38
# @Author   : qh
# @Email    : 867075698@qq.com
# @File     : tests.py
# @Software : PyCharm


# def f1():
#     n = 999
#
#     def f2():
#         print(n)
#
#     return f2
#
#
# result = f1()
# result()


# def fun(n):
#     if n == 1:
#         return 1
#     else:
#         return n + fun(n - 1)
    # 5+f(4)
    # f(4)=4+f(3)
    # f(3)=3+f(2)
    # f(2)=2+f(1)
    # f(1)=1
    # 5+4+3+2+1

# result=fun(5)
# print(result)

# print(5+(5-1)+(5-2)+(5-3)+(5-4))

# num=0
# for i in range(1, 6):
#     num+=i
# print(num)
import time

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from time import sleep
#
# url = 'https://www.baidu.com/'
# driver = webdriver.Chrome()
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(10)
# # 鼠标悬停至设置链接
# link = driver.find_element_by_id("s-usersetting-top")
# ActionChains(driver).move_to_element(link).perform()
#
# driver.find_element_by_link_text('搜索设置').click()
#
# # 保存设置
# driver.find_element_by_class_name('prefpanelgo').click()
# sleep(2)
# # 接受警告框
# driver.switch_to_alert().accept()
#
# driver.quit()

from selenium import webdriver
import time

# 浏览器无头模式配置，无界面模式，减少浏览器的渲染
# options = webdriver.ChromeOptions()
# options.headless = True
#
# browser = webdriver.Chrome(options=options)
# browser.implicitly_wait(10)
#
#
# browser.get("http://www.baidu.com")
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="kw"]').send_keys("python自动化")
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="su"]').click()
# time.sleep(2)
# print(browser.title)
# browser.quit()



# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome()
# wait = WebDriverWait(browser, 15)
# browser.maximize_window()
# browser.get("http://100.100.152.116:10281/")
# # browser.set_window_size(1500, 500)  # 设置浏览器窗口大小
#
# username = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="username"]')))
# username.send_keys("admin")
#
# password = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="password"]')))
# password.send_keys("smai123")
#
# su = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//button[@type="submit"]')))
# su.click()
#
#
# time.sleep(5)
# lu_kou = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="main_layout"]/main/main/div/form/div/div[1]/div/div[2]/div/div/div/div[1]/span[1]')))
#
# lu_kou.click()
#
# time.sleep(1)
# chang_jiang = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="main_layout"]/main/main/div/form/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/'
#                'div/div[2]/div/div/div/div[2]/div')
# ))
# chang_jiang.click()
#
# time.sleep(2)
# start_date = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="dataDate"]')
# ))
# start_date.click()
#
# start_dates = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="main_layout"]/main/main/div/form/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/'
#                'div[1]/div/div[2]/table/tbody/tr[4]/td[4]')
# ))
# start_dates.click()
#
# end_time = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="main_layout"]/main/main/div/form/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/'
#                'div[1]/div/div[2]/table/tbody/tr[4]/td[4]')
# ))
# end_time.click()
#
# submit = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="main_layout"]/main/main/div/form/div/div[4]/div/div[2]/button')
# ))
# submit.click()
#
#
# # 滚动到指定位置--不支持JS但是支持移动到指定位置
# time.sleep(2)
# loc = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="main_layout"]/main/main/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/label[2]/span[2]')))
# browser.execute_script('arguments[0].scrollIntoView(false);', loc)


