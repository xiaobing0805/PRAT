# -*- coding: utf-8 -*-

__author__ = "那天不蓝了"

"""

公众号: 读测优品

Email: 17765287025@163.com

"""

from flask import Blueprint
from flask_restful import Api


api_bp = Blueprint('api', __name__)
api = Api(api_bp)


from .auth import Auth
api.add_resource(Auth, "/auth/")

from .project import Project, ProjectList
api.add_resource(Project, "/project/")
api.add_resource(ProjectList, "/project_list/")

from .suite import Suite
api.add_resource(Suite, "/suite/")

from .case import Case, ManageFile
api.add_resource(Case, "/case/")
api.add_resource(ManageFile, "/manage_file/")

from .keyword import Keyword
api.add_resource(Keyword, "/keyword/")

from .task import Task, TaskList
api.add_resource(Task, "/task/")
api.add_resource(TaskList, "/task_list/")


from .user import User
api.add_resource(User, "/user/")


from .settings import Settings
api.add_resource(Settings, "/settings/")
