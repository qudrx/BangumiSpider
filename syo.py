import requests
from bs4 import BeautifulSoup
import re
import datetime
from TranMod import FanyiSpider
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

st_front = "https://ncode.syosetu.com/"
#st_back = input()
# st_back = "n2273dh/"
st_back = "n8440fe/"
st = st_front + st_back

# response = requests.get(st)
# response.encoding = response.apparent_encoding
# soup = BeautifulSoup(response.text, 'html.parser')

def getHtmlList(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/51.0.2704.63 Safari/537.36'}
        r = requests.get(url, headers = headers, timeout = 30)
        # r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("")


response = getHtmlList(st)
soup = BeautifulSoup(response, 'html.parser')
# print(soup)
Novel = soup.find("div", {'id': 'novel_contents'})
Tran = FanyiSpider()

Novel_title = Novel.find("p", {'class': 'novel_title'}).text.strip()
print(Novel_title)
print()

Novel_writer = Novel.find("div", {'class': 'novel_writername'}).find('a')
Novel_writer_name = Novel_writer.text
Novel_writer_web = Novel_writer.attrs.get('href')
print(Novel_writer_name)
print(Novel_writer_web)
print()

# Novel_intro = Novle.find("div", {'id', 'novel_ex'})
pa = re.compile('(?s)<div id="novel_ex">(.*?)</div>')
Novel_intro = str(re.findall(pa, response)[0]).replace('<br />', '')
print(Novel_intro)
print()
Novel_intro_list = Novel_intro.split('\n')
for i in Novel_intro_list:
    print(i)
    print(Tran.paragraph_translate(i, from_='jp', to='zh'))






#A
#策略：直接给出地址，把机翻过的东西存下来，网址去原地址里爬
#优点：简单，实现简单
#缺点：无法实现中文的替换
#改进型：我先将网页save到服务器，挂载到自己的域名下的Temp Address，然后修改网页，再机翻

#B
#策略：直接原始网页将东西分类并爬下来，然后用selenium来实现机翻
#优点：替换方便
#缺点：相对稍微繁琐


print('\n---------爬取结束---------\n')
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('爬取完成时间： ' + now_time)