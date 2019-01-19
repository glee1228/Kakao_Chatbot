import requests
from bs4 import BeautifulSoup
import datetime

url = "http://fd.postech.ac.kr/bbs/board_menu.php?bo_table=weekly&sca=%ED%95%99%EC%83%9D"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
print(result)
bab_tag = result.select('td.pointer.txtheight')
day_tag = result.select('td.bg1')
day_tag2 = result.select('td.bg0')

r = datetime.datetime.today().weekday()
hour = datetime.datetime.now().hour
if hour>=14:
    if r==6:
        r=0
    else :
        r+=1

days=["월","화","수","목","금","토","일"]
list1=["월","수","금","일"]
list2=["화","목","토"]
bab_dict={}
print(bab_tag)
if days[r] in list1:
    if days[r] == "월":
        bab_dict ={
            'breakfast' : bab_tag[r].text,
            'lunch' : bab_tag[r+1].text,
            'dinner' : bab_tag[r+2].text
            }
    elif days[r] == "수":
        bab_dict ={
        'breakfast': bab_tag[r+4].text,
        'lunch':bab_tag[r+5].text,
        'dinner':bab_tag[r+6].text
        }
    elif days[r] == "금":
        bab_dict ={
        'breakfast': bab_tag[r+8].text,
        'lunch':bab_tag[r+9].text,
        'dinner':bab_tag[r+10].text
        }
    elif days[r] == "일":
        bab_dict ={
        'breakfast': bab_tag[r+12].text,
        'lunch':bab_tag[r+13].text,
        'dinner':bab_tag[r+14].text
        }
if days[r] in list2:
    if days[r] == "화":
        bab_dict ={
        'breakfast': bab_tag[r+2].text,
        'lunch' : bab_tag[r+3].text,
        'dinner' : bab_tag[r+4].text
        }
    elif days[r] == "목":
        bab_dict ={
        'breakfast': bab_tag[r+6].text,
        'lunch':bab_tag[r+7].text,
        'dinner':bab_tag[r+8].text
        }
    elif days[r] == "토":
        bab_dict ={
        'breakfast': bab_tag[r+10].text,
        'lunch':bab_tag[r+11].text,
        'dinner':bab_tag[r+12].text
        }
return_msg = "지곡회관 학생식당/{0}요일\n-------조식-------\n{1}\n-------중식-------\n{2}\n-------석식-------\n{3}\n".format(days[r],bab_dict['breakfast'],bab_dict['lunch'],bab_dict['dinner'])
#print(return_msg)