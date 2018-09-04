import requests
from bs4 import BeautifulSoup
import datetime

url = "https://bds.bablabs.com/restaurants/MjMyOTIzNjAw?campus_id=3hXYy5crHG"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
#print(result)
bab_tag = result.select('div.card-body.store-card-menu-body > div > ul > li > div')
r = datetime.datetime.today().weekday()
days=["월","화","수","목","금","토","일"]
print("포스텍 학내에 식당은 지곡회관(프리덤, 위즈덤, 연지)과 학생회관(오아시스) 이외에 POSCO국제관(디메들리 뷔페, 피닉스 중식당), 포항가속기연구소, 포항산업과학연구원(RIST) 등에 위치하고 있습니다.")
print("-----인재개발원식당-----")
print(days[r])
print("운영시간 : ")
print("------------------")
#012/345/678/91011/121314
#0/1/2/3/4
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