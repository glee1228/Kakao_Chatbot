import requests
from bs4 import BeautifulSoup
import datetime

url = 'http://pal.postech.ac.kr/Board.pal?top=6&sub=12&sub2=0&pageMode=pal&method=boardList&brd_id=pal_cafeteria'
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
bab_tag = result.select('table > tbody > tr')
brd_num = str(bab_tag[0]['brd_num'])
url2 = 'http://pal.postech.ac.kr/Board.pal?top=6&sub=12&sub2=0&method=boardView&pageMode=pal&mode=&brd_id=pal_cafeteria&brd_num={0}&currentPage=1&user_browser=msie_false&search_type=brd_subject&search_text=#'.format(brd_num)
res2 = requests.get(url2)
result2 = BeautifulSoup(res2.content,'html.parser')
bab_tag2 = result2.select('tr > td > p > img')

print(bab_tag2[0]['src'])
