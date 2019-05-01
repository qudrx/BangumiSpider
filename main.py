import requests
from bs4 import BeautifulSoup
import re
import uuid
import sys
import datetime


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

st_f = "http://bangumi.tv/subject/"
st_b = "216371"
st = st_f + st_b

sys.stdout = Logger("content/" + st_b + ".txt")

response = requests.get(st)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, 'html.parser')

# 2019.4.16 14:55 /280709
# print(soup.prettify())
# pa = re.compile('^(?!class=).*$')
pa = re.compile('<a href="(.*?)" class="l"><span>(.*?)</span>')
paa = re.compile('(?s)<div id="subject_summary" class="subject_summary" property="v:summary">(.*?)</div>')

# print(li_list)
# print('\n')

s = response.text
res = re.findall(paa, s)
resLab = re.findall(pa, s)
ss = str(res[0])
ss = ss.replace('<br />', '')
# re.sub('br', "", ss)

print('---------类别---------\n')
ObjType = soup.find("div", {'id': 'headerSearch'})
ObjTypeContent = ObjType.find_all('option')
for i in ObjTypeContent:
    if i.attrs.get('selected'):
        print(i.text)
print()


print('---------标题---------\n')
SubTitle = soup.find("h1", {'class': 'nameSingle'})
print('主标题： ' + SubTitle.find('a').text)
print('副标题： ', end='')
if SubTitle.find('small'):
    print(SubTitle.find('small').text)
else:
    print('None')
print()


print("---------简介---------\n\n"+ss+"\n\n")

# f = open("kk", "w", encoding="utf-8")
# print(s, file=f)
# print(res, file=f)
# f.close()

print("---------标签---------\n")
for i in resLab:
    print(i[1]+"\nbangumi.tv"+i[0]+"\n")
print("\n\n")


print("---------角色---------\n")
paChar = re.compile('<a href="(.*?)" title="(.*?)" class="avatar l">')
paCharType = re.compile('<small><span class="badge_job_tip">(.*?)</span></small>')
paCV = re.compile('<a href="(.*?)" rel="v:starring">(.*?)</a>')
resChar = re.findall(paChar, s)
resCharType = re.findall(paCharType, s)
resCV = re.findall(paCV, s)
for i in range(0, len(resChar)):
    print(resCharType[i] + "\n" + resChar[i][1] + "\nbangumi.tv" + resChar[i][0] + "\n" + resCV[i][1] + "\nbangumi.tv" + resCV[i][0] + "\n")


print("\n---------制作信息---------\n")
TargetIn = soup.find("div", {'class': 'infobox'})
TargetImg = "http:" + TargetIn.find("img").attrs.get("src")
print("预览图： " + TargetImg + "\n")

# TargetImg_down = requests.get(url=TargetImg)
# # file_name = str(uuid.uuid4())+'.jpg'
# file_name = st_b + "_MainImpressionImg" + '.jpg'
# with open(file_name, 'wb') as fp:
#     fp.write(TargetImg_down.content)

Tag = TargetIn.find_all("li")
for i in Tag:
    TagWeb = i.find_all('a')
    print(i.text)
    if TagWeb:
        for j in TagWeb:
            print("bangumi.tv" + j['href'])
    print()



print("\n---------评分信息---------\n")
TargetRank = soup.find("div", {'class': 'SidePanel png_bg'})
RankTitle = TargetRank.find("div", {'class': 'global_score'})
for i in RankTitle.find_all("small"):
    print(i.text)
RankChinese = RankTitle.find_all("span")
print(RankChinese[2].text)
RankContent = TargetRank.find_all("li")
for i in RankContent:
    RankTem = i.find_all("span")
    RankPrintCon = 0
    for j in RankTem:
        RankPrintCon = RankPrintCon + 1
        if RankPrintCon % 2:
            print(j.text + "分： ", end='')
        else:
            print(j.text + "  " + j.attrs.get('style'))


print("\n---------关联条目---------")
RelSub = soup.find("div", {'class': 'content_inner'})
RelContent = RelSub.find_all("li")
for i in RelContent:
    RelType = i.find("span", {'class', 'sub'}).text
    if RelType:
        print('\n' + RelType)
    RelName = i.find_all("a")
    print(RelName[1].text)
    print('bangumi.tv' + RelName[0].attrs.get('href'))
    print('http:' + RelName[0].find("span").attrs.get('style')[22:-2])


print('\n\n---------评论---------\n')
LongComment = soup.find("div", {'class': 'content_inner clearit'})
LongCommentContent = LongComment.find_all("div", {'class': 'item clearit'})
for i in LongCommentContent:
    print(i.find('a').attrs.get('title'))
    LongCommentA = i.find_all('span')
    print('http:' + LongCommentA[0].find('img').attrs.get('src'))
    print(LongCommentA[3].text)
    LongCommentB = i.find_all('small')
    print(LongCommentB[0].text + '   ' + LongCommentB[1].text)
    print('http://bangumi.tv' + LongCommentB[2].find('a').attrs.get('href'))
    print(i.find("div", {'class': 'content'}).text)
    print()


