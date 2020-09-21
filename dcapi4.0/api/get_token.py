from ruamel import yaml

from api.base_api import BaseApi
from string import Template

class GetToken(BaseApi):


    _name = "hhh"
    _password = "hhh123"
    def template(self):
        with open("../api/get_token.yml") as f:
            data = {
                "name": self._name,
                "password": self._password
            }
            re = Template(f.read()).substitute(data)
            return yaml.safe_load(re)
            # print(re)
            # print(f.read())
            # print((type(f.read())))


    def get_token(self):
        #把请求信息转化为一个规范的字典结构体
        # req = {
        #     "method": "post",
        #     "url": "http://IP/admin/login",
        #     "params":
        #         {
        #     "name": self._name,
        #     "password": self._password,
        # }
        # }
        # req = yaml.safe_load(open("../api/get_token.yml"))
        req = self.template()
        r = self.requests_http(req)
        # print(r.json())
        return r


# if __name__ == '__main__':
#     gt = GetToken()
#     gt.template()