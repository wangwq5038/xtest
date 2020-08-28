# -*- encoding: utf-8 -*-
'''
@File    :   readyaml.py
@Time    :   2020/08/28 16:00:48
@Author  :   wangwq 
@Version :   1.0
@Contact :   wangwq@mail.jj.cn
'''

# here put the import lib
"""
异步读取文件可以使用aiofiles这个第三方库，yaml_load是一个协程，
可以保证主进程读取yaml测试用例时不被阻塞，
通过await yaml_load()便能获取测试用例的数据

可以看到，测试用例还支持一定的模板语法，如${function}、$(a:b)等，
这能在很大程度上拓展测试人员用例编写的能力
"""
import os
import aiofiles
import yaml
import re
async def yaml_load(dir='',file=''):
    """
    异步读取yaml文件，并转译其中的特殊值
    :param file:
    :return:
    """

    if dir:
        file = os.path.join(dir,file)
    async with aiofiles.open(file,'r',encoding='utf-8',errors='ignore') as f:
        data = await f.read()

    data = yaml.load(data)

    # 匹配函数调用形式的语法
    pattern_function = re.compile(r'^\${([A-Za-z_]+\w*\(.*\))}$')
    pattern_function2 = re.compile(r'^\${(.*)}$')
    # 匹配取默认值的语法
    pattern_function3 = re.compile(r'^\$\((.*)\)$')


    def my_iter(data):
        """
        递归测试用例，根据不同数据类型做相应处理，将模板语法转化为正常值
        :param data:
        :return:
        """
        if isinstance(data,(list,tuple)):
            for index, _data in enumerate(data):
                data[index] = my_iter(_data) or _data
        elif isinstance(data,dict):
            for k,v in data.items():
                data[k] = my_iter(v) or v
        elif isinstance(data,(str,bytes)):
            m = pattern_function.match(data)
            if not m:
                m = pattern_function2.match(data)
            if m:
                return eval(m.group(1))
            if not m:
                m = pattern_function3.match(data)
            if m:
                k, k = m.group(1).split(':')
                return bxmat.default_values.get(k).get(k)
            return data
    my_iter(data)
    return BXMDict(data)

