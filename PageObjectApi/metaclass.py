import pytest

function
_express = """
def {}(self, response, validata):
    with allure.step(response.pop('case_name')):
        validator(response, validata)
"""



class CaseMetaClass(type):
    """
    根据接口调用的结果自动生成测试用例
    """

    def __new__(cls, name, bases, attrs):
        test_cases_data = attrs.pop('test_case_data')
        for each in test_cases_data:
            api = each.pop('api')
            function_name = 'test' + api
            test_data = [tuple(x.values()) for x in each.get('response')]
            function = gen_function(function_express.format(function_name),
                                    namespance = {'validator': validator, 'allure': allure})

            #集成allure

            story_function = allure.story('{}'.format(api.replace('_', '/')))(function)
            attrs[function_name] = pytest.mark.parametrize('response, validata', test_data)(story_function)
        return  super().__new__(cls, name, bases, attrs)