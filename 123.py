import requests
from bs4 import BeautifulSoup
import time
import uuid
import re

response = requests.get("http://bangumi.tv/")
response.encoding = response.apparent_encoding
# response.encoding="utf-8"

# print(response.text)

s = response.text
pa = re.compile(r'"title">(.*?)</p>')
result = pa.findall(s)
print(result)

soup = BeautifulSoup(response.text,'html.parser')
# print(soup.prettify())

# time.sleep(2)


# target = soup.find(id="featuredItems")
# li_list = target.find_all('div')
# for li in li_list:
#     a_tag = li.find('a')
#     if a_tag:
#         href = "http://bangumi.tv/"+a_tag.attrs.get("href")
#         title = a_tag.attrs.get("title")
#         # img_src = a_tag.find("div").attrs.get("style")
#         print(href)
#         print(title)
#         # print(img_src)
#         # img_reponse = requests.get(url=img_src)
#         # file_name = str(uuid.uuid4())+'.jpg
#         # with open(file_name,'wb') as fp:
#         #     fp.write(img_reponse.content)