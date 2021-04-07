def demo(num,*nums,**person):
    print(num)
    print(nums)
    print(person)

demo(1,(1,2,3),{"name": "qiaoyang",
                "gendar": "male",
                "number": "13982932057"
})

def demo1(num,*nums,**person):
    print(num)
    print(nums)
    print(person)


demo1(1,1,2,3,name="qiaoyang",gendar="male",number="13982932057")