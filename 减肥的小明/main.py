class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return ("我的名字叫%s，现在%s公斤"%(self.name,self.weight))

    def run(self):
        self.weight-=0.5
        print("%s跑了半天，体重减少到了%s公斤！！"%(self.name,self.weight))

    def eat(self):
        self.weight+=1
        print("%s开始干饭,体重增加到%s公斤"%(self.name,self.weight))


xiaoming = Person("李子明",75)

xiaoming.run()
xiaoming.eat()

xiaomei = Person("小美",45)

print(xiaoming)
print(xiaomei)