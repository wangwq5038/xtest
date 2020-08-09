import requests
import unittest

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users'
        self.auth=('51zxw','zxw20182018')

    def test_get_user(self):
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],'51zxw')
        self.assertEqual(result['email'],'51zxw@163.com')

    # def test_add_user(self):
    #     form_data={'username':'zxw222','email':'zxw222@163.com','groups':'http://127.0.0.1:8000/groups/6/'}
    #     r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['username'],'zxw222')
    #     self.assertEqual(result['email'],'zxw222@163.com')

    #
    # def test_update_user(self):
    #     form_data={'email':'zxw2018@163.com'}
    #     r=requests.patch(self.base_url+'/6/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['email'],'zxw2018@163.com')

    # def test_delete_user(self):
    #     r=requests.delete(self.base_url+'/4/',auth=self.auth)
    #
    #     self.assertEqual(r.status_code,204)

    # def test_no_auth(self):
    #     r=requests.get(self.base_url)
    #     result=r.json()
    #
    #     self.assertEqual(result['detail'],'Authentication credentials were not provided.')


class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/groups'
        self.auth=('51zxw','zxw20182018')

    def test_group_developer(self):
        r=requests.get(self.base_url+'/7/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Developer')

    # def test_add_group(self):
    #     form_data={'name':'Pm'}
    #     r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['name'],'Pm')

    # def test_update_group(self):
    #     form_data={'name':'Boss'}
    #     r=requests.patch(self.base_url+'/6/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['name'],'Boss')

    # def test_delete_group(self):
    #     r=requests.delete(self.base_url+'/6/',auth=self.auth)
    #     self.assertEqual(r.status_code,204)

if __name__ == '__main__':
    unittest.main()
