import requests
from bs4 import BeautifulSoup
import datetime

url = "http://fd.postech.ac.kr/bbs/board_menu.php?bo_table=weekly&sca=%EA%B5%90%EC%A7%81%EC%9B%90"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
#print(result)
bab_tag = result.select('td.pointer.txtheight')
r = datetime.datetime.today().weekday()
days=["월","화","수","목","금","토","일"]
list1=["월","수","금","일"]
list2=["화","목","토"]
print("포스텍 학내에 식당은 지곡회관(프리덤, 위즈덤, 연지)과 학생회관(오아시스) 이외에 POSCO국제관(디메들리 뷔페, 피닉스 중식당), 포항가속기연구소, 포항산업과학연구원(RIST) 등에 위치하고 있습니다.")
print("-----교직원식당-----")
print(days[r])
print("운영시간 : 11:50 ~ 13:00")
print("------------------")
if days[r] in "월":
    print(bab_tag[r].text)
elif days[r] in "화":
    print(bab_tag[r].text)
elif days[r] in "수":
    print(bab_tag[r].text)
elif days[r] in "목":
    print(bab_tag[r].text)
elif days[r] in "금":
    print(bab_tag[r].text)
elif days[r] in "토":
    print(bab_tag[r].text)
elif days[r] in "일":
    print(bab_tag[r].text)


