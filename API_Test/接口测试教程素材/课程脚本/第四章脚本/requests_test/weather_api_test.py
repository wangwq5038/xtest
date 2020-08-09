import requests
from urllib import  parse

data={'city':'上海'}
city=parse.urlencode(data).encode('utf-8')
url='https://www.sojson.com/open/api/weather/json.shtml'

r=requests.get(url,params=city)
# print(r.text)
response_data=r.json()

print(response_data['date'])
print(response_data['message'])
print(response_data['status'])
print(response_data['city'])

print(response_data['data']['forecast'][0]['date'])
print(response_data['data']['forecast'][0]['type'])
print(response_data['data']['forecast'][0]['high'])
print(response_data['data']['forecast'][0]['low'])