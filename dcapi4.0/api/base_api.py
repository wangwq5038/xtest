import requests


class BaseApi:
    def requests_http(self, req):

        # r = requests.request(method="post", url="http://IP/admin/login",params={"name": self._name, "password": self._password})
        r = requests.request(**req)
        # print(r.json())
        return r





# if __name__ == '__main__':
#     ba = BaseApi()
#     ba.requests_http()