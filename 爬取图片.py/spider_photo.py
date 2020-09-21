# -*- encoding: utf-8 -*-
'''
@File    :   spider_photo.py
@Time    :   2020/08/06 20:08:52
@Author  :   wangwq 
@Version :   1.0
@Contact :   wangwq@mail.jj.cn
'''

# here put the import lib
#爬取WEB页面图片，天气网

import urllib
import urllib.request
import re

def load_page(url):
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    data=response.read()
    return  data

def get_image(html):
    regx=r'http://[\S]*jpg'
    pattern=re.compile(regx)
    get_image=re.findall(pattern,repr(html))

    num=1
    for img in  get_image:
        image=load_page(img)
        with open('E:\\Photo\\%s.jpg' %num,'wb') as fb:
            fb.write(image)
            print("正在下载第%s张图片" %num)
            num=num+1
    print("下载完成！")

url='http://p.weather.com.cn/2017/06/2720826.shtml#p=7'
html=load_page(url)
get_image(html)