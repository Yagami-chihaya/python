import requests
from lxml import etree
import pytesseract
from PIL import Image
import os

url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
params = ""
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
}

responce = requests.get(url=url,headers=headers).text

tree = etree.HTML(responce)
img_path ='https://so.gushiwen.cn/'+str(tree.xpath('//*[@id="imgCode"]/@src')[0])
yanzhenma = requests.get(url=img_path).content

if os.path.exists("验证码图片") is not True:
    os.mkdir("验证码图片")
with open("验证码图片/test01.jpg",'wb') as fp:
    fp.write(yanzhenma)

img = Image.open("验证码图片/test01.jpg")
img = img.convert("L")    #图片灰化处理
img.save("验证码图片/test02.jpg")

# 自定义灰度界限，小于这个值为黑色，大于这个值为白色
threshold = 70

table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 图片二值化
photo = img.point(table, '1')
photo.save("验证码图片/test03.jpg")


text = pytesseract.image_to_string("验证码图片/test03.jpg")[0:4] #image_tp_string方法的lang属性可以选择图片识别的语言，默认选择英文
#不知道为何识别最后有乱码字符，故这里只提取我们要的前四个字符
print(text)

session = requests.session()

url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
data = {


    "from": "http://so.gushiwen.cn/user/collect.aspx",
    "email": "935760346@qq.com",
    "pwd": "123456",
    "code": text,
    "denglu": "登录"
}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
}
responce = session.post(url=url,data=data,headers=headers)


text_url = "https://so.gushiwen.cn/user/collect.aspx?type=m&id=1813666&sort=t"
page_text = session.get(url=text_url,headers=headers).text
print(page_text)
#由于古诗文网采用了__VIEWSTATE反爬虫，本人新手爬取失败




