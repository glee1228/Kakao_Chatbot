import requests
from bs4 import BeautifulSoup
import datetime

url = "https://bds.bablabs.com/restaurants?campus_id=3hXYy5crHG"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
#print(result)
bab_tag = result.select('ul > li > div > div > a > img ')
r = datetime.datetime.today().weekday()
days=["월","화","수","목","금","토","일"]
#imgs = bab_tag.get('src')
print(bab_tag[0]['src'])

