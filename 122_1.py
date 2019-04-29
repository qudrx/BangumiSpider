import requests
from bs4 import BeautifulSoup
import time

stt = "http://bangumi.tv/anime/browser?sort=rank&page="

# for num in range(1, 624):
for num in range(1, 2):
    st = stt + str(num)
    response = requests.get(st)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    target = soup.find(id="browserItemList")
    li_list = target.find_all('li')
    for li in li_list:
        a_tag = li.find('a')
        b_tag = li.find('div')
        if b_tag:
            title_zh = b_tag.find("a").text
            title_jp = b_tag.find("small").text
            rank = b_tag.find("span").text
            information = b_tag.find("p").text
            score = b_tag.find("p", {'class': 'rateInfo'}).text
            print(title_zh)
            print(title_jp)
            print(rank)
            print(information[26:])
            print(score[2:-1])

        if a_tag:
            href = "http://bangumi.tv/" + a_tag.attrs.get("href")
            img_src = a_tag.find("img").attrs.get("src")
            print(href)
            print(img_src[2:] + "\n")
            # img_reponse = requests.get(url=img_src)
            # file_name = str(uuid.uuid4())+'.jpg
            # with open(file_name,'wb') as fp:
            #     fp.write(img_reponse.content)
