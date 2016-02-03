# encoding: UTF-8
import requests

raw_url = 'http://www.heibanke.com/lesson/crawler_ex02/'
login_url = 'http://www.heibanke.com/accounts/login'
# cookies = {"csrftoken":"TU2E3HRpVcWIbVLcUr88ySzSSUyLrSoB"}
cookies1 = {"sessionid":"19l7r6arrifpt5m6yehh5yl1dok56512","Hm_lvt_74e694103cf02b31b28db0a346da0b6b":"1454330919,1454414156,1454503690,1454506527","Hm_lpvt_74e694103cf02b31b28db0a346da0b6b":"1454512824","csrftoken":"wpeKyEIIQby5U5lJ6x7SgIslN49lw9Yc"}
# cookies2 = {"Hm_lvt_74e694103cf02b31b28db0a346da0b6b":"1454330919,1454414156,1454503690,1454506527","Hm_lpvt_74e694103cf02b31b28db0a346da0b6b":"1454512824","csrftoken":"wpeKyEIIQby5U5lJ6x7SgIslN49lw9Yc"}
password = 1

# requests.get()
while password < 2:
    req_data3 = {"csrfmiddlewaretoken":"wpeKyEIIQby5U5lJ6x7SgIslN49lw9Yc", "username":"aaa","password":str(password)}
    print req_data3
    s = requests.Session()
    response = s.post(raw_url, data=req_data3, cookies=cookies1)
    # 经过多次的cookies的实验，发现sessionid这个属性决定是否是登陆的状态，而Hm_1vt和Hm_1pv这两个属性决定是否会出现CSRF错误
    password += 1
    print response.content

# 第二次尝试，先进入登陆页面进行session对象的登陆，在使用同一个页面进行用户名和密码的尝试，但是最后显示CSRF不正确。
# form_data = {"csrfmiddlewaretoken":"TU2E3HRpVcWIbVLcUr88ySzSSUyLrSoB","username":"yang2yang","password":"d197753119"}
# s = requests.Session()
# response = s.post(login_url, cookies=cookies, data=form_data)
# print response.content
#
# req_data3 = {"csrfmiddlewaretoken": "wpeKyEIIQby5U5lJ6x7SgIslN49lw9Yc", "username": "aaa", "password":str(password)}
# print req_data3
# response = s.post(raw_url, cookies=cookies1, data=req_data3)
# print response.content
