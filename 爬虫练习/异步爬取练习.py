import requests
from lxml import etree
import os

urls = [
    "https://www.baidu.com/s?ie=UTF-8&wd=yagamichihaya",
    "https://www.baidu.com/s?ie=UTF-8&wd=qiaoyang",
    "https://www.baidu.com/s?ie=UTF-8&wd=bilibili"
]
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
}
i=1
for url in urls:
    response = requests.get(url=url,headers=headers).text
    if os.path.exists("异步爬取练习文件夹") is not True:
        os.mkdir("异步爬取练习文件夹")
    fileName = "异步爬取练习文件夹/"+str(i)+".html"
    with open(fileName,"w",encoding="utf-8") as fp:
        fp.write(response)
    i+=1
