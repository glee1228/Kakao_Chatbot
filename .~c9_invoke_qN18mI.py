# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import random
import os
import requests
from bs4 import BeautifulSoup
import datetime
import re

app = Flask(__name__)
heroku =False

@app.route('/')
def hello():
    return "파이썬챗봇입니다"
@app.route('/keyboard')
def keyboard():
    keyboard =  {
    "type" : "buttons",
    "buttons" : ["메뉴추천","인재창조원식당","지곡회관(학생)","지곡회관(교직원)","지곡회관(푸드코트)","포항가속기연구소식당","RIST식당","영화추천"]}
    return jsonify(keyboard)
    
    
@app.route('/message',methods=['POST'])
def message():
    user_msg = request.json['content']
    img_bool = False
    if user_msg =="메뉴추천":
        menu =["RIST식당","학생회관식당","포항가속기연구소식당","RIST식당","지곡회관(학생)","지곡회관(교직원)","지곡회관(푸드코트)","학생회관매점","인재창조원식당"]
        return_msg = random.choice(menu)
    
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
        if hour>=14:
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
        return_msg = "지곡회관 학생식당/{0}요일\n-------조식-------\n{1}\n-------중식-------\n{2}\n-------석식-------\n{3}\n".format(days[r],bab_dict['breakfast'],bab_dict['lunch'],bab_dict['dinner'])
    elif user_msg =="지곡회관(교직원)":
        url = "http://fd.postech.ac.kr/bbs/board_menu.php?bo_table=weekly&sca=%EA%B5%90%EC%A7%81%EC%9B%90"
        res = requests.get(url)
        result = BeautifulSoup(res.content, 'html.parser')
        #print(result)
        bab_tag = result.select('td.pointer.txtheight')
        table_tag = result.select('table.list_td.tbl')
        bab_area = result.find("table",
        			{"class": "list_td"}
        	        ).find_all("td")
        r = datetime.datetime.today().weekday()
        hour = datetime.datetime.now().hour
        if hour>=14:
            if r==6:
                r=0
            else :
                r+=1
        days=["월","화","수","목","금","토","일"]
        bab_check=False
        return_msg=""
        #print("포스텍 학내에 식당은 지곡회관(프리덤, 위즈덤, 연지)과 학생회관(오아시스) 이외에 POSCO국제관(디메들리 뷔페, 피닉스 중식당), 포항가속기연구소, 포항산업과학연구원(RIST) 등에 위치하고 있습니다.")
        if days[r]=="토"or days[r]=="일":
            return_msg = "주말에는 교직원 식당을 운영하지 않습니다."
        else :
            for bab_index in bab_area:
                bab_tag=bab_index.text
                if bab_check==True:
                    bab_dict={}
                    bab_dict={
                            'lunch':bab_index.text
                        }
                    return_msg = "지곡회관 교직원식당/{0}요일\n-------중식-------\n{1}\n".format(days[r],bab_dict['lunch'])
                    break
                if "".join(re.findall(r"[월화수목금]+".format(days[r]), bab_tag))==days[r]:
                    bab_check=True
            if return_msg=="":
                return_msg="지곡회관(교직원식당)\n{0}요일의 식단 정보가 없습니다.".format(days[r])
    elif user_msg =="인재창조원식당":
        r = datetime.datetime.today().weekday()
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        days=["월","화","수","목","금","토","일"]
        if hour>=14:
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
            print(bab_tag)
            bab_list =bab_tag[2].text.split() #아침,한식, 3000원
            if bab_list[0]=="점심" :
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
        if hour>=14:
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
        
        today = yearmonth+str("%02d"%day)
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
    elif user_msg=='지곡회관(푸드코트)':
        preurl = "http://fd.postech.ac.kr/bbs/board.php?bo_table=food_court&page=1"
        res = requests.get(preurl)
        result = BeautifulSoup(res.content, 'html.parser')
        post_tag = result.select('table.board_list > tr > td')
        postnum = int(post_tag[0].text.split()[0])+2
        posturl = "http://fd.postech.ac.kr/bbs/board.php?bo_table=food_court&wr_id="
        url = posturl+str(postnum)+"&page=1"
        #print(url)
        res2 = requests.get(url)
        result2 = BeautifulSoup(res2.content, 'html.parser')
        bab_tag = result2.select('tbody > tr > td')
        r = datetime.datetime.today().weekday()
        hour = datetime.datetime.now().hour
        days=["월","화","수","목","금","토","일"]
        if hour>=14:
            if r==6:
                r=0
            else :
                r+=1
        mimi=[]
        ddungs=[]
        hansik=[]
        yangsik=[]
        
        
        ddungs_tag=bab_tag[7].text
        ddungs_menu=" ".join(re.findall(r"[가-힣0-9,]+", ddungs_tag))
        #print(ddungs_menu)
        
        hansik_breakfast_tag=bab_tag[8].text
        hansik_breakfast_menu=" ".join(re.findall(r"[가-힣0-9,(/)]+", hansik_breakfast_tag))
        #print(hansik_breakfast_menu)
        
        hansik_dinner_tag=bab_tag[12].text
        hansik_dinner_menu=" ".join(re.findall(r"[가-힣0-9,:(/)]+", hansik_dinner_tag))
        #print(hansik_dinner_menu)
        
        mimi_tag = bab_tag[11].text
        mimi_menu=" ".join(re.findall(r"[가-힣0-9,:()]+", mimi_tag))
        #print(mimi_menu)
        
        yangsik_tag = bab_tag[13].text
        yangsik_menu =" ".join(re.findall(r"[가-힣0-9,(/)]+",yangsik_tag))
        #print(yangsik_menu)
        
        bab_dict={
            'ddungs': ddungs_menu,
            'hansik_breakfast':hansik_breakfast_menu,
            'hansik_dinner':hansik_dinner_menu,
            'mimi':mimi_menu,
            'yangsik':yangsik_menu
        }
        
        return_msg = "지곡회관 푸드코트/{0}요일\n-------뚱스밥버거(조,중,석식)-------\n{1}\n-------한식(조식)-------\n{2}\n-------한식(중,석식)-------\n{3}\n-------미미짬뽕(중,석식)-------\n{4}\n-------양식(중,석식)-------\n{5}".format(days[r],bab_dict['ddungs'],bab_dict['hansik_breakfast'],bab_dict['hansik_dinner'],bab_dict['mimi'],bab_dict['yangsik'])

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
            "buttons" : ["메뉴추천","인재창조원식당","지곡회관(학생)","지곡회관(교직원)","지곡회관(푸드코트)","포항가속기연구소식당","RIST식당","영화추천"]
        }
        }
    else :
        return_json = {
        "message":{
            "text" : return_msg
        },
        "keyboard":{
            "type":"buttons",
            "buttons" : ["메뉴추천","인재창조원식당","지곡회관(학생)","지곡회관(교직원)","지곡회관(푸드코트)","포항가속기연구소식당","RIST식당","영화추천"]
        }
        }
    return jsonify(return_json)
    
app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))