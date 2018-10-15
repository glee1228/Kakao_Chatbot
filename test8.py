import requests
from bs4 import BeautifulSoup
import datetime

url = "https://bds.bablabs.com/restaurants?campus_id=3hXYy5crHG"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
bab_tag = result.select('ul > li > div > div > a > img ')
bab_tag2 = result.select('div.card.card-menu > div > div.card-text')
bab_url = bab_tag2[2].text
if bab_tag :
    bab_src = bab_tag[0]['src']
    return_msg = bab_src
elif bab_url :
    return_msg = bab_url
else :
    return_msg = "식당에서 업데이트한 식단이 없습니다"

print(return_msg)