import requests
from bs4 import BeautifulSoup
import datetime
import re
 
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
if hour>=15:
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
print(return_msg)