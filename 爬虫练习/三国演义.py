# coding=utf-8

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
    }

    text = requests.get(url=url,headers=header)
    print(text.encoding)
    text.encoding=('UTF-8')

    text=text.text
    soup = BeautifulSoup(text,"lxml")
    charact = soup.select(".book-mulu li")

    print(type(charact))

    str = ""
    for a in charact:
        str+=a.get_text()+"\n"

    with open("三国演义","w",encoding="utf-8") as fp:
        fp.write(str)