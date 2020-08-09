import unittest
import requests
from urllib import parse
from time import  sleep

class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url='https://www.sojson.com/open/api/weather/json.shtml'

    def test_weather_beijing(self):
        data={'city':'北京'}
        city=parse.urlencode(data).encode('utf-8')
        r=requests.get(self.url,params=city)
        result=r.json()

        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'Success!')
        self.assertEqual(result['city'],'北京')
        sleep(3)

    def test_weather_param_error(self):
        data={'city':'999'}
        r=requests.get(self.url,params=data)
        result=r.json()

        self.assertEqual(result['message'],'Check the parameters.')
        sleep(3)

    def test_weather_no_param(self):

        r=requests.get(self.url)
        result=r.json()

        self.assertEqual(result['message'],'Check the parameters.')
        self.assertEqual(result['status'],400)
        sleep(3)

if __name__ == '__main__':
    unittest.main()
