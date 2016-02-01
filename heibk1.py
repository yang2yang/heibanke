# encoding: UTF-8
import requests
import re


raw_url = 'http://www.heibanke.com/lesson/crawler_ex00/'
response = requests.get(raw_url)

# print response.content

pattern = re.compile(r'.+输入.*数字\D*(\d+)..+')

num = pattern.search(response.content)

if num:
    print "It is a beatiful line!"
    print num.group(1)

url = raw_url + num.group(1)
# print url

response = requests.get(url)
# print response.content
num = pattern.search(response.content)

while num:
    print num.group(0)
    print num.group(1)
    url = raw_url + num.group(1)
    print url
    response = requests.get(url)
    num = pattern.search(response.content)


print "ok"
