import re
import time
import requests
from lxml import etree
import os
from multiprocessing.dummy import Pool

#前言：梨视频的采用了ajax方式加载视频，并且在ajax里的表格保存了视频的假地址，但也不完全假，通过正则替换的方式将地址更改为正确地址即可
#有一说一，这个对新手太劝退了！！

url = "https://www.pearvideo.com/"
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
}

response = requests.get(url=url,headers=headers).text
tree = etree.HTML(response)

hrefAll = tree.xpath('//div[@class="vervideo-tbd"]/a/@href')  #获取了首页所有视频的a标签的href属性，即获取视频序号(id)
nameAll = tree.xpath('//div[@class="vervideo-tbd"]/a//div[@class="vervideo-name"]/text()')   #获取首页视频的名字列表

if os.path.exists("视频") is not True:      #没有文件夹则创建一个
    os.mkdir("视频")

infoList = [] #存储视频的url和保存路径

i=1
num = int(input("请输入下载任务的最大数量(可下载视频最多5个，因为首页就这么多)\n"))

def downloadVideo(infoList):   #定义下载功能函数,便于后面进程池调用，至于为什么只有一个参数，是因为pool.map方法只接受两个参数，所以这里是为了减少参数把video_src和video_path参数合并成一个字典参数
    print(infoList['video_path']+" 开始下载\n")
    start = time.time()
    video = requests.get(url=infoList['video_src'], headers=headers).content
    with open(infoList['video_path'], "wb") as fp:
        fp.write(video)
    end = time.time()
    spend_time = end - start
    print(infoList['video_path']+"下载完成 花时"+str(round(spend_time,2))+"秒\n")



for href in hrefAll:
    video_url = "https://www.pearvideo.com/videoStatus.jsp?contId="+href[6:]    #访问ajax，目的是从表单获取视频假地址

    headers={
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
        "Referer": video_url
    }

    video_json = requests.get(url=video_url,headers=headers).json()      #获取表单

    json_url = video_json.get('videoInfo').get('videos').get('srcUrl')    #获取表单里的视频假地址

    code = "/cont-"+href[6:]+"-"       #视频假地址的替换内容

    video_src = re.sub('/[0-9]*-',code,json_url)      #正则处理假地址，处理后video_src即为视频真正的地址


    video_name = str(i)+"."+nameAll[i-1]      #视频名字
    video_path = "视频/"+video_name+".mp4"   #视频保存的本地地址

    video_info = {      #合并video_src和video_path两个参数
        "video_src": video_src,
        "video_path": video_path
    }
    infoList.append(video_info)

    i+=1

pool = Pool(num)   #创建Pool对象，参数意思是可同时运行4个进程
pool.map(downloadVideo,infoList)   #注意该方法只能传入两个参数！！
pool.close()   #关闭pool，使其不在接受新的（主进程）任务
pool.join()   #主进程阻塞后，让子进程继续运行完成，子进程运行完后，再把主进程全部关掉

