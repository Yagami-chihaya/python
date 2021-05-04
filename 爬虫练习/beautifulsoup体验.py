import requests
import lxml

from bs4 import BeautifulSoup

bs = BeautifulSoup(open("test.html"),'lxml')
tag = bs.a
print(type(bs))
