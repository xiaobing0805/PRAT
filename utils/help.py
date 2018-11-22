# -*- coding: utf-8 -*-

__author__ = "那天不蓝了"

"""

公众号: 读测优品

Email: 17765287025@163.com

"""

import codecs
import requests


def check_version():
    f = codecs.open('version.txt', 'r')
    version = f.readline()
    s = requests.Session()
    r_version = s.get("https://github.com/xiaobing0805/PRAT/blob/master/version.txt").text
    if version != r_version:
        print("*" * 25)
        print("本地版本：v%s" % version)
        print("github版本: v%s" % r_version)
        print("PRAT开源平台代码已有更新，请到下面的地址更新代码:")
        print("下载最新代码，直接覆盖本地即可")
        print("https://github.com/xiaobing0805/PRAT")
        print("*" * 25)
        exit(0)
    f.close()
