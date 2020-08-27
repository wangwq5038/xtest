import yaml
import os
import requests
import pytest
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
yamlPath = os.path.join(fileNamePath,'jjmatchapi.yaml')
host = 'http://127.0.0.1:9999'
with open(yamlPath,'r',encoding='utf-8') as f:
    result = f.read()
    x = yaml.load(result,Loader=yaml.FullLoader)
    a = (x[0]['description'])
    b = (x[1]['description'])
url = host + x[0]['request']['uri']
headers = x[0]['request']['headers']
data = x[0]['request']['json']
method = x[0]['request']['method']
cookies = x[0]['request']['cookies']
res = requests.request(method=method,url=url,headers=headers,json=data,cookies=cookies)
if res.json()["code"] == 0:
    print("{}断言通过".format(a))
else:
    print("{}断言失败".format(a))
url = host + x[1]['request']['uri']
headers = x[1]['request']['headers']
method = x[1]['request']['method']
cookies = x[1]['request']['cookies']
res = requests.request(method=method,url=url,headers=headers,cookies=cookies)
if res.json()["code"] == 0:
    print("{}断言通过".format(b))
else:
    print("{}断言失败".format(b))

