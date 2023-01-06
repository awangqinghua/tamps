#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/1/5 20:24
# @Author   : wqh
# @Email    : 867075698@qq.com
# @File     : lesson04.py
# @Software : PyCharm


# 导入Flask类
from flask import Flask

# Flask函数接收一个参数__name__，它会指向程序所在的包

app = Flask(__name__)


# 装饰器的作用是将路由映射到视图函数 index
@app.route('/')
def index():
    return 'Hello World XiaoMing'


# Flask应用程序实例的 run 方法 启动 WEB 服务器

if __name__ == '__main__':
    # app.run()  # 可以指定运行的主机IP地址，端口，是否开启调试模式
    app.run(host="0.0.0.0", port=8888, debug=True)
