# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import random
import os
import requests
from bs4 import BeautifulSoup
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return "파이썬챗봇입니다"
@app.route('/keyboard')
def keyboard():
    keyboard =  {
    "type" : "buttons",
    "buttons" : ["메뉴추천","인재창조원식당","학생식당","교직원식당","포항가속기연구소식당","RIST식당","로또뽑기","영화추천"]}
    return jsonify(keyboard)
    
    
@app.route('/message',methods=['POST'])
def message():
    user_msg = request.json['content']
    img_bool = False
    if user_msg =="메뉴추천":
        menu =["RIST식당","학생회관식당","포항가속기연구소식당","RIST식당","학생식당","교직원식당","학생회관매점","인재창조원식당"]
        return_msg = random.choice(menu)
        
    elif user_msg =="로또뽑기":
        numbers = list(range(1,46))
        pick = random.sample(numbers,6)
        return_msg = str(sorted(pick))
    
    elif user_msg =="영화추천":
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
        
    elif user_msg =="학생식당":
        url = "http://fd.postech.ac.kr/bbs/board_menu.php?bo_table=weekly&sca=%ED%95%99%EC%83%9D"
        res = requests.get(url)
        result = BeautifulSoup(res.content, 'html.parser')
        #print(result)
        bab_tag = result.select('td.pointer.txtheight')
        day_tag = result.select('td.bg1')
        day_tag2 = result.select('td.bg0')
        
        r = datetime.datetime.today().weekday()
        days=["월","화","수","목","금","토","일"]
        list1=["월","수","금","일"]
        list2=["화","목","토"]
        bab_dict={}
        if days[r] in list1:
            if days[r] == "월":
                bab_dict ={
                'breakfast' : bab_tag[r].text,
                'lunch' : bab_tag[r+1].text,
                'dinner' : bab_tag[r+2].text
                }
            elif days[r] == "수":
                bab_dict ={
                'breakfast': bab_tag[r+5].text,
                'lunch':bab_tag[r+6].text,
                'dinner':bab_tag[r+7].text
                }
            elif days[r] == "금":
                bab_dict ={
                'breakfast': bab_tag[r+10].text,
                'lunch':bab_tag[r+11].text,
                'dinner':bab_tag[r+12].text
                }
            elif days[r] == "일":
                bab_dict ={
                'breakfast': bab_tag[r+15].text,
                'lunch':bab_tag[r+16].text,
                'dinner':bab_tag[r+17].text
                }
        if days[r] in list2:
            if days[r] == "화":
                bab_dict ={
                'breakfast': bab_tag[r+3].text,
                'lunch' : bab_tag[r+4].text,
                'dinner' : bab_tag[r+5].text
                }
            elif days[r] == "목":
                bab_dict ={
                'breakfast': bab_tag[r+8].text,
                'lunch':bab_tag[r+9].text,
                'dinner':bab_tag[r+10].text
                }
            elif days[r] == "토":
                bab_dict ={
                'breakfast': bab_tag[r+13].text,
                'lunch':bab_tag[r+14].text,
                'dinner':bab_tag[r+15].text
                }
        return_msg = "학생식당/{0}요일\n-------조식-------\n{1}\n-------중식-------\n{2}\n-------석식-------\n{3}\n".format(days[r],bab_dict['breakfast'],bab_dict['lunch'],bab_dict['dinner'])
    elif user_msg =="교직원식당":
        url = "http://fd.postech.ac.kr/bbs/board_menu.php?bo_table=weekly&sca=%EA%B5%90%EC%A7%81%EC%9B%90"
        res = requests.get(url)
        result = BeautifulSoup(res.content, 'html.parser')
        #print(result)
        bab_tag = result.select('td.pointer.txtheight')
        r = datetime.datetime.today().weekday()
        days=["월","화","수","목","금","토","일"]
        list1=["월","수","금","일"]
        list2=["화","목","토"]
        #print("포스텍 학내에 식당은 지곡회관(프리덤, 위즈덤, 연지)과 학생회관(오아시스) 이외에 POSCO국제관(디메들리 뷔페, 피닉스 중식당), 포항가속기연구소, 포항산업과학연구원(RIST) 등에 위치하고 있습니다.")
        bab_dict={}
        bab_dict={
                'lunch':bab_tag[r].text
            }
        return_msg = "교직원식당/{0}요일\n-------중식-------\n{1}\n".format(days[r],bab_dict['lunch'])
    elif user_msg =="인재창조원식당":
        url = "https://bds.bablabs.com/restaurants/MjMyOTIzNjAw?campus_id=3hXYy5crHG"
        res = requests.get(url)
        result = BeautifulSoup(res.content, 'html.parser')
        #print(result)
        bab_tag = result.select('div.card-body.store-card-menu-body > div > ul > li > div')
        r = datetime.datetime.today().weekday()
        days=["월","화","수","목","금","토","일"]
        bab_dict={}
        if days[r] == "월":
                bab_dict ={
                'breakfast' : bab_tag[r].text,
                'lunch' : bab_tag[r+1].text,
                'dinner' : bab_tag[r+2].text
                }
        if days[r] == "화":
                bab_dict ={
                'breakfast' : bab_tag[r+2].text,
                'lunch' : bab_tag[r+3].text,
                'dinner' : bab_tag[r+4].text
                }
        if days[r] == "수":
                bab_dict ={
                'breakfast' : bab_tag[r+4].text,
                'lunch' : bab_tag[r+5].text,
                'dinner' : bab_tag[r+6].text
                }
        if days[r] == "목":
                bab_dict ={
                'breakfast' : bab_tag[r+6].text,
                'lunch' : bab_tag[r+7].text,
                'dinner' : bab_tag[r+8].text
                }
        if days[r] == "금":
                bab_dict ={
                'breakfast' : bab_tag[r+8].text,
                'lunch' : bab_tag[r+9].text,
                'dinner' : bab_tag[r+10].text
                }
        return_msg = "인재창조원식당/{0}요일\n-------조식-------\n{1}\n-------중식-------\n{2}\n-------석식-------\n{3}\n".format(days[r],bab_dict['breakfast'],bab_dict['lunch'],bab_dict['dinner'])
    elif user_msg =="포항가속기연구소식당":
        url = "https://bds.bablabs.com/restaurants?campus_id=3hXYy5crHG"
        res = requests.get(url)
        result = BeautifulSoup(res.content, 'html.parser')
        bab_tag = result.select('ul > li > div > div > a > img ')
        bab_src = bab_tag[0]['src']
        return_msg = bab_src
    elif user_msg =="RIST식당":
        return_msg ="https://ssgfoodingplus.com/fmn101.do?goTo=todayMenu&storeCd=05600"
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
            "buttons" : ["메뉴추천","인재창조원식당","학생식당","교직원식당","포항가속기연구소식당","RIST식당","로또뽑기","영화추천"]
        }
        }
    else :
        return_json = {
        "message":{
            "text" : return_msg
        },
        "keyboard":{
            "type":"buttons",
            "buttons" : ["메뉴추천","인재창조원식당","학생식당","교직원식당","포항가속기연구소식당","RIST식당","로또뽑기","영화추천"]
        }
        }
    return jsonify(return_json)
    
app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))