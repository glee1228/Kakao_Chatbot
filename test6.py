# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import datetime
import re

url = "http://fd.postech.ac.kr/bbs/board_menu.php?bo_table=weekly&sca=%EA%B5%90%EC%A7%81%EC%9B%90"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
res = requests.get(url,headers=headers)
result = BeautifulSoup(res.content, 'html.parser')
print(result)
bab_tag = result.select('td.pointer.txtheight')
table_tag = result.select('table.list_td.tbl')
bab_area = result.find("table",
			{"class": "list_td"}
	        ).find_all("td")
r = datetime.datetime.today().weekday()
hour = datetime.datetime.now().hour
if hour>=14:
    if r==6:
        r=0
    else :
        r+=1
days=["월","화","수","목","금","토","일"]
bab_check=False
return_msg=""
#print("포스텍 학내에 식당은 지곡회관(프리덤, 위즈덤, 연지)과 학생회관(오아시스) 이외에 POSCO국제관(디메들리 뷔페, 피닉스 중식당), 포항가속기연구소, 포항산업과학연구원(RIST) 등에 위치하고 있습니다.")
if days[r]=="토"or days[r]=="일":
    return_msg = "주말에는 교직원 식당을 운영하지 않습니다."
else :
    for bab_index in bab_area:
        bab_tag=bab_index.text
        if bab_check==True:
            bab_dict={}
            bab_dict={
                    'lunch':bab_index.text
                }
            return_msg = "지곡회관 교직원식당/{0}요일\n-------중식-------\n{1}\n".format(days[r],bab_dict['lunch'])
            break
        if "".join(re.findall(r"[월화수목금]+".format(days[r]), bab_tag))==days[r]:
            bab_check=True
    if return_msg=="":
        return_msg="지곡회관(교직원식당) {0}의 식단 정보가 없습니다.".format(days[r])


