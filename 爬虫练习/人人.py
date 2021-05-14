#人人的验证码很杂乱，噪点也多，故暂时验证码读取失败

import requests
from lxml import etree
from PIL import Image
import pytesseract
url="http://www.renren.com/SysHome.do"

params={

}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
}

response = requests.get(url=url,headers=headers).text

tree = etree.HTML(response)

picture_path = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]

picture = requests.get(url=picture_path).content

with open("人人验证码test1.jpg","wb") as fp:
    fp.write(picture)

img = Image.open("人人验证码test1.jpg")
img = img.convert("L")        #图片灰化处理


ashValue = 200  #设置灰化边界值，小于该值输出黑点，大于该值输出白点

table = []

for i in range(256):
    if i < ashValue:
        table.append(0)
    else:
        table.append(1)

img = img.point(table,'1')
img.save("人人验证码.jpg")
img.show()
text = pytesseract.image_to_string("人人验证码.jpg")

print(text)



