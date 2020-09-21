import os

from aiohttp import ClientSession

from readyaml import yaml_load


async def entrace(test_cases, loop, semaphore=None):
    """
    http执行入口
    :param test_cases:
    :param semaphore:
    :return:
    """
    res = BXMDict()
    # 在CookieJar的update_cookies方法中，如果unsafe=False并且访问的是IP地址，客户端是不会更新cookie信息
    # 这就导致session不能正确处理登录态的问题
    # 所以这里使用的cookie_jar参数使用手动生成的CookieJar对象，并将其unsafe设置为True
    async with ClientSession(loop=loop, cookie_jar=CookieJar(unsafe=True), headers={'token': bxmat.token}) as session:
        await advertise_cms_login(session)
        if semaphore:     #计数信号量
            async with semaphore:
                for test_case in test_cases:
                    data = await one(session, case_name=test_case)
                    res.setdefault(data.pop('case_dir'), BXMList()).append(data)
        else:
            for test_case in test_cases:
                data = await one(session, case_name=test_case)
                res.setdefault(data.pop('case_dir'), BXMList()).append(data)

        return res


async def one(session, case_dir='', case_name=''):
    """
    一份测试用例执行的全过程，包括读取.yml测试用例，执行http请求，返回请求结果
    所有操作都是异步非阻塞的
    :param session: session会话
    :param case_dir: 用例目录
    :param case_name: 用例名称
    :return:
    """
    project_name = case_name.split(os.sep)[1]
    domain = bxmat.url.get(project_name)
    test_data = await yaml_load(dir=case_dir, file=case_name)
    result = BXMDict({
        'case_dir': os.path.dirname(case_name),
        'api': test_data.args[1].replace('/', '_'),
    })
    if isinstance(test_data.kwargs, list):
        for index, each_data in enumerate(test_data.kwargs):
            step_name = each_data.pop('caseName')
            r = await http(session, domain, *test_data.args, **each_data)
            r.update({'case_name': step_name})
            result.setdefault('responses', BXMList()).append({
                'response': r,
                'validator': test_data.validator[index]
            })
    else:
        step_name = test_data.kwargs.pop('caseName')
        r = await http(session, domain, *test_data.args, **test_data.kwargs)
        r.update({'case_name': step_name})
        result.setdefault('responses', BXMList()).append({
            'response': r,
            'validator': test_data.validator
        })

    return result