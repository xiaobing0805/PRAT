# -*- coding: utf-8 -*-

__author__ = "那天不蓝了"

"""

公众号: 读测优品

Email: 17765287025@163.com

"""


from flask_restful import Resource, reqparse

from utils.parsing import parser_robot_keyword_list


class Keyword(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('category', type=str)

    def get(self):
        args = self.parser.parse_args()
        if args["category"] == "robot":
            return parser_robot_keyword_list()
