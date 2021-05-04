import json

import requests
from bs4 import BeautifulSoup

#爬豆瓣的图片

if __name__ == "__main__":
    url = "https://movie.douban.com/top250"


    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
    }


    request = requests.get(url=url,headers=header)

    text = request.text

    bs = BeautifulSoup(text,"lxml")
    i = 0
    picture = bs.select(".pic a img") #抓捕类名为.pic下的a标签里的img标签，返回ResultSet对象
    print(type(picture))

    picstr = ""         #用来保存转换后字符串对象
    for pic in picture:       #遍历获取到的img标签对象，再把值传回str对象里
        print(pic['alt'])
        new_pic = str((pic['alt']))
        picstr+=new_pic+"\n"



    with open("picture","w",encoding="utf-8") as fp:  #保存数据
        fp.write(picstr)

    '''movieList = bs.find_all("div","item")
    for movieList in movieList:
        print(movieList.text)'''








