# -*- encoding: utf-8 -*-
'''
@File    :   http_requests.py
@Time    :   2020/08/31 09:43:51
@Author  :   wangwq 
@Version :   1.0
@Contact :   wangwq@mail.jj.cn
'''
import requests
# here put the import lib
"""
http请求测试接口
"""
async def http(domain, *args, **kwargs):
    """
    http请求处理器
    :param domain: 服务地址
    :param args:
    :param kwargs:
    :return:
    """
    method, api = args
    arguments = kwargs.get('data') or kwargs.get('params') or kwargs.get('json') or {}

    # kwargs中加入token
    kwargs.setdefault('headers', {}).update({'token': bxmat.token})
    # 拼接服务地址和api
    url = ''.join([domain, api])

    async with ClientSession() as session:       #引入session会话对象
        async with session.request(method, url, **kwargs) as response:
            res = await response_handler(response)
            return {
                'response': res,
                'url': url,
                'arguments': arguments
            }