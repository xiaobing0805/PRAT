# -*- coding: utf-8 -*-

__author__ = "那天不蓝了"

"""

公众号: 读测优品

Email: 17765287025@163.com

"""


class AutoBeatException(Exception):
    pass


class AutoBeatConfigException(AutoBeatException):
    pass


class AutoBeatExecutorTimeout(AutoBeatException):
    pass


class AutoBeatTaskTimeout(AutoBeatException):
    pass


class AutoBeatWebServerTimeout(AutoBeatException):
    pass


class AutoBeatSkipException(AutoBeatException):
    pass
