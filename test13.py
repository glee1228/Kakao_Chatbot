from urllib.request import FancyURLopener

class AppURLopener(FancyURLopener):     			 
   	version = "Mozilla/5.0"

default_agent = FancyURLopener().version
changed_agent = AppURLopener().version
print(default_agent,"->",changed_agent)
url = "http://fd.postech.ac.kr/bbs/board_menu.php?bo_table=weekly&sca=%EA%B5%90%EC%A7%81%EC%9B%90"
html = AppURLopener().open(url) 
print(html)