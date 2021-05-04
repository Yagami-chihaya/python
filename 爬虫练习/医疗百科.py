import requests
from lxml import etree

if __name__ == "__main__":

    url = "https://baike.baidu.com/wikitag/api/getlemmas"
    params={
        "limit": "24",
        "timeout": "3000",
        "filterTags": "[]",
        "tagId": "75953",
        "fromLemma": "false",
        "contentLength": "40",
        "page": "1"
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
    }

    response = requests.post(url=url,data=params,headers=headers).text
    tree = etree.HTML(response)
    name = tree.xpath("/html/body/div[2]/div[2]/div/div/div[1]/div[30]/a/div/div[2]/div[1]/div[1]")
    print(response)
    print(tree)
    print(name)