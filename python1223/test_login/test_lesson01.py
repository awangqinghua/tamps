#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/1/3 17:04
# @Author   : wqh
# @Email    : 867075698@qq.com
# @File     : test_lesson01.py
# @Software : PyCharm


import pytest


@pytest.mark.smoke
def test_api():
    # print("ggg")
    assert "123" == "123"


@pytest.mark.smokes
def test_apis():
    assert "123" == "123"


@pytest.mark.smok
def test_aping():
    assert "123" == "123"


@pytest.mark.regress
class TestApi:
    def test_bbb(self):
        assert "word" == "word"

    def test_bba(self):
        assert "word" == "word"

    def test_bbc(self):
        assert "wos" == "wos"


if __name__ == '__main__':

    pytest.main(["-m", "regress", "-s", "-v"])
