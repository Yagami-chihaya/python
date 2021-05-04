# coding = utf-8
import json

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    kw = input("请输入餐厅关键字")
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
    }
    data = {
        "cname":"",
        "pid":"",
        "keyword": kw,
        "pageIndex": "1",
        "pageSize": "10"
    }

    responese = requests.post(url=url,data=data,headers=header)

    text = responese.json()
    newText = json.dumps(text,ensure_ascii=False)



    with open("./爬下来的文件/KFC--%s"%kw,"w",encoding="utf-8") as fp:
        fp.write(newText)





