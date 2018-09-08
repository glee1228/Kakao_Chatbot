
import requests
from bs4 import BeautifulSoup
import datetime
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
if hour>=16:
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day==31:
            month+=1
            day=1
        else:
            day+=1
    else:
        if day==30:
            month+=1
            day=1
        else :
            day+=1
elif hour<6:
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day==1:
            month-=1
            day=31
        else:
            day-=1
    else:
        if day==1:
            month-=1
            day=30
        else :
            day-=1
url = "https://www.poswel.co.kr/fmenu/three_days.php?area_code=A4&"
payloads = "nyear=%d&nmonth=%02d&reqday=%02d"%(year,month,day)
url = url+payloads
print(url)
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
bab_tag = result.select('strong.blue')
bab2_tag = result.select('div.list_3day_menu_tit_explain > span')
r = datetime.datetime.today().weekday()
today = datetime.datetime.now().strftime("%Y-%m-%d")
days=["월","화","수","목","금","토","일"]
bab_list =bab_tag[3].text.split() #아침,한식, 3000원
if bab_list[0]=="저녁" :
    print("점심이 두개입니다")
else :
    print("점심이 한개입니다")

#print(bab_tag[0].text.split())
#print(bab_tag2)
print(today)