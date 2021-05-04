import requests

if __name__ == "__main__" :
    url = "https://www.sogou.com/"
    respones = requests.get(url)  #发起请求

    content = respones.text
    print(content)
    with open("爬虫练习/sogou.html","w",encoding="utf-8") as fp:
        fp.write(content)