import requests
import unittest
from  mysql_action import DB
import yaml
import logging

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users'
        self.auth=('51zxw','zxw20182018')


    def test_001_get_user(self):
        logging.info('test_001_get_user')
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],'sutune')
        self.assertEqual(result['email'],'sutune@163.com')

    def test_002_add_user(self):
        logging.info('test_002_add_user')
        form_data={'username':'zxw666','email':'zxw666@163.com','groups':'http://127.0.0.1:8000/groups/2/'}
        r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],'zxw666')
        self.assertEqual(result['email'],'zxw666@163.com')

    #
    def test_003_update_user(self):
        logging.info('test_003_update_user')
        form_data={'email':'zxw2018@163.com'}
        r=requests.patch(self.base_url+'/1/',data=form_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['email'],'zxw2018@163.com')

    def test_004_delete_user(self):
        logging.info('test_004_delete_user')
        r=requests.delete(self.base_url+'/2/',auth=self.auth)

        self.assertEqual(r.status_code,204)

    def test_005_no_auth(self):
        logging.info('test_005_no_auth')
        r=requests.get(self.base_url)
        result=r.json()

        self.assertEqual(result['detail'],'Authentication credentials were not provided.')


class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/groups'
        self.auth=('51zxw','zxw20182018')


    def test_001_group_developer(self):
        logging.info('test_001_group_developer')
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Developer')

    def test_002_add_group(self):
        logging.info('test_002_add_group')
        form_data={'name':'Pm'}
        r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Pm')

    def test_003_update_group(self):
        logging.info('test_003_update_group')
        form_data={'name':'Boss'}
        r=requests.patch(self.base_url+'/2/',data=form_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Boss')

    def test_004_delete_group(self):
        logging.info('test_004_delete_group')
        r=requests.delete(self.base_url+'/1/',auth=self.auth)
        self.assertEqual(r.status_code,204)

if __name__ == '__main__':
    db=DB()
    f=open('datas.yaml','r')
    datas=yaml.load(f)
    db.init_data(datas)
    unittest.main()
