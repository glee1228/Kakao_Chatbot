import requests
from bs4 import BeautifulSoup
import datetime

url = "https://ssgfoodingplus.com/fmn101.do?goTo=todayMenu&storeCd=05600"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
#print(result)
bab_tag = result.select('#menuForm > section > article > div.menu_info')
r = datetime.datetime.today().weekday()
days=["월","화","수","목","금","토","일"]
print(bab_tag)

