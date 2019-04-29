import requests
from bs4 import BeautifulSoup
import uuid


reponse = requests.get(url="https://www.autohome.com.cn/news/")
reponse.encoding = reponse.apparent_encoding

soup = BeautifulSoup(reponse.text,'html.parser')
target = soup.find(id="auto-channel-lazyload-article")
li_list = target.find_all('li')
for li in li_list:
    a_tag = li.find('a')
    if a_tag:
        href = a_tag.attrs.get("href")
        title = a_tag.find("h3").text
        img_src = "http:"+a_tag.find("img").attrs.get('src')
        print(href)
        print(title)
        print(img_src)
        # img_reponse = requests.get(url=img_src)
        # file_name = str(uuid.uuid4())+'.jpg'
        # with open(file_name,'wb') as fp:
        #     fp.write(img_reponse.content)