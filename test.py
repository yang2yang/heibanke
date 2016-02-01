# encoding: UTF-8
import requests
import re

text = "<h3>下一个你需要输入的数字是36752. 还有一大波数字马上就要到来...</h3>"

pattern = re.compile(r'.+输入.*数字\D*(\d+)..+')
num = pattern.search(text)

print "hello"
print num.group(0)
print num.group(1)
