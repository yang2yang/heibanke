# encoding: UTF-8
import requests

raw_url = 'http://www.heibanke.com/lesson/crawler_ex02/'
cookies = {"csrftoken":"TU2E3HRpVcWIbVLcUr88ySzSSUyLrSoB"}
password = 1
# requests.get()
while password < 2:
    req_data3 = {"csrfmiddlewaretoken":"TU2E3HRpVcWIbVLcUr88ySzSSUyLrSoB", "username":"aaa", "password":str(password)}
    print req_data3
    s = requests.Session()
    s.auth = ('yang2yang','d197753119')
    response = s.get(raw_url, data=req_data3, cookies = cookies) #md,注意这里变成的post，get和网页中的post，get的区别
    password += 1
    print response.content
