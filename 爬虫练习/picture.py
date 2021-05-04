import requests
from lxml import etree


def download_picture(page):


    url = "https://wallhaven.cc/search?"
    parmas = {
        "categories": "001",
        "purity": "100",
        "topRange": "1y",
        "sorting": "toplist",
        "order": "desc",
        "page": page
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"
    }
    response = requests.get(url=url,params=parmas,headers=headers).text
    tree = etree.HTML(response)
    pictureList = tree.xpath("//a[@class='preview']")
    i=0
    for picture in pictureList:
        picture_src = picture.xpath('@href')[0]
        picture_web = requests.get(url=picture_src,headers=headers).text
        newtree = etree.HTML(picture_web)
        picture_src1 = newtree.xpath("//img[@id='wallpaper']/@src")[0]
        picture_data = requests.get(url=picture_src1,headers=headers).content
        picture_name = "第"+str(page)+"页 第"+str(i+1)+"张图片"+".jpg"
        i+=1
        picture_path = "爬下来的文件/pictures/"+picture_name
        with open(picture_path,"wb") as fp:
            fp.write(picture_data)

if __name__ == "__main__":
    pagetotal = input("请输入你要下载的页数\n")
    page=1
    while True:
        if page<=int(pagetotal):
            download_picture(page)
            page+=1
        else : break
