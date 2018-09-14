import requests
from bs4 import BeautifulSoup
import datetime

url = "https://bds.bablabs.com/restaurants?campus_id=3hXYy5crHG"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
bab_tag = result.select('ul > li > div > div > a > img ')
print(bab_tag)
if not bab_tag:
    print("없음")
else :
    print("있음")
#print(bab_tag[0]['src'])

