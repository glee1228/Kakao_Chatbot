import requests
from bs4 import BeautifulSoup
import datetime

url = "https://bds.bablabs.com/restaurants/MjMyOTIzNjAw?campus_id=3hXYy5crHG"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
#print(result)
bab_tag = result.select('div.card-body.store-card-menu-body > div > ul > li > div')
weekday_tag = result.select('div > div > h6')
wd = weekday_tag[0].text
r = datetime.datetime.today().weekday()
days=["월","화","수","목","금","토","일"]
if days[r] in wd :
    if days[r] == "월":
        print("-------조식---------")
        print(bab_tag[r].text)
        print("-------중식---------")
        print(bab_tag[r+1].text)
        print("-------석식---------")
        print(bab_tag[r+2].text)
        print("----------------")
    if days[r] == "화":
        print("-------조식---------")
        print(bab_tag[r+2].text)
        print("-------중식---------")
        print(bab_tag[r+3].text)
        print("-------석식---------")
        print(bab_tag[r+4].text)
        print("----------------")
    if days[r] == "수":
        print("-------조식---------")
        print(bab_tag[r+4].text)
        print("-------중식---------")
        print(bab_tag[r+5].text)
        print("-------석식---------")
        print(bab_tag[r+6].text)
        print("----------------")
    if days[r] == "목":
        print("-------조식---------")
        print(bab_tag[r+6].text)
        print("-------중식---------")
        print(bab_tag[r+7].text)
        print("-------석식---------")
        print(bab_tag[r+8].text)
        print("----------------")
    if days[r] == "금":
        print("-------조식---------")
        print(bab_tag[r+8].text)
        print("-------중식---------")
        print(bab_tag[r+9].text)
        print("-------석식---------")
        print(bab_tag[r+10].text)
        print("----------------")
else:
    print("오늘 날짜와 맞는 식단이 없습니다.")