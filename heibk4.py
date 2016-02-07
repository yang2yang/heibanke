import requests
import re

l = []
page = 1
while page < 14:
    # payload = {'page':'1'}
    page = str(page)
    print page
    raw_url = "http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page="
    url = raw_url + page
    print "raw_url",url
    cookies = {"sessionid":"5xd4dfd42f4fo9dvr2fhzrh3fg33udqn","Hm_lvt_74e694103cf02b31b28db0a346da0b6b":"1454414156,1454503690,1454506527,1454727366","Hm_lpvt_74e694103cf02b31b28db0a346da0b6b":"1454727504","csrftoken":"lLpuxx9PdWaN04Tzk45rHdytfInIVltc"}
    response = requests.get(url, cookies=cookies)
    print "response_url",response.url

    pattern = re.compile(r'password_pos\D+(\d+).+\n.+val\D+(\d+)')
    # match = pattern.search(response.content)
    # print match.group(1),match.group(2)
    match = pattern.findall(response.content)
    l += match
    page = int(page)
    page += 1

print l
