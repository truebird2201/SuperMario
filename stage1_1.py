from random import randint
from pico2d import *
import game_framework
import Select_state
import stage1_2
import GameOver
from math import *

sonic_sprite = None
star = None
walk_monster = None
fly_monster = None
stage1_1 = None
num = None
item = None
score = None
coin = None
star = None
firesonic = None
flower = None
bmx = 0
bmy = 0
point = 0
money = 0
life = 3

def point_draw():
    global point
    score.clip_draw(0, 0, 170, 80, 80, 519, 130 ,50)
    coin.clip_draw(0, 0, 20, 20, 120, 485, 20, 20)
    sonic_sprite.clip_draw(0, 460, 40, 40, 120, 560, 40, 40)

    for i in range(0, 9+1):                                                 # 점수
        if point//1000000 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+20, 515, 25, 25)
        if (point // 100000) % 10000 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+40, 515, 25, 25)
        if (point//10000)%1000 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+60, 515, 25, 25)
        if (point//1000)%100 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+80, 515, 25, 25)
        if (point//100)%10 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+100, 515, 25, 25)
        if (point//10)%10 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+120, 515, 25, 25)
        if point%10 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+140, 515, 25, 25)

    for i in range(0, 9+1):                                                 # 돈
        if (money//10)%10 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+20, 490, 25, 25)
        if money%10 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+40, 490, 25, 25)

    for i in range(0, 9+1):                                                 # 목숨
        if (life//10)%10 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+20, 560, 25, 25)
        if life%10 == i:
            num.clip_draw(0+80*i, 0, 80, 80, 130+40, 560, 25, 25)


class item:
    left = 0
    right = 0
    top = 0
    bottom = 0
    frame = 0
    ground = True
    dir = 1
    gravity = 0.01
    jumpPower = 1.5
    jumpTime = 0
    savey = 0
    kind = 0

    Jumping = True

    life = True


    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind

    def update(self):
        if self.kind==0:
            self.frame = (self.frame + 0.025) % 10
        else:
            self.frame = (self.frame + 0.02) % 7
        self.left = self.x - 20
        self.right = self.x + 20
        self.top = self.y + 20
        self.bottom = self.y - 20

        if self.kind == 1:
            self.x += self.dir * 0.7
        elif self.kind == 2:
            self.x += self.dir * 0.5



    def move(self):
        if self.kind == 1:                                                              # 스타
            if self.Jumping:
                self.y = (self.jumpTime * self.jumpTime * (-self.gravity) / 2) + (
                            self.jumpTime * self.jumpPower)
                self.jumpTime += 1
                if self.y < self.savey:
                    self.y = self.savey
                    self.Jumping = True
                    self.jumpTime = 0.0


            for i in b:
                if crush(self, i) == 1:
                    self.dir = -1
                elif crush(self, i) == 2:
                    self.dir = 1
                elif crush(self, i) == 3:
                    self.y = i.top + 20
                    self.savey = self.y

        elif self.kind == 2:                                                            # 버섯
            self.y -= 0.5
            for i in b:
                if crush(self, i) == 1:
                    self.dir = -1
                elif crush(self, i) == 2:
                    self.dir = 1
                elif crush(self, i) == 3:
                    self.y = i.top + 20

    def draw(self):
        if self.kind == 0:
            coin.clip_draw(int(self.frame) * 20, 0, 20, 20, self.x, self.y, 20, 20)
        if self.kind == 1:
            it.clip_draw(int(self.frame) * 40, 160, 40, 40, self.x, self.y, 50, 50)
        elif self.kind == 2:
            it.clip_draw(0, 120, 40, 40, self.x, self.y, 25, 25)
        elif self.kind == 3:
            it.clip_draw(40, 120, 40, 40, self.x, self.y, 25, 25)



class player:

    left = 0
    right = 0
    top = 0
    bottom = 0
    frame = 0
    ground = True
    dir = 0
    dir2 = 1
    gravity = 0.01
    jumpPower = 1.5
    jumpTime = 0
    downpower = 0
    savey = 0
    savey2 = 0
    jumpcount = 2
    Ground = True
    Jumping = False
    fast = False
    GoDown = False
    GoDown2 = False
    plus_move = 0
    die = False
    starmode = False
    firemode = False
    starcount = 0
    diedown = 0
    size = 48


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        if sonic.dir == 0:  # 프레임
            self.frame = (self.frame + 0.015) % 8
        else:
            self.frame = (self.frame + 0.03) % 8

        if self.size == 60:                         # 버섯
            self.left = self.x - 20
            self.right = self.x + 20
            self.top = self.y + 30
            self.bottom = self.y - 30

        elif self.size == 48:                       # 기본
            self.left = self.x - 16
            self.right = self.x + 16
            self.top = self.y + 24
            self.bottom = self.y - 24

        for i in ite:                                                           # 아이템 감지
            if player_ground_crush(self, i) != 0 and i.life == True:
                if i.kind == 1:                                                 # 별
                    self.starmode = True
                    self.starcount = 3500
                    i.life = False
                elif i.kind == 2:                                                # 버섯
                    self.size = 60
                    i.life = False
                elif i.kind == 0:                                                # 동전
                    global money
                    money += 1
                    i.life = False
                    if money == 50:
                        money = 0
                elif i.kind == 3:                                                # 꽃
                    self.firemode = True
                    self.size = 60
                    i.life = False

        for i in wm:
            if self.die == False and i.die == False:
                if sonic.starmode == False:                                                 # 스타모드가 아니라면
                    if player_ground_crush(self, i) == 1 or player_ground_crush(self, i) == 2:                  # 옆에서 부딪히면 소닉 죽음
                        sonic.die = True
                        sonic.frame = 0
                        sonic.dir = 0
                    if player_ground_crush(self, i) == 3:                                             # 위에서 소닉이 밟으면 굼바 죽음
                        if i.die == False:
                            global point
                            point += 2
                        i.die = True
                        i.frame = 0

                        self.Jumping = True
                        self.jumpTime = 0.0
                        self.jumpcount = 1

                else:
                    if crush(sonic, i) != 0:
                        if i.die == False:
                            point += 2
                        i.die = True
                        i.frame = 0


        if self.die == True and int(self.frame) <= 2:                                        # 떨어지는 이미지
            self.diedown -= 0.2
        elif self.die == True and int(self.frame) <= 6:
            self.diedown += 1

        if self.die == True and int(self.frame) == 7:                               # 죽으면 초기화
            global life
            life -= 1
            enter()
        if self.starmode == True:
            self.starcount-=1

        if self.starcount == 0 and self.starmode == True:                           # 스타모드 끝
            self.starmode = False



    def move(self):

        if self.Jumping:
            self.y = (self.jumpTime * self.jumpTime * (-self.gravity) / 2) + (
                        self.jumpTime * self.jumpPower) + self.savey2
            self.jumpTime += 1
            if self.y < self.savey:
                self.y = self.savey
                self.Jumping = False
                self.jumpTime = 0.0
                self.jumpcount = 2

        if self.dir != 0 and self.plus_move < 0.6:
            self.plus_move += 0.001
            if self.plus_move > 0.6:
                self.plus_move = 0.6

        elif self.dir == 0 and self.plus_move > 0:
            self.plus_move -= 0.0015
            if self.plus_move < 0:
                self.plus_move = 0

        if self.dir != 0 and self.dir != self.dir2:
            self.plus_move = 0

        if self.x > 970 and self.dir != -1:
            self.x = 970
        elif self.x < 30 and self.dir != 1:
            self.x = 30
        else:
            if self.fast and self.dir != 0:  # 대시 on
                self.x += (self.dir * 0.2) + (self.dir2 * self.plus_move)
            else:  # 대시 off
                self.x += self.dir2 * self.plus_move
        self.Ground = False

        for i in b:
            if player_ground_crush(self, i) == 3:
                self.Ground = True
                self.downpower = 0

        if self.Ground == False:
            self.savey = 0
            if self.Jumping == False:
                self.y -= 0.2 + self.downpower
                self.downpower += 0.015

        for i in b:
            if self.size == 60:
                if player_ground_crush(self, i) == 1:
                    self.x = i.left - 20
                elif player_ground_crush(self, i) == 2:
                    self.x = i.right + 20
                elif player_ground_crush(self, i) == 3:
                    self.y = i.top + 30
                    self.savey = self.y
                elif player_ground_crush(self, i) == 4:
                    self.y = i.bottom-30
                    self.savey = self.y
                    self.Jumping = False
            elif self.size == 48:
                if player_ground_crush(self, i) == 1:
                    self.x = i.left - 16
                elif player_ground_crush(self, i) == 2:
                    self.x = i.right + 16
                elif player_ground_crush(self, i) == 3:
                    self.y = i.top + 24
                    self.savey = self.y
                elif player_ground_crush(self, i) == 4:
                    self.y = i.bottom-24
                    self.savey = self.y
                    self.Jumping = False

    def draw(self):

        if self.die == True:                        # 죽으면
                sonic_sprite.clip_draw(int(self.frame) * 40, 260, 40, 40, self.x, self.y-self.diedown, self.size, self.size)
        else:
            if self.GoDown2 == True:
                if self.firemode == True:
                    firesonic.clip_draw(int(self.frame) * 40, 300, 40, 40, self.x, self.y, self.size, self.size)
                else:
                    sonic_sprite.clip_draw(int(self.frame) * 40, 300, 40, 40, self.x, self.y, self.size, self.size)
                if self.frame > 7:
                    delay(0.2)
                    self.GoDown2 = False
                    game_framework.change_state(stage1_2)
            else:
                if self.starmode == False:                                                                          # 스타모드 아닐때
                    if self.dir == 1:  # 오른쪽
                        if self.fast:  # 대시
                            if self.firemode == True:
                                firesonic.clip_draw(int(self.frame) * 40, 380, 40, 40, self.x, self.y, self.size, self.size)
                            else:
                                sonic_sprite.clip_draw(int(self.frame) * 40, 380, 40, 40, self.x, self.y, self.size, self.size)
                        else:
                            if self.Jumping:
                                if self.firemode == True:
                                    firesonic.clip_draw(int(self.frame) * 40, 340, 40, 40, self.x, self.y, self.size, self.size)
                                else:
                                    sonic_sprite.clip_draw(int(self.frame) * 40, 340, 40, 40, self.x, self.y, self.size, self.size)
                            else:
                                if self.plus_move < 0.5:
                                    if self.firemode == True:
                                        firesonic.clip_draw(int(self.frame) * 40, 460, 40, 40, self.x, self.y, self.size, self.size)
                                    else:
                                        sonic_sprite.clip_draw(int(self.frame) * 40, 460, 40, 40, self.x, self.y, self.size, self.size)
                                else:
                                    if self.firemode == True:
                                        firesonic.clip_draw(int(self.frame) * 40, 220, 40, 40, self.x, self.y, self.size, self.size)
                                    else:
                                        sonic_sprite.clip_draw(int(self.frame) * 40, 220, 40, 40, self.x, self.y, self.size, self.size)

                    elif self.dir == -1:  # 왼쪽
                        if self.fast:  # 대시
                            if self.firemode == True:
                                firesonic.clip_composite_draw(int(self.frame) * 40, 380, 40, 40, 0, 'h', self.x, self.y, self.size, self.size)
                            else:
                                sonic_sprite.clip_composite_draw(int(self.frame) * 40, 380, 40, 40, 0, 'h', self.x, self.y, self.size, self.size)
                        else:
                            if self.Jumping:
                                if self.firemode == True:
                                    firesonic.clip_composite_draw(int(self.frame) * 40, 340, 40, 40, 0, 'h', self.x, self.y, self.size, self.size)
                                else:
                                    sonic_sprite.clip_composite_draw(int(self.frame) * 40, 340, 40, 40, 0, 'h', self.x, self.y, self.size, self.size)
                            else:
                                if self.plus_move < 0.5:
                                    if self.firemode == True:
                                        firesonic.clip_composite_draw(int(self.frame) * 40, 460, 40, 40, 0, 'h', self.x, self.y, self.size, self.size)
                                    else:
                                        sonic_sprite.clip_composite_draw(int(self.frame) * 40, 460, 40, 40, 0, 'h', self.x, self.y, self.size, self.size)
                                else:
                                    if self.firemode == True:
                                        firesonic.clip_composite_draw(int(self.frame) * 40, 220, 40, 40, 0, 'h', self.x,self.y, self.size, self.size)
                                    else:
                                        sonic_sprite.clip_composite_draw(int(self.frame) * 40, 220, 40, 40, 0, 'h', self.x,self.y, self.size, self.size)

                    elif self.dir == 0 and self.dir2 == 1:  # 마지막이 오른쪽이였던 멈춤
                        if self.Jumping == False:
                            if self.plus_move == 0:
                                if self.firemode == True:
                                    firesonic.clip_draw(int(self.frame) * 40, 420, 40, 40, self.x, self.y, self.size, self.size)
                                else:
                                    sonic_sprite.clip_draw(int(self.frame) * 40, 420, 40, 40, self.x, self.y, self.size, self.size)
                            else:
                                if self.firemode == True:
                                    firesonic.clip_draw(int(self.frame) * 40, 180, 40, 40, self.x, self.y, self.size, self.size)
                                else:
                                    sonic_sprite.clip_draw(int(self.frame) * 40, 180, 40, 40, self.x, self.y, self.size, self.size)
                        else:
                            if self.firemode == True:
                                firesonic.clip_draw(int(self.frame) * 40, 340, 40, 40, self.x, self.y, self.size, self.size)
                            else:
                                sonic_sprite.clip_draw(int(self.frame) * 40, 340, 40, 40, self.x, self.y, self.size, self.size)

                    elif self.dir == 0 and self.dir2 == -1:  # 마지막이 왼쪽이였던 멈춤
                        if self.Jumping == False:
                            if self.plus_move == 0:
                                if self.firemode == True:
                                    firesonic.clip_composite_draw(int(self.frame) * 40, 420, 40, 40, 0, 'h', self.x, self.y, self.size, self.size)
                                else:
                                    sonic_sprite.clip_composite_draw(int(self.frame) * 40, 420, 40, 40, 0, 'h', self.x, self.y, self.size, self.size)
                            else:
                                if self.firemode == True:
                                    firesonic.clip_composite_draw(int(self.frame) * 40, 180, 40, 40, 0, 'h', self.x, self.y,self.size, self.size)
                                else:
                                    sonic_sprite.clip_composite_draw(int(self.frame) * 40, 180, 40, 40, 0, 'h', self.x, self.y,self.size, self.size)
                        else:
                            if self.firemode == True:
                                firesonic.clip_composite_draw(int(self.frame) * 40, 340, 40, 40, 0, 'h', self.x, self.y, self.size, self.size)
                            else:
                                sonic_sprite.clip_composite_draw(int(self.frame) * 40, 340, 40, 40, 0, 'h', self.x, self.y, self.size, self.size)


                else:                                                                                                                       # 스타 모드일때
                    if self.dir == 1:  # 오른쪽
                        if self.fast:  # 대시
                            star.clip_draw(int(self.frame) * 40, 380, 40, 40, self.x, self.y, self.size, self.size)
                        else:
                            if self.Jumping:
                                star.clip_draw(int(self.frame) * 40, 340, 40, 40, self.x, self.y, self.size, self.size)
                            else:
                                if self.plus_move < 0.5:
                                    star.clip_draw(int(self.frame) * 40, 460, 40, 40, self.x, self.y, self.size, self.size)
                                else:
                                    star.clip_draw(int(self.frame) * 40, 220, 40, 40, self.x, self.y, self.size, self.size)

                    elif self.dir == -1:  # 왼쪽
                        if self.fast:  # 대시
                            star.clip_composite_draw(int(self.frame) * 40, 380, 40, 40, 0, 'h', self.x, self.y,self.size, self.size)
                        else:
                            if self.Jumping:
                                star.clip_composite_draw(int(self.frame) * 40, 340, 40, 40, 0, 'h', self.x,self.y, self.size, self.size)
                            else:
                                if self.plus_move < 0.5:
                                    star.clip_composite_draw(int(self.frame) * 40, 460, 40, 40, 0, 'h', self.x,self.y, self.size, self.size)
                                else:
                                    star.clip_composite_draw(int(self.frame) * 40, 220, 40, 40, 0, 'h', self.x,self.y, self.size, self.size)

                    elif self.dir == 0 and self.dir2 == 1:  # 마지막이 오른쪽이였던 멈춤
                        if self.Jumping == False:
                            if self.plus_move == 0:
                                star.clip_draw(int(self.frame) * 40, 420, 40, 40, self.x, self.y, self.size, self.size)
                            else:
                                star.clip_draw(int(self.frame) * 40, 180, 40, 40, self.x, self.y, self.size, self.size)
                        else:
                            star.clip_draw(int(self.frame) * 40, 340, 40, 40, self.x, self.y, self.size, self.size)

                    elif self.dir == 0 and self.dir2 == -1:  # 마지막이 왼쪽이였던 멈춤
                        if self.Jumping == False:
                            if self.plus_move == 0:
                                star.clip_composite_draw(int(self.frame) * 40, 420, 40, 40, 0, 'h', self.x,self.y, self.size, self.size)
                            else:
                                star.clip_composite_draw(int(self.frame) * 40, 180, 40, 40, 0, 'h', self.x,self.y, self.size, self.size)
                        else:
                            star.clip_composite_draw(int(self.frame) * 40, 340, 40, 40, 0, 'h', self.x, self.y,self.size, self.size)


class Monster:

    left = 0
    right = 0
    top = 0
    bottom = 0
    frame = 0
    Ground = False
    dir = 1
    life = True
    die = False
    global point


    def __init__(self, x, y, Speed, kind):
        self.x = x
        self.y = y
        self.Speed = Speed
        self.kind = kind

    def update(self):
        if self.kind==0:                    # 굼바 프레임
            self.frame = (self.frame + 0.03) % 16

        elif self.kind == 1:                # 부끄부끄 프레임
            self.frame = (self.frame + 0.05) % 8

        self.left = self.x - 30
        self.right = self.x + 30
        self.top = self.y + 30
        self.bottom = self.y - 30


        if self.die == True and int(self.frame) == 10:
            self.life = False

    def move(self):
        if self.kind == 0:                                      # 굼바
            self.x += self.dir * self.Speed
            for i in b:
                if crush(self, i) == 3:
                    if self.dir == 1:
                        if self.x+30 > i.right:
                            self.dir = -1
                            self.x += self.dir * self.Speed/10
                    else:
                        if self.x-30 < i.left:
                            self.dir = 1
                            self.x += self.dir * self.Speed/10
            self.Ground = False
            for i in b:
                if crush(self, i) == 3:
                    self.Ground = True
                    self.downpower = 0

            if self.Ground == False:
                self.y -= 3

        elif self.kind == 1:                                    # 부끄부끄
            pass


    def draw(self):

        if self.kind == 0:                                  # 굼바 그리기
            if self.die == True:
                if self.dir == 1:  # 오른쪽
                    walk_monster.clip_composite_draw(1296, 0, 109, 93, 0, 'h', self.x, self.y, 40, 30)
                elif self.dir == -1:  # 왼쪽
                    walk_monster.clip_draw(1296, 0, 109, 93, self.x, self.y, 40, 30)
            else:
                if self.dir == 1:  # 오른쪽
                    walk_monster.clip_composite_draw(int(self.frame) * 81, 0, 81, 93, 0, 'h', self.x, self.y, 30, 30)

                elif self.dir == -1:  # 왼쪽
                    walk_monster.clip_draw(int(self.frame) * 81, 0, 81, 93, self.x, self.y, 30, 30)

        elif self.kind == 1:                               # 부끄부끄 그리기
            if self.dir == 1:  # 오른쪽
                fly_monster.clip_composite_draw(int(self.frame) * 40, 0, 40, 40, 0, 'h', self.x, self.y, 45, 45)

            elif self.dir == -1:  # 왼쪽
                fly_monster.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 45, 45)


class Block:                         # 블럭

    left = 0
    right = 0
    top = 0
    bottom = 0
    kind = 0

    def __init__(self, left, right, top, bottom, kind):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.kind = kind

    def draw(self):
        if self.kind == 0:              # 땅
            walk_monster.clip_draw(60, 60, 1, 1, self.left, self.bottom, self.right-self.left, self.top-self.bottom)
        elif self.kind == 1:            # 파이프
            pass

def player_ground_crush(A,B):
    if sonic.size == 48:
        if A.y+24 > B.bottom and A.y-24 < B.top and A.x+16 > B.left and A.x-16 < B.left:
            return 1
        if A.y+24 > B.bottom and A.y-24 < B.top and A.x+16 > B.right and A.x-16 < B.right:
            return 2
        if A.y+25 > B.bottom and A.y-24 < B.bottom and A.x+16 > B.left and A.x-16 < B.right:
            return 4
        if A.y+24 > B.top and A.y-25 < B.top and A.x+16 > B.left and A.x-16 < B.right:
            return 3
        else:
            return 0
    elif sonic.size == 60:
        if A.y+30 > B.bottom and B.top > A.y-29 and A.x+20 > B.left and B.left > A.x-20:
            return 1
        if A.y+30 > B.bottom and B.top > A.y-29 and A.x-20 < B.right and B.right < A.x+20:
            return 2
        if A.y-30 < B.bottom and A.y+30 > B.bottom and A.x+20 > B.left and B.right > A.x-20:
            return 4
        if A.y-31 < B.top and A.y+30 > B.top and A.x+20 > B.left and B.right > A.x-20:
            return 3
        else:
            return 0

def crush(A, B):
    if A.y + 20 > B.bottom and A.y - 20 < B.top and A.x + 20 > B.left and A.x - 20 < B.left:
        return 1
    if A.y + 20 > B.bottom and A.y - 20 < B.top and A.x + 20 > B.right and A.x - 20 < B.right:
        return 2
    if A.y + 21 > B.bottom and A.y - 20 < B.bottom and A.x + 20 > B.left and A.x - 20 < B.right:
        return 4
    if A.y + 20 > B.top and A.y - 21 < B.top and A.x + 20 > B.left and A.x - 20 < B.right:
        return 3

    else:
        return 0

def backmove():
    global bmx
    global bmy
    global sonic

    if sonic.dir == 1:
        bmx -= sonic.plus_move
    elif sonic.dir == -1:
        bmx += sonic.plus_move

def draw_back():                                   # 배경 그리기
    stage1_1.clip_draw(0, 0, 2357, 314, 1178.5*2.7+bmx, 157*2.7+bmy, 2357*2.7, 314*2.7)

def enter():
    global sonic, b, wm, ite
    global WIDTH, HEIGHT, frame, x, y, walk_monster, point, coin, firesonic, point, money
    global sonic_sprite, stage1_1, num, score, it, star, flower, fly_monster

    sonic_sprite = load_image('sonic.png')
    walk_monster = load_image('walk_monster.png')
    fly_monster = load_image('fly_monster.png')
    stage1_1 = load_image('1-1-1.png')
    num = load_image('number.png')
    score = load_image('score.png')
    it = load_image('item.png')
    star = load_image('starsonic.png')
    firesonic = load_image('firesonic.png')
    coin = load_image('coin.png')
    flower = load_image('flower.png')

    WIDTH = 1000
    HEIGHT = 800

    b = [Block(0, 930, 25, 0, 0), Block(930, 1000, 70, 0, 0)]
    wm = [Monster(100,100,0.2,0),Monster(100,100,0.2,1),Monster(100,100,0.4,0),Monster(100,100,0.7,0)]
    ite = [item(500, 100, 1),item(500, 100, 2),item(100, 20, 0),item(100, 40, 0),item(150, 40, 3)]

    sonic = player(30, 60)
    bmx = 0
    bmy = 0
    point = 0
    money = 0

def exit():
    global sonic, b,wm, ite
    global WIDTH, HEIGHT, frame, x, y, money, point,flower
    global sonic_sprite, stage1_1, num, score,star, it, coin,firesonic

    del(sonic_sprite)
    del(stage1_1)
    del(flower)
    del(sonic)
    del(b)
    del(num)
    del (score)
    del(ite)
    del(it)
    del(star)
    del(coin)
    del(firesonic)
    del(money)
    del(point)

def handle_events():
    global sonic
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 끄기
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:  # 키 다운
            if sonic.die == False:
                if event.key == SDLK_RIGHT:  # 오른쪽
                    sonic.plus_move = 0
                    sonic.dir2 = 1
                    sonic.dir += 1
                elif event.key == SDLK_LEFT:  # 왼쪽
                    sonic.plus_move = 0
                    sonic.dir2 = -1
                    sonic.dir -= 1
                elif event.key == SDLK_DOWN:  # 아래
                    sonic.GoDown = True
                elif event.key == SDLK_ESCAPE:  # ESC
                    game_framework.change_state(Select_state)
                elif event.key == SDLK_SPACE:  # 스페이스
                    if sonic.jumpcount == 2:
                        sonic.savey = sonic.y
                        sonic.savey2 = sonic.y
                        sonic.Jumping = True
                        sonic.jumpcount -= 1

                    elif sonic.jumpcount == 1:
                        sonic.jumpTime = 0
                        sonic.savey2 = sonic.y
                        sonic.Jumping = True
                        sonic.jumpcount -= 1

                elif event.key == SDLK_LSHIFT or event.key == SDLK_RSHIFT:  # 쉬프트
                    sonic.fast = True

        elif event.type == SDL_KEYUP:  # 키 업
            if event.key == SDLK_RIGHT:  # 오른쪽
                sonic.dir -= 1
            elif event.key == SDLK_LEFT:  # 왼쪽
                sonic.dir += 1
            elif event.key == SDLK_LSHIFT or event.key == SDLK_RSHIFT:  # 쉬프트
                sonic.fast = False

def update():
    global life
    sonic.update()
    sonic.move()
    backmove()
    for i in wm:
        i.update()
        i.move()
    for i in ite:
        i.update()
        i.move()
    if life == 0:
        game_framework.change_state(GameOver)

def draw():
    clear_canvas()
    draw_back()
    point_draw()
    for i in b:
        i.draw()
    for i in wm:
        if i.life == True:
            i.draw()
    for i in ite:
        if i.life == True:
            i.draw()
    sonic.draw()
    update_canvas()

def pause():
    pass


def resume():
    pass