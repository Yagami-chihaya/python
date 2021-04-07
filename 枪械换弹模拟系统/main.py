import time

class Gun:
    def __init__(self,model):
        self.model=model
        self.bulltle_count=0
        

    def addBulltle(self):
        self.bulltle_count=30

    def shoot(self):
        while True:
            if self.bulltle_count>0:
                self.bulltle_count-=1
                print("子弹 -1 ，还剩%d发"%self.bulltle_count)
                time.sleep(0.1)
            else:
                print("子弹已打空，请补充弹药！")
                break


class Soldier:
    def __init__(self,name):
        self.name=name
        self.gun=None
    
    def __str__(self):
        return ("上场的士兵是%s，他使用的武器是%s！！"%(self.name,self.gun.model))

    def fire(self):
        if self.gun==None:
            print("士兵还未装备武器！！")
        if self.gun.bulltle_count<=0:
            print("开始上弹！！")
            self.gun.addBulltle()
        if self.gun.bulltle_count>0:
            print("%s已开火，请注意掩护！！"%self.name)
            self.gun.shoot()

AK47 = Gun("AK47")
siwote = Soldier("斯沃特")

siwote.gun=AK47

print(siwote)

siwote.fire()