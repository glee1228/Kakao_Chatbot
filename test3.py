import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
star_tag = result.select('div.star_t1 > a > span.num')
print(len(star_tag))