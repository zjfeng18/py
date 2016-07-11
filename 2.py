from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e: #网页在服务器上不存在（或获取页面时不存在），uelopen会抛出HTTPError异常
        return None
    try:
        bsObj=BeautifulSoup(html.read(),"html.parser")
        title=bsObj.body.h1
    except AttributeError as e:#如果调用标签不存在，BeautifulSoup就会返回None对象，再调用这个None对象下的的子标签，就会返回AttributeError错误
        return None
    return title

title=getTitle("http://www.vccoo.com")
if title == None:
    print("Title 没有找到")
else:
    print(title)