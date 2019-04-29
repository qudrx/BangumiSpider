import requests
from bs4 import BeautifulSoup

response = requests.get("http://bangumi.tv/anime/browser?sort=rank")
response.encoding = response.apparent_encoding
# response.encoding="utf-8"

# print(response.text)

# s = response.text
# pa = re.compile(r'"title">(.*?)</p>')
# result = pa.findall(s)
# print(result)

soup = BeautifulSoup(response.text,'html.parser')
# print(soup.prettify())

# gg = soup.find_all('img', {'class': 'cover'})
# # print(gg)
# list = []
# for i in gg:
#     list.append('http' + i['src'])
#
# for i in list:
#     print(i)


bac = "&page="
num = 2


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
        print(img_src[2:]+"\n")
        # img_reponse = requests.get(url=img_src)
        # file_name = str(uuid.uuid4())+'.jpg
        # with open(file_name,'wb') as fp:
        #     fp.write(img_reponse.content)
