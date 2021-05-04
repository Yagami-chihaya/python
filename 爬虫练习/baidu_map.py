import requests

from lxml import etree

if __name__ == "__main__":
    url = "http://api.map.baidu.com/place/v2/search?"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
    }
    data = {
        "query": "医院",
        "region": "合肥",
        "output": "xml",
        "ak": "e5QwVHtv0jZsF5wKfw2fuTBxx9AgxgWo",
        "page_size": 20
    }
    responese = requests.get(url=url, headers=headers, params=data).text
    tree = etree.HTML(responese.encode("utf-8"))
    i = 0
    hospitalStr = ""
    while i < len(tree.xpath('//name')):

        name = str(tree.xpath('//name/text()')[i]) + "\n"
        address = str(tree.xpath('//address/text()')[i]) + "\n"
        try:
            if str(tree.xpath('//telephone/text()')[i]) != -1:
                telephone = str(tree.xpath('//telephone/text()')[i]) + "\n"
                hospitalStr += name + address + telephone + "*****************\n"
        except:
            hospitalStr += name + address + "*****************\n"

        i += 1
    hos = hospitalStr
    print(hos)
    with open("./baiduMap", "w", encoding="utf-8") as fp:
        fp.write(hos)