print('\n---------讨论版---------\n')
DisBoard = soup.find('table').find_all('tr')
for i in DisBoard:
    if i.attrs.get('class'):
        DisBoardContent = i.find_all('td')
        print( DisBoardContent[0].find('a').text)
        print('http://bangumi.tv' + DisBoardContent[0].find('a').attrs.get('href'))
        print(DisBoardContent[1].find('a').text)
        print('http://bangumi.tv' + DisBoardContent[1].find('a').attrs.get('href'))
        print(DisBoardContent[2].find('small').text)
        print(DisBoardContent[3].find('small').text + '\n')


print('\n---------人数统计信息---------\n')
SumInAll = soup.find("div", {'id': 'columnSubjectHomeA'}).find_all("span", {'class': 'tip_i'})[1].find_all('a')
for i in SumInAll:
    print(i.text)
    print('http://bangumi.tv' + i.attrs.get('href') + '\n')


print('\n---------吐槽箱---------\n')
Remark = soup.find("div", {'id': 'comment_box'}).find_all("div", {'class': 'item clearit'})
for i in Remark:
    RemarkSpan = i.find_all('span')
    RemarkA = i.find_all('a')
    print('http:' + RemarkSpan[0].attrs.get('style')[22:-2])
    print(RemarkA[1].text)
    print('http://bangumi.tv' + RemarkA[1].attrs.get('href'))
    print(i.find('small').text[2:])
    print(i.find('p').text)
    print()


RelIndex = soup.find("div", {'id': 'subjectPanelIndex'})
print('\n---------' + RelIndex.find('h2').text + '---------\n')
RelIndexContent = RelIndex.find_all('li')
for i in RelIndexContent:
    RelIndexList = i.find_all('a')
    print(RelIndexList[1].text)
    print('http://bangumi' + RelIndexList[1].attrs.get('href'))
    print('http:' + i.find('span').attrs.get('style')[22:-2])
    print('by  ' + RelIndexList[2].text)
    print('http://bangumi' + RelIndexList[2].attrs.get('href'))
    print()


RelUser = soup.find("div", {'id': 'subjectPanelCollect'})
RelUserPri = RelUser.find('h2').text.replace('?', '')
print('\n---------' + RelUserPri + '---------\n')
RelUserContent = RelUser.find_all('li')
for i in RelUserContent:
    RelUserSpan = i.find_all('span')
    RelUserA = i.find_all('a')
    print(RelUserA[1].text)
    print('http://bangumi' + RelUserA[1].attrs.get('href'))
    print('http:' + RelUserSpan[0].attrs.get('style')[22:-2])
    if len(RelUserSpan) > 1:
        print(RelUserSpan[1].attrs.get('class'))
    else:
        print("None Rank")
    print(i.find('small').text)
    print()


print('\n---------爬取结束---------\n')
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('爬取完成时间： ' + now_time)



# ------ The Following Statement is Just Rubbish -----------


# bb = "class"
# for li in list(li_list):
#     # print(li)
#     # resWeb = re.findall(pa, str(li))
#     a_tag = li.find_all('span')
#     for ll in a_tag:
#         aa = str(ll)[6:11]
#         # print(aa)
#         if (aa != bb):
#             print(str(ll)[6:-7])   #标签
        # tem = str(ll)[6:-7]
#         # pa.findall(tem)
#         # if tem:
#         #     print(tem)



# target = soup.find(id="subject_detail")
# # li_list = target.find_all('div')
# li_list = target.find("div", {'class': 'subject_tag_section'})
# # print(li_list)
# for li in li_list.children:
#     # aa = li.find({'class': 'inner'})
#     print(li)
#     # a_tag = li.find_all('span')
#     # for ll in a_tag:
#     #     print(str(ll)[6:-7])   #标签


# target = soup.find(id="subject_detail")
# # li_list = target.find_all('div')
# li_list = target.find("div", {'class': 'subject_tag_section'})
# # print(li_list)
# for li in li_list:
#     bb = ""
#     bb = bb.join(li)
#     # aa = bb.find({'class': 'inner'})
#     a_tag = bb.find_all('span')
#     for ll in a_tag:
#         print(str(ll)[6:-7])   #标签
#     # a_tag = li.select('div[id="subject_summary"]')
#     # a_tag = li.select('.subject_summary')
#     # print(a_tag)


    # b_tag = li.find('div')
    # if b_tag:
    #     introduce = b_tag.find("div", {'class': 'll'})
        # print(b_tag)
        # title_zh = b_tag.find("a").text
        # title_jp = b_tag.find("small").text
        # rank = b_tag.find("span").text
        # information = b_tag.find("p").text
        # score = b_tag.find("p", {'class': 'rateInfo'}).text
        # print(title_zh)
        # print(title_jp)
        # print(rank)
        # print(information[26:])
        # print(score[2:-1])

    # if a_tag:
    #     href = "http://bangumi.tv/" + a_tag.attrs.get("href")
    #     img_src = a_tag.find("img").attrs.get("src")
    #     print(href)
    #     print(img_src[2:] + "\n")
    #     # img_reponse = requests.get(url=img_src)
    #     # file_name = str(uuid.uuid4())+'.jpg
    #     # with open(file_name,'wb') as fp:
    #     #     fp.write(img_reponse.content)