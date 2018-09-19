# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import random
import os
import requests
from bs4 import BeautifulSoup
import datetime

app = Flask(__name__)
heroku =False

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
        
    elif user_msg =="지곡회관(학생)":
        url = "http://fd.postech.ac.kr/bbs/board_menu.php?bo_table=weekly&sca=%ED%95%99%EC%83%9D"
        res = requests.get(url)
        result = BeautifulSoup(res.content, 'html.parser')
        #print(result)
        bab_tag = result.select('td.pointer.txtheight')
        day_tag = result.select('td.bg1')
        day_tag2 = result.select('td.bg0')
        
        r = datetime.datetime.today().weekday()
        hour = datetime.datetime.now().hour
        if hour>=15:
            if r==6:
                r=0
            else :
                r+=1
        
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
                'breakfast': bab_tag[r+4].text,
                'lunch':bab_tag[r+5].text,
                'dinner':bab_tag[r+6].text
                }
            elif days[r] == "금":
                bab_dict ={
                'breakfast': bab_tag[r+8].text,
                'lunch':bab_tag[r+9].text,
                'dinner':bab_tag[r+10].text
                }
            elif days[r] == "일":
                bab_dict ={
                'breakfast': bab_tag[r+12].text,
                'lunch':bab_tag[r+13].text,
                'dinner':bab_tag[r+14].text
                }
        if days[r] in list2:
            if days[r] == "화":
                bab_dict ={
                'breakfast': bab_tag[r+2].text,
                'lunch' : bab_tag[r+3].text,
                'dinner' : bab_tag[r+4].text
                }
            elif days[r] == "목":
                bab_dict ={
                'breakfast': bab_tag[r+6].text,
                'lunch':bab_tag[r+7].text,
                'dinner':bab_tag[r+8].text
                }
            elif days[r] == "토":
                bab_dict ={
                'breakfast': bab_tag[r+10].text,
                'lunch':bab_tag[r+11].text,
                'dinner':bab_tag[r+12].text
                }
        return_msg = "지고학생식당/{0}요일\n-------조식-------\n{1}\n-------중식-------\n{2}\n-------석식-------\n{3}\n".format(days[r],bab_dict['breakfast'],bab_dict['lunch'],bab_dict['dinner'])
    elif user_msg =="교직원식당":
        url = "http://fd.postech.ac.kr/bbs/board_menu.php?bo_table=weekly&sca=%EA%B5%90%EC%A7%81%EC%9B%90"
        res = requests.get(url)
        result = BeautifulSoup(res.content, 'html.parser')
        #print(result)
        bab_tag = result.select('td.pointer.txtheight')
        r = datetime.datetime.today().weekday()
        hour = datetime.datetime.now().hour
        if hour>=15:
            if r==6:
                r=0
            else :
                r+=1
        
        days=["월","화","수","목","금","토","일"]
        list1=["월","수","금","일"]
        list2=["화","목","토"]
        #print("포스텍 학내에 식당은 지곡회관(프리덤, 위즈덤, 연지)과 학생회관(오아시스) 이외에 POSCO국제관(디메들리 뷔페, 피닉스 중식당), 포항가속기연구소, 포항산업과학연구원(RIST) 등에 위치하고 있습니다.")
        if days[r]=="토"or days[r]=="일":
            return_msg = "주말에는 교직원 식당을 운영하지 않습니다."
        else :
            bab_dict={}
            bab_dict={
                    'lunch':bab_tag[r].text
                }
            return_msg = "교직원식당/{0}요일\n-------중식-------\n{1}\n".format(days[r],bab_dict['lunch'])
    elif user_msg =="인재창조원식당":
        r = datetime.datetime.today().weekday()
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        days=["월","화","수","목","금","토","일"]
        if hour>=15:
            if r==6:
                r=0
            else :
                r+=1
            if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                if day==31:
                    month+=1
                    day=1
                else:
                    day+=1
            else:
                if day==30:
                    month+=1
                    day=1
                else :
                    day+=1
        
                    
        if days[r]=="토" or days[r]=="일":
            return_msg = "주말에는 인재창조원 식당을 운영하지않습니다."
        else : 
            url = "https://www.poswel.co.kr/fmenu/three_days.php?area_code=A4&"
            payloads = "nyear=%d&nmonth=%02d&reqday=%02d"%(year,month,day)
            url = url+payloads
            print(url)
            res = requests.get(url)
            result = BeautifulSoup(res.content, 'html.parser')
            bab_tag = result.select('strong.blue')
            bab2_tag = result.select('div.list_3day_menu_tit_explain > span')
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            
            bab_list =bab_tag[3].text.split() #아침,한식, 3000원
            if bab_list[0]=="저녁" :
                bab_dict={}
                bab_dict ={
                    'breakfast' : bab2_tag[0].text,
                    'lunch' : bab2_tag[2].text,
                    'lunch2' : bab2_tag[4].text,
                    'dinner' : bab2_tag[6].text
                    }
                return_msg = "인재창조원식당/{0}요일\n-------조식-------\n{1}\n-------중식1-------\n{2}\n-------중식2-------\n{3}\n-------석식-------\n{4}\n".format(days[r],bab_dict['breakfast'],bab_dict['lunch'],bab_dict['lunch2'],bab_dict['dinner'])
            else :
                bab_dict={}
                bab_dict ={
                    'breakfast' : bab2_tag[0].text,
                    'lunch' : bab2_tag[2].text,    
                    'dinner' : bab2_tag[4].text
                    }
                return_msg = "인재창조원식당/{0}요일\n-------조식-------\n{1}\n-------중식-------\n{2}\n-------석식-------\n{3}\n".format(days[r],bab_dict['breakfast'],bab_dict['lunch'],bab_dict['dinner'])
    elif user_msg =="포항가속기연구소식당":
        url = "https://bds.bablabs.com/restaurants?campus_id=3hXYy5crHG"
        res = requests.get(url)
        result = BeautifulSoup(res.content, 'html.parser')
        bab_tag = result.select('ul > li > div > div > a > img ')
        if not bab_tag :
            return_msg = "식당에서 업데이트한 식단이 없습니다"
        else :
            bab_src = bab_tag[0]['src']
            return_msg = bab_src
    elif user_msg =="RIST식당":
        url = 'https://ssgfoodingplus.com/fmn101.do?goTo=todayMenuJson'
        yearmonth = datetime.datetime.now().strftime("%Y-%m-")
        now = datetime.datetime.now()
        month = now.month
        day = now.day
        r = datetime.datetime.today().weekday()
        hour = datetime.datetime.now().hour
        if hour>=15:
            if r==6:
                r=0
            else :
                r+=1
            if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                if day==31:
                    month+=1
                    day=1
                else:
                    day+=1
            else:
                if day==30:
                    month+=1
                    day=1
                else :
                    day+=1
        
        today = yearmonth+str(day)
        days=["월","화","수","목","금","토","일"]
        payloads = {"storeCd": "05600", "cafeCd": "01", "menuDate": today}
        res = requests.post(url, data= payloads).json()
        breakfast=""
        lunch=""
        dinner=""
        for i in range(0,len(res['result'])):
            if res['result'][i]['meal_type_nm']=="조식":
                breakfast+=res['result'][i]['if_menu_nm']+"\n"
            elif res['result'][i]['meal_type_nm']=="중식":
                lunch+=res['result'][i]['if_menu_nm']+"\n"
            elif res['result'][i]['meal_type_nm']=="석식":
                dinner+=res['result'][i]['if_menu_nm']+"\n"
        return_msg ="RIST식당/{0}요일\n-------조식-------\n{1}\n-------중식-------\n{2}\n-------석식-------\n{3}\n".format(days[r],breakfast,lunch,dinner)
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