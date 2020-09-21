import os
import re

import pytest
import requests


@pytest.fixture(scope='session')
def test_case(request):
    """
    测试用例生成处理
    :param request:
    :return:
    """
    var = request.config.getoption("--rootdir")
    test_file = request.config.getoption("--tf")
    env = request.config.getoption("--te")
    cases = []
    if test_file:
        cases = [test_file]
    else:
        if os.path.isdir(var):
            for root, dirs, files in os.walk(var):
                if re.match(r'\w+', root):
                    if files:
                        cases.extend([os.path.join(root, file) for file in files if file.endswith('yml')])
    data = main(cases)

    content = """
import allure

from conftest import CaseMetaClass

@allure.feature('{}接口测试({}项目)')
class Test{}API(object, metaclass= CaseMetaClass):
    test_case_data = {}
"""
    test_case_files = []
    if os.path.isdir(var):
        for root, dirs, files in os.walk(var):
            if not ('.' in root or '__' in root):
                if files:
                    case_name = os.path.basename(root)
                    project_name = os.path.basename(os.path.dirname(root))
                    test_case_file = os.path.join(root, 'test_{}.py'.format(case_name))
                    with open(test_case_file, 'w', encoding='utf-8') as fw:
                        fw.write(content.format(case_name, project_name, case_name.title(), data.get(root)))
    if test_file:
        temp = os.path.dirname(test_file)
        py_file = os.path.join(temp, 'test_{}.py'.format(os.path.basename(temp)))
    else:
        py_file = var

    pytest.main([
        '-v',
        py_file,
        '--alluredir',
        'report',
        '--te',
        env,
        '--capture',
        'no',
        '--disable-warnings',
    ])

    for file in test_case_files:
        os.remove(file)
    return test_case_files