from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.vccoo.com")
bsObj=BeautifulSoup(html.read(),"html.parser")
print(bsObj.h1)