from api.get_token import GetToken
from testcses.test_base import TestBase


class TestToken(TestBase):

    # def setup(self):
    #     self.gettoken = GetToken()

    def test_get_token(self):
        print(self.gettoken.get_token().json())
        assert self.gettoken.get_token().json()["code"] == 0


    def test_get_xxx(self):
        self.gettoken