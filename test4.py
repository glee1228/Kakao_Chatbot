import requests
from bs4 import BeautifulSoup
import datetime

url = "http://fd.postech.ac.kr/bbs/board_menu.php?bo_table=weekly&sca=%ED%95%99%EC%83%9D"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
#print(result)
bab_tag = result.select('td.pointer.txtheight')
day_tag = result.select('td.bg1')
day_tag2 = result.select('td.bg0')

r = datetime.datetime.today().weekday()
days=["월","화","수","목","금","토","일"]
list1=["월","수","금","일"]
list2=["화","목","토"]
print("포스텍 학내에 식당은 지곡회관(프리덤, 위즈덤, 연지)과 학생회관(오아시스) 이외에 POSCO국제관(디메들리 뷔페, 피닉스 중식당), 포항가속기연구소, 포항산업과학연구원(RIST) 등에 위치하고 있습니다.")
print("-----학생식당-----")
print(days[r])
print("------------------")
print("운영 시간 :  조식(breakfast) 07:30 ~ 09:30	중식(lunch) 11:30 ~ 13:30	석식(dinner) 17:30 ~ 19:00")
if days[r] in list1:
    if days[r] == "월":
        print("-------조식---------")
        print(bab_tag[r].text)
        print("-------중식---------")
        print(bab_tag[r+1].text)
        print("-------석식---------")
        print(bab_tag[r+2].text)
        print("----------------")
    elif days[r] =="수":
        print("-------조식---------")
        print(bab_tag[r+5].text)
        print("-------중식---------")
        print(bab_tag[r+6].text)
        print("-------석식---------")
        print(bab_tag[r+7].text)
        print("----------------")
    elif days[r]=="금":
        print("-------조식---------")
        print(bab_tag[r+10].text)
        print("-------중식---------")
        print(bab_tag[r+11].text)
        print("-------석식---------")
        print(bab_tag[r+12].text)
        print("----------------")
    elif days[r] =="일":
        print("-------조식---------")
        print(bab_tag[r+15].text)
        print("-------중식---------")
        print(bab_tag[r+16].text)
        print("-------석식---------")
        print(bab_tag[r+17].text)
        print("----------------")
        
if days[r] in list2:
    if days[r] == "화":
        print("-------조식---------")
        print(bab_tag[r+3].text)
        print("-------중식---------")
        print(bab_tag[r+4].text)
        print("-------석식---------")
        print(bab_tag[r+5].text)
        print("----------------")
    elif days[r] =="목":
        print("-------조식---------")
        print(bab_tag[r+8].text)
        print("-------중식---------")
        print(bab_tag[r+9].text)
        print("-------석식---------")
        print(bab_tag[r+10].text)
        print("----------------")
    elif days[r]=="토":
        print("-------조식---------")
        print(bab_tag[r+13].text)
        print("-------중식---------")
        print(bab_tag[r+14].text)
        print("-------석식---------")
        print(bab_tag[r+15].text)
        print("----------------")
#012/678/121314/181920
#345/91011/151617
#day_tag2 화,목,토

