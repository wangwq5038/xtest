from api.get_token import GetToken


class TestBase:

    def setup(self):
        self.gettoken = GetToken()
