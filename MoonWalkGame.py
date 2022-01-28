import pyxel
import random


class Player:
      #初期設定
    def __init__(self):
        self.x = 50
        self.y = 100
        self.vy = 0
        self.g = 1
        self.jump = 0
    def update(self):
        self.y += self.vy
        #重力
        if self.y < 100:
            self.vy += self.g
        #地面で止まる
        if self.y >= 100:
            self.vy = 0
            self.y = 100
            self.jump = 0
        #2段ジャンプまで
        if self.jump <= 1:
          if pyxel.btnp(pyxel.KEY_SPACE):
            self.vy -= 8
            self.jump += 1

class Obstacle:
    speed = 3
    def __init__(self):
      #初期設定
        self.x = 150
        self.y = 100
    def update(self):
      #敵移動
        self.x -= self.speed

class App:
    def __init__(self):
        pyxel.init(150, 150)
        #画像読み込み
        pyxel.load("MoonWalkGame.pyxres")
        #初期設定
        self.point = 0
        self.is_game_over = False
        self.miss = 0
        self.obstacles = [Obstacle()]
        self.player = Player()
        #作動
        pyxel.run(self.update, self.draw)

    def update(self):
      #class Playerのupdateを実行
        self.player.update()
        #score追加
        if self.miss <= 2:
            self.point += 1
        
        for self.obstacle in self.obstacles:
          #class Obstacleのupdateを実行
            self.obstacle.update()
            if -9 <= self.obstacle.x - self.player.x <=9 and -14 <= self.obstacle.y - self.player.y  <= 14:
              self.is_game_over = True
              self.obstacle.x = 150
              self.obstacle.y = random.randint(80, 100)
            #missを追加、is_game_overを元に戻す
            if self.is_game_over == True:
              self.miss += 1
              self.is_game_over = False
            #敵が画面外に行った時はじめに戻す
            if self.obstacle.x+16 <= 0:
              self.obstacle.x = 150
              self.obstacle.y = random.randint(80, 100)

    def draw(self):
        pyxel.cls(5)
        #ムーンウォーク
        if pyxel.frame_count % 20 <= 10:
          pyxel.blt(self.player.x,self.player.y,0,3,1,9,14,6)
        elif pyxel.frame_count % 20 >= 11:
          pyxel.blt(self.player.x,self.player.y,0,19,1,9,14,6)
        #Lifeの表示
        if self.miss >= 1:
          pyxel.blt(135,2,0,32,17,16,14,0)
        else:
          pyxel.blt(135,2,0,16,17,16,14,0)
        if self.miss >= 2:
          pyxel.blt(116,2,0,32,17,16,14,0)
        else:
          pyxel.blt(116,2,0,16,17,16,14,0)
        if self.miss >= 3:
          pyxel.blt(97,2,0,32,17,16,14,0)
        else:
          pyxel.blt(97,2,0,16,17,16,14,0)
        pyxel.text(5,5,"SCORE:"+str(self.point), 7)
        for self.obstacle in self.obstacles:
            pyxel.blt(self.obstacle.x, self.obstacle.y,0,51,2,9,11,6)
        pyxel.rect(0,115,150,35,10)
        if self.miss >= 3:
          pyxel.cls(5)
          pyxel.text(55,70,"GAME OVER!!",7)
          pyxel.text(59,80,"SCORE:"+str(self.point),7)

App()