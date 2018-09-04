import requests
from bs4 import BeautifulSoup
import datetime

url = 'https://ssgfoodingplus.com/fmn101.do?goTo=todayMenuJson'
today = datetime.datetime.now().strftime("%Y-%m-%d")
payloads = {"storeCd": "05600", "cafeCd": "01", "menuDate": today}
res = requests.post(url, data= payloads).json()
for i in range(0,len(res['result'])):
    if res['result'][i]['meal_type_nm']=="조식":
        print(res['result'][i]['if_menu_nm'])
    elif res['result'][i]['meal_type_nm']=="중식":
        print(res['result'][i]['if_menu_nm'])
    elif res['result'][i]['meal_type_nm']=="석식":
        print(res['result'][i]['if_menu_nm'])
    