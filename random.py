# -*-coding:utf-8-*
#
# import random
from urllib import *
url = 'http://www.baidu.com'
req = request(url)
response =urlopen(req)
html = response.read