import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
title_tag = result.select('dt.tit > a')
star_tag = result.select('div.star_t1 > a > span.num')
reserve_tag = result.select('div.star_t1.b_star > span.num')
img_tag = result.select('div.thumb > a > img')
movie_dict={}

for i in range(0,10):
    movie_dict[i] = {
        
        'title':title_tag[i].text,
        'star' : star_tag[i].text,
        'reserve' : reserve_tag[i].text,
        'img' : img_tag[i]['src']
    }
