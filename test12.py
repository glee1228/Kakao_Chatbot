import requests
from bs4 import BeautifulSoup
import datetime

url = 'http://pal.postech.ac.kr/'
headers = {
    'Referer': 'http://pal.postech.ac.kr/Board.pal?top=6&sub=12&sub2=0&pageMode=pal&method=boardList&brd_id=pal_cafeteria',             # 네이버 크롤링 시, Referer 필수이기에 User-Agent 재선언
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'), 
     
}

yearmonth = datetime.datetime.now().strftime("%Y-%m-")
now = datetime.datetime.now()
month = now.month
day = now.day
r = datetime.datetime.today().weekday()
hour = datetime.datetime.now().hour

today = yearmonth+str("%02d"%day)
print(today)
days=["월","화","수","목","금","토","일"]
payloads = {"top": "6", "sub": "12", "sub2" :"0","method":"boardView"}

res = requests.get(url, headers = headers)
res2 = requests.post(res,data = payloads)
result = BeautifulSoup(res2, 'html.parser')
print(result)
