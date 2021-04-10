class Qiaoyang:
    def __new__(cls):
        print("new")
        saveAddress = super().__new__(cls) #__new__方法会为对象分配空间，如果不返回地址会导致类不会初始化
        return saveAddress
    
    def __init__(self):
        print("init")
    
qiaoyang = Qiaoyang()

print(qiaoyang)

