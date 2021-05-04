# coding = utf-8
import requests

if __name__ == "__main__":
    #进行UA(User-Agent)伪装
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               }
    url = "https://www.sogou.com/web"
    keyword = input("请输入你要搜索的关键词")
    parma = {
        "query":keyword 
    }
    respones = requests.get(url,params=parma,headers = "")
    content = respones.text
    fileName = keyword+".html"

    with open(fileName,mode="w",encoding="utf-8") as f:
        f.write(content)