# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import random
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello():
    return "파이썬챗봇입니다"
@app.route('/keyboard')
def keyboard():
    keyboard =  {
    "type" : "buttons",
    "buttons" : ["메뉴", "로또", "고양이","영화"]}
    return jsonify(keyboard)
    
    
@app.route('/message',methods=['POST'])
def message():
    user_msg = request.json['content']
    img_bool = False
    if user_msg =="메뉴":
        menu =["20층","멀캠식당","꼭대기","급식"]
        return_msg = random.choice(menu)
    elif user_msg =="로또":
        numbers = list(range(1,46))
        pick = random.sample(numbers,6)
        return_msg = str(sorted(pick))
    elif user_msg == "고양이":
        img_bool = True
        url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"
        res = requests.get(url).json()
        return_img = res[0]['url']
        return_msg = "야옹이다옹"
    elif user_msg =="영화":
        img_bool = True
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
        pick_movie = movie_dict[random.randrange(0,9)]
        return_msg = "%s/평점:%s/예매율:%s%% "% (pick_movie['title'],pick_movie['star'],pick_movie['reserve'])
        return_img = pick_movie['img']
    else :
        return_msg = "메뉴만 사용가능"
        
    if img_bool==True:
        img_bool=False
        return_json = {
        "message":{
            "text" : return_msg,
            "photo" : {
                "url": return_img,
                "height":630,
                "width":720
            }
        },
        "keyboard":{
            "type":"buttons",
            "buttons" :["메뉴","로또","고양이","영화"]
        }
        }
    else :
        return_json = {
        "message":{
            "text" : return_msg
        },
        "keyboard":{
            "type":"buttons",
            "buttons" :["메뉴","로또","고양이","영화"]
        }
        }
    return jsonify(return_json)
    
app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))