# encoding: UTF-8
import requests

raw_url = 'http://www.heibanke.com/lesson/crawler_ex02/'
password = 1

while password < 31:
    print password
    print str(password)
    # req_data = "csrfmiddlewaretoken=R9EqJQQNDZZC4gpthRKWZMQ6FB6hc5DI&username=aaa&password=" + passwd
    # req_data2 = 'csrfmiddlewaretoken=R9EqJQQNDZZC4gpthRKWZMQ6FB6hc5DI&username=aaa&password=11'
    req_data3 = {"csrfmiddlewaretoken":"R9EqJQQNDZZC4gpthRKWZMQ6FB6hc5DI", "username":"aaa", "password":str(password)}
    print req_data3
    response = requests.post(raw_url, data=req_data3) #md,注意这里变成的post，get和网页中的post，get的区别
    # get好像不能够发送表单数据，但是post可以发送表单数据 看来并不是这样，get和post都是可选data的，但是还是有点小问题在。
    password += 1
    print response.content
