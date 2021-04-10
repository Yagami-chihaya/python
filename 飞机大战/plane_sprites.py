import random
import pygame

SCREEN_SIZE_HEIGHT = 700
SCREEN_RECT = pygame.Rect(0,0,480,700)

class GameSprites(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        super().__init__()
        self.image=pygame.image.load(image_name) 
        self.rect=self.image.get_rect()
        self.speed=speed

    def update(self):
        #更改精灵y轴方向
        self.rect.y += self.speed 

class Background(GameSprites):
    def update(self):

        super().update()
        if self.rect.y>= SCREEN_SIZE_HEIGHT:
            self.rect.y= -SCREEN_SIZE_HEIGHT

class Enemy(GameSprites):
    def __init__(self):
        super().__init__("飞机大战/images/enemy1.png")  #调用父类初始化方法创建敌机对象
        self.speed = random.randint(1,4)
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)
        self.rect.bottom = 0 #相当于rect.y=-rect.height
    def update(self):
        super().update()
        if self.rect.y >=SCREEN_SIZE_HEIGHT:
            self.kill()
    def __del__(self):
        print("销毁")

class Hero(GameSprites):
    def __init__(self):
        super().__init__("飞机大战/images/me1.png",0)
        self.rect.centerx = 0.5*SCREEN_RECT.width
        self.rect.bottom = SCREEN_RECT.bottom-120
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x +=3
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -=3

        if self.rect.x < 0 :
            self.rect.x = 0
        elif self.rect.x > SCREEN_RECT.width-self.rect.width:
            self.rect.x = SCREEN_RECT.width-self.rect.width

    def fire(self):
        for i in (0,1,2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.y = self.rect.y + 20*i
            self.bullet_group.add(bullet)
    
    

class Bullet(GameSprites):
    def __init__(self):
        super().__init__("飞机大战/images/bullet1.png",-5)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()