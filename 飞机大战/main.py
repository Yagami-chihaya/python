
import pygame
import plane_sprites

##游戏初始化

pygame.init()

SCREEN_SIZE = (480,700)


screen = pygame.display.set_mode(SCREEN_SIZE)

#加载背景图片
bg1 = plane_sprites.Background("飞机大战/images/background.png")
bg2 = plane_sprites.Background("飞机大战/images/background.png")
bg2.rect.y=-bg2.rect.height
backGround_group = pygame.sprite.Group(bg1,bg2)



#初始化飞机
hero = plane_sprites.Hero()
hero_group = pygame.sprite.Group(hero)

#创建子弹生成定时器
pygame.time.set_timer(pygame.USEREVENT+1,500)

#创建敌机出生定时器
pygame.time.set_timer(pygame.USEREVENT,1000)

#创建敌机组

enemy_group = pygame.sprite.Group()

#定义时钟
clock = pygame.time.Clock()


#更新显示
pygame.display.update()


##游戏循环
while(True):
    #事件列表捕获
    for event in pygame.event.get():
        #检测用户点击关闭按钮事件关闭程序
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #定时器添加敌机
        elif event.type  == pygame.USEREVENT:
            enemy = plane_sprites.Enemy()
            enemy_group.add(enemy)
        #定时器生成子弹
        elif event.type == pygame.USEREVENT+1:
            hero.fire()
    #调用飞机类里的update方法控制飞机的移动和移动限制
    hero_group.update()
    


    clock.tick(60)  #可以指定循环体内部的频率，参数代表一秒执行几次循环体


   
    

    #背景循环移动
    backGround_group.update()
    backGround_group.draw(screen)

    #让敌机动起来
    enemy_group.update()
    enemy_group.draw(screen)

    #显示飞机
    hero_group.update()
    hero_group.draw(screen)

    #显示子弹组
    hero.bullet_group.update()
    hero.bullet_group.draw(screen)

    #碰撞检测
    pygame.sprite.groupcollide(hero.bullet_group,enemy_group,True,True)#子弹和敌机的检测
    isEnd = pygame.sprite.spritecollide(hero,enemy_group,True)
    if len(isEnd) > 0:
        pygame.quit()
        exit()
        print("游戏结束，请重新开始游戏")
    pygame.display.update()

pygame.quit()