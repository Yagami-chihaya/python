class Game:

    top_score=60
    
    def __init__(self,player_name):
        self.player_name=player_name
    
    @staticmethod    #定义静态方法
    def show_help():
        print("help")
    
    def changeScore(self,score):
        self.score=score
        print("%s的分数是%d"%(self.player_name,self.score))
    
    @classmethod  #定义类方法
    def show_top_score(cls):

        print("当前最高分是%d"%cls.top_score)

    def start_game(self):
        print("%s开始了游戏"%self.player_name)

newGame01 = Game("小明")
Game.show_help()
newGame01.start_game()
newGame01.changeScore(0)
Game.show_top_score()

