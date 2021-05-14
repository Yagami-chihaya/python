import requests
from lxml import etree
import os
import time


def download_picture(page,categories,topRange,purity):


    url = "https://wallhaven.cc/search?"
    parmas = {
        "categories": categories,
        "purity": purity,
        "topRange": topRange,
        "sorting": "toplist",
        "order": "desc",
        "page": page
    }
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
    }
    proxies = {

        
    }

    response = requests.get(url=url,params=parmas,headers=headers,proxies=proxies).text
    tree = etree.HTML(response)
    pictureList = tree.xpath("//a[@class='preview']")
    print("网页读取成功！开始下载壁纸！")
    isExists = os.path.exists("pictures")  # 判断是否存在pictures目录，如果没有则创建
    if not isExists:
        os.mkdir("pictures")
    i=0
    for picture in pictureList:
        picture_src = picture.xpath('@href')[0]

        picture_web = requests.get(url=picture_src,headers=headers).text
        newtree = etree.HTML(picture_web)
        picture_src1 = newtree.xpath("//img[@id='wallpaper']/@src")[0]
        start_time = time.time()
        picture_data = requests.get(url=picture_src1,headers=headers).content
        picture_name = "类型_"+categories+" 第"+str(page)+"页 第"+str(i+1)+"张图片"+".jpg"
        i+=1

        picture_path = "./pictures/"+picture_name
        with open(picture_path,"wb") as fp:
            fp.write(picture_data)
            end_time = time.time()
            print(picture_src + "下载完成 大小为:"+str(round(os.path.getsize(picture_path)/1024/1024,2))+"M 耗时"+str(round(end_time-start_time))+"秒")

if __name__ == "__main__":

    pagetotal = input("请输入你要下载的页数\n")
    categories = input("选择你要下载的类型：一、下载其他类型输入100 二、下载动漫类型输入010 三、下载真人壁纸输入001 \n也可以选择多种类型\n")
    topRange = input("选择日期 1.一天1d 2.三天3d 3.一周1w 4.一个月1M 5.三个月3M 6.半年6M 7.一年1y\n")
    purity = input("是否下载不可描述的图片！！1.是的话输入010 2.否输入100 3.我全都要110\n")

    page=1
    while True:
        if page<=int(pagetotal):
            download_picture(page,categories,topRange,purity)
            page+=1
        else : break
    print("下载完成，请在程序根目录查看！")
    os.startfile("pictures")

