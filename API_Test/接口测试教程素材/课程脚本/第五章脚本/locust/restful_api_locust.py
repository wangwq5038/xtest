from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):
    @task(2)
    def test_users(self):
        self.client.get('/users/',auth=('51zxw','zxw20182018'))

    @task(1)
    def test_groups(self):
        self.client.get('/groups/',auth=('51zxw','zxw20182018'))

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000