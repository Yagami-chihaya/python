import requests
from lxml import etree
import os


url = "https://www.iwara.tv/videos"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
}
params = {
    "f[0]": "created:2021",
    "sort": "views"
}
proxies = {
    #"http":"67.207.83.225:80"
}

response = requests.get(url=url,headers=headers,params=params,proxies=proxies).text

tree = etree.HTML(response)

a_list = tree.xpath('//div[@class="field-item even"]/a/@href')
print("网站读取成功！")
if os.path.exists("iwara视频") is not True:
    os.mkdir("iwara视频")
i=1
for a in a_list:
    a_src = "https://www.iwara.tv"+a
    print(a_src)
    video_page = requests.get(url=a_src,headers=headers,proxies=proxies).text
    tree=etree.HTML(video_page)
    print(video_page)
    video_data_src = tree.xpath('//*[@id="video-player_html5_api"]')
    print(video_data_src)
    video_data = requests.get(url=video_data_src,headers=headers,proxies=proxies).content

    video_name = "第"+str(i)+"个视频.mp4"
    video_path = "iwara视频/"+video_name
    print("开始下载视频")
    with open(video_path,"wb") as fp:
        fp.write(video_data)
    print("成功下载"+video_name)
    i+=1


