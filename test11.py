import requests
from bs4 import BeautifulSoup
import datetime

url = 'https://ssgfoodingplus.com/fmn101.do?goTo=todayMenuJson'
yearmonth = datetime.datetime.now().strftime("%Y-%m-")
now = datetime.datetime.now()
month = now.month
day = now.day
r = datetime.datetime.today().weekday()
hour = datetime.datetime.now().hour
if hour>=14:
    if r==6:
        r=0
    else :
        r+=1
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
        
today = yearmonth+str("%02d"%day)
print(today)
days=["월","화","수","목","금","토","일"]
payloads = {"storeCd": "05600", "cafeCd": "01", "menuDate" :today}
res = requests.post(url, data= payloads).json()
breakfast=""
lunch=""
dinner=""
for i in range(0,len(res['result'])):
    if res['result'][i]['meal_type_nm']=="조식":
        breakfast+=res['result'][i]['if_menu_nm']+"\n"
    elif res['result'][i]['meal_type_nm']=="중식":
        lunch+=res['result'][i]['if_menu_nm']+"\n"
    elif res['result'][i]['meal_type_nm']=="석식":
        dinner+=res['result'][i]['if_menu_nm']+"\n"
return_msg ="RIST식당/{0}요일\n-------조식-------\n{1}\n-------중식-------\n{2}\n-------석식-------\n{3}\n".format(days[r],breakfast,lunch,dinner)
print(return_msg)