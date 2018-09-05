
import requests
from bs4 import BeautifulSoup
import datetime

url = "https://www.poswel.co.kr/fmenu/three_days.php?area_code=A4&nyear=2018&nmonth=09&reqday=05"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
print(result)
#bab_tag = result.select('strong.font25')
r = datetime.datetime.today().weekday()
today = datetime.datetime.now().strftime("%Y-%m-%d")
days=["월","화","수","목","금","토","일"]
#print(bab_tag)
print(today)