# coding=utf-8

import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = "https://movie.douban.com/chart"
    params = {

		"filter":""
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
    request = requests.get(url=url,params=params,headers=headers)
    text = request.text
    bs = BeautifulSoup(text,'html.parser')
    title = bs.find_all("tr",class_="item")

    print(title)
