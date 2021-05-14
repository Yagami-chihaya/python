import requests

url = "https://www.baidu.com/s?ie=UTF-8&wd=ip"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
}

proxies = {
    "http":"218.253.39.60:8380	"
    #218.22.58.74
}
response = requests.get(url=url,headers=headers,proxies=proxies).text

with open("ip.html","w",encoding="utf-8") as fp:
    fp.write(response)