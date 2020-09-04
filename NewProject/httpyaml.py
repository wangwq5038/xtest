# -*- encoding: utf-8 -*-
'''
@File    :   httpyaml.py
@Time    :   2020/08/31 10:18:00
@Author  :   wangwq 
@Version :   1.0
@Contact :   wangwq@mail.jj.cn
'''

# here put the import lib
#yaml测试文件自动生成

import re
import os
import sys

from requests import Session

template ="""
args:
  - {method}
  - {api}
kwargs:
  -
    caseName: {caseName}
    {data_or_params}:
        {data}
validator:
  -
    json:
      successed: True
"""


def auto_gen_cases(swagger_url, project_name):
    """
    根据swagger返回的json数据自动生成yml测试用例模板
    :param swagger_url:
    :param project_name:
    :return:
    """
    swagger_url = 'http://139.224.26.136:8081/swagger.json'
    res = Session().request('get', swagger_url).json()
    data = res.get('paths')

    workspace = os.getcwd()    #返回当前进程的工作目录

    project_ = os.path.join(workspace, project_name)

    if not os.path.exists(project_):
        os.mkdir(project_)

    for k, v in data.items():
        pa_res = re.split(r'[/]+', k)
        dir, *file = pa_res[1:]

        if file:
            file = ''.join([x.title() for x in file])
        else:
            file = dir

        file += '.yml'

        dirs = os.path.join(project_, dir)

        if not os.path.exists(dirs):
            os.mkdir(dirs)

        os.chdir(dirs)

        if len(v) > 1:
            v = {'post': v.get('post')}
        for _k, _v in v.items():
            method = _k
            api = k
            caseName = _v.get('description')
            data_or_params = 'params' if method == 'get' else 'data'
            parameters = _v.get('parameters')

            data_s = ''
            try:
                for each in parameters:
                    data_s += each.get('name')
                    data_s += ': \n'
                    data_s += ' ' * 8
            except TypeError:
                data_s += '{}'

        file_ = os.path.join(dirs, file)

        with open(file_, 'w', encoding='utf-8') as fw:
            fw.write(template.format(
                method=method,
                api=api,
                caseName=caseName,
                data_or_params=data_or_params,
                data=data_s
            ))

        os.chdir(project_)   #改变当前工作目录到指定的路径,指定到project_

# swagger_url = 'http://139.224.26.136:8081/swagger.json'
# res = Session().request('get', swagger_url).json()
# data = res.get('paths')
#
# workspace = os.getcwd()  #返回当前工作目录
#
# # project_ = os.path.join(workspace, project_name)   #路径拼接
#
# # if not os.path.exists(project_)   #判端括号内的路径是否存在
# #     os.mkdir(project_)
# for k, v in data.items():
#     # print(v)
#     print(v.get('parameters'))







