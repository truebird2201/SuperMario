
from pico2d import *
import game_framework
import Select_state
import GameOver
import stage1_1
import stage1_3

diecount=0

def point_draw():
    global point
    score.clip_draw(0, 0, 170, 80, 80, 519, 130 ,50)
    coin.clip_draw(0, 40, 20, 20, 120, 485, 20, 20)
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
    dir = 1
    gravity = 0.005
    jumpPower = 1.2
    jumpTime = 0
    downpower = 0
    savey = 0
    savey2 = 0
    jumpcount = 2
    Ground = True
    Jumping = False
    x=0



    def __init__(self, x, y, kind):
        self.x2 = x
        self.y = y
        self.kind = kind
        self.savey = y

    def update(self):
        if self.kind == 0:
            self.frame = (self.frame + 15* game_framework.frame_time) % 10
        else:
            self.frame = (self.frame + 12* game_framework.frame_time) % 10
        self.x = self.x2 + bmx
        #
        self.left = self.x - 10
        self.right = self.x + 10
        self.top = self.y + 10
        self.bottom = self.y - 10

        if self.kind == 1:
            self.x2 += self.dir * 0.7
        elif self.kind == 2:
            self.x2 += self.dir * 0.5




    def move(self):
        if self.kind == 1:                                                              # 스타
            self.y = (self.jumpTime * self.jumpTime * (-self.gravity) / 2) + (
                    self.jumpTime * self.jumpPower) + self.savey
            self.jumpTime += 1
            if self.y < self.savey:
                self.y = self.savey
                self.jumpTime = 0.0


            self.Ground = False

            if self.Ground == False:
                self.savey = 0

            for i in b:
                if crush(self, i) == 1:
                    self.dir = -1
                elif crush(self, i) == 2:
                    self.dir = 1
                elif crush(self, i) == 3:
                    self.y = i.top + 10
                    self.savey = self.y
                    self.jumpTime = 1.0
                    self.Ground = True
                    self.downpower = 0

            self.y -= 0.5
            for i in b:
                if crush(self, i) == 1:
                    self.dir = -1
                elif crush(self, i) == 2:
                    self.dir = 1
                elif crush(self, i) == 3:
                    self.y = i.top + 10


        elif self.kind == 2:                                                            # 빨간 버섯
            self.y -= 0.5
            for i in b:
                if crush(self, i) == 1:
                    self.dir = -1
                elif crush(self, i) == 2:
                    self.dir = 1
                elif crush(self, i) == 3:
                    self.y = i.top + 10

        elif self.kind == 4:                                                            # 초록 버섯
            self.y -= 0.5
            for i in b:
                if crush(self, i) == 1:
                    self.dir = -1
                elif crush(self, i) == 2:
                    self.dir = 1
                elif crush(self, i) == 3:
                    self.y = i.top + 10



    def draw(self):
        if self.kind == 0:
            coin.clip_draw(int(self.frame) * 20, 40, 20, 20, self.x, self.y,25,25)
        if self.kind == 1:
            it.clip_draw(int(self.frame) * 40, 160, 40, 40, self.x, self.y,20,20)
        elif self.kind == 2:
            it.clip_draw(0, 120, 40, 40, self.x, self.y,20,20)
        elif self.kind == 3:
            it.clip_draw(40, 120, 40, 40, self.x, self.y,20,20)
        elif self.kind == 4:
            it.clip_draw(80, 120, 40, 40, self.x, self.y,20,20)


class Fire:
    left = 0
    right = 0
    top = 0
    bottom = 0
    frame = 0
    dir = 1
    gravity = 0.01
    jumpPower = 1.5
    jumpTime = 0
    downpower = 0
    savey = 0
    savey2 = 0
    jumpcount = 2
    Ground = True
    Jumping = False
    x=0


    def __init__(self,x,y,dir):
        self.x2 = x
        self.y = y
        self.dir = dir

    def update(self):

        self.frame = (self.frame + 40* game_framework.frame_time) % 10

        self.x = self.x2
        self.left = self.x - 6
        self.right = self.x + 6
        self.top = self.y + 6
        self.bottom = self.y - 6


        for i in b:
            if crush(self, i) == 1:
                fb.remove(self)
            elif crush(self, i) == 2:
                fb.remove(self)
            elif crush(self, i) == 3:
                self.y = i.top + 20

        for i in wm:
            if i.die == False:
                if crush(self, i) != 0:
                    if i.die == False:
                        global point
                        point += 2
                    i.die = True
                    i.frame = 0
                    fb.remove(self)

        if self.left > 1000:
            fb.remove(self)
        if self.left < 0:
            fb.remove(self)


    def move(self):
        self.x2 += self.dir * 400* game_framework.frame_time

    def draw(self):
        coin.clip_draw(int(self.frame) * 20, 0, 20, 20, self.x, self.y, 20, 20)



class player:

    left = 0
    right = 0
    top = 0
    bottom = 0
    frame = 0
    dir = 0
    dir2 = 1
    gravity = 0.015
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
    firemode = True
    starcount = 0
    diedown = 0
    size = 54
    depence = False
    depencetime = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        if self.depence == True:
            self.depencetime += 1
            if self.depencetime == 400:
                self.depencetime = 0
                self.depence = False

        if self.dir == 0:  # 프레임
            self.frame = (self.frame + 8 * game_framework.frame_time) % 8
        else:
            self.frame = (self.frame + 16 * game_framework.frame_time) % 8

        if self.size == 54:                         # 버섯
            self.left = self.x - 16
            self.right = self.x + 16
            self.top = self.y + 27
            self.bottom = self.y - 27

        if self.size == 48:                       # 기본
            self.left = self.x - 16
            self.right = self.x + 16
            self.top = self.y + 24
            self.bottom = self.y - 24

        if sonic.die == False and sonic.top < 0:
            self.dir = 0
            global diecount
            diecount+=1
            enter()

        for i in ite:                                                           # 아이템 감지
            if crush(self, i) != 0:
                if i.kind == 1:                                                 # 별
                    self.starmode = True
                    self.starcount = 3500
                    ite.remove(i)
                elif i.kind == 2:                                                # 버섯
                    self.size = 54
                    ite.remove(i)
                elif i.kind == 0:                                                # 동전
                    global money
                    money += 1
                    ite.remove(i)
                    if money == 50:
                        money = 0
                        life += 1
                elif i.kind == 3:                                                # 꽃
                    self.firemode = True
                    ite.remove(i)
                    self.size = 54
                elif i.kind == 4:                                                # 초록 버섯
                    life += 1
                    ite.remove(i)

        for i in wm:
            if self.die == False and i.die == False:
                if self.starmode == False:                                                 # 스타모드가 아니라면
                    if self.depence == False and (crush(self, i) == 1 or crush(self, i) == 2):                  # 옆에서 부딪히면 소닉 죽음
                        if self.size == 60 or self.firemode == True:
                            self.size = 48
                            self.firemode = False
                            self.depence = True
                        else:
                            sonic.die = True
                            sonic.frame = 0
                            sonic.dir = 0
                    if crush(self, i) == 3:                                             # 위에서 소닉이 밟으면 굼바 죽음
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
            self.diedown -= 0.2 * game_framework.frame_time
        elif self.die == True and int(self.frame) <= 6:
            self.diedown += 1 * game_framework.frame_time

        if self.die == True and int(self.frame) == 7:  # 죽으면 초기화
            diecount += 1
            enter()

        if self.starmode == True:
            self.starcount -= 1

        if self.starcount == 0 and self.starmode == True:                           # 스타모드 끝
            self.starmode = False



    def move(self):

        if self.Jumping:                                                            # 점프
            self.y = (self.jumpTime * self.jumpTime * (-self.gravity) / 2) + (
                        self.jumpTime * self.jumpPower) + self.savey2 +0.5
            self.jumpTime += 400 * game_framework.frame_time
            if self.y < self.savey:
                self.y = self.savey
                self.Jumping = False
                self.jumpTime = 0.0
                self.jumpcount = 2

        if self.dir != 0 and self.plus_move < 250:                      # 움직이는 중
            self.plus_move += 400 * game_framework.frame_time
            if self.plus_move > 250:
                self.plus_move = 250

        elif self.dir == 0 and self.plus_move > 0:                      # 멈추고 미끄러짐
            self.plus_move -= 800 * game_framework.frame_time
            if self.plus_move < 0:
                self.plus_move = 0

        if self.dir != 0 and self.dir != self.dir2:
            self.plus_move = 0

        if self.x > 970 and self.dir != -1:
            self.x = 970
        elif self.x < 10 and self.dir != 1:
            self.x = 10
            self.dir = 0

        else:
            if self.fast and self.dir != 0:  # 대시 on
                self.x += ((self.dir * 0.2) + (self.dir2 * self.plus_move)) * game_framework.frame_time
            else:  # 대시 off
                self.x += self.dir2 * self.plus_move * game_framework.frame_time
        self.Ground = False

        for i in b:                         # 블럭 충돌
            if self.size==48:
                if self.bottom + 10 > i.top and self.bottom < i.top and self.right > i.left and self.left < i.right and self.Jumping == True:
                    self.y = i.top + 24
                    self.savey = self.y
                    self.Ground = True

                elif self.bottom + 10 > i.top and self.bottom - 1 < i.top and self.right > i.left and self.left < i.right and self.Jumping == False:
                    self.y = i.top + 24
                    self.savey = self.y
                    self.Ground = True
                    if self.GoDown == True:
                        if i.kind == 1:
                            self.GoDown2 = True
                            self.frame = 0
                            self.GoDown = False

                elif self.top+1 > i.bottom and self.bottom < i.bottom and self.right > i.left and self.left < i.right and self.Jumping==True:           # 아래 -> 위
                    self.y = i.bottom - 24
                    self.savey = 0
                    self.Jumping = False
                    self.jumpcount = 2
                    self.jumpTime = 0.0
                    if i.kind == 3:
                        if i.notused == 0:
                            i.notused = 1
                    if i.kind == 2:
                        if i.notused == 0:
                            i.notused = 1

                elif self.top > i.bottom and self.bottom < i.top and self.right > i.left and self.left < i.left:             # 왼 -> 오
                    if self.bottom + 10 > i.top and self.bottom < i.top and self.right > i.left and self.left < i.right:
                        pass
                    else:
                        self.x = i.left - 16
                        if i.kind == 1:
                            i.kind=0
                            self.GoDown2 = 1
                            self.frame = 0
                            self.GoDown = False

                elif self.top > i.bottom and self.bottom < i.top and self.right > i.right and self.left < i.right:           # 오 -> 왼
                    if self.bottom + 10 > i.top and self.bottom < i.top and self.right > i.left and self.left < i.right:
                        pass
                    else:
                        self.x = i.right + 16

            elif self.size == 54:
                if self.bottom + 10 > i.top and self.bottom < i.top and self.right > i.left and self.left < i.right and self.Jumping == True:
                    self.y = i.top + 27
                    self.savey = self.y
                    self.Ground = True

                elif self.bottom + 10 > i.top and self.bottom - 1 < i.top and self.right > i.left and self.left < i.right and self.Jumping == False:
                    self.y = i.top + 27
                    self.savey = self.y
                    self.Ground = True
                    if self.GoDown == True:
                        if i.kind == 1:
                            self.GoDown2 = True
                            self.frame = 0
                            self.GoDown = False

                elif self.top + 1 > i.bottom and self.bottom < i.bottom and self.right > i.left and self.left < i.right and self.Jumping == True:  # 아래 -> 위
                    self.y = i.bottom - 27
                    self.savey = 0
                    self.Jumping = False
                    self.jumpcount = 2
                    self.jumpTime = 0.0
                    if i.kind == 3:
                        if i.notused == 0:
                            i.notused = 1
                    if i.kind == 2:
                        if i.notused == 0:
                            i.notused = 1

                elif self.top > i.bottom and self.bottom < i.top and self.right > i.left and self.left < i.left:  # 왼 -> 오
                    if self.bottom + 10 > i.top and self.bottom < i.top and self.right > i.left and self.left < i.right:
                        pass
                    else:
                        self.x = i.left - 16
                        if i.kind == 1:
                            i.kind=0
                            self.GoDown2 = 1
                            self.frame = 0
                            self.GoDown = False

                elif self.top > i.bottom and self.bottom < i.top and self.right > i.right and self.left < i.right:  # 오 -> 왼
                    if self.bottom + 10 > i.top and self.bottom < i.top and self.right > i.left and self.left < i.right:
                        pass
                    else:
                        self.x = i.right + 16


        if self.Ground == False:
            self.savey = 0
            if self.Jumping == False:
                self.y -= (400 + self.downpower) * game_framework.frame_time
                self.downpower += 400 * game_framework.frame_time


    def draw(self):

        if self.die == True:                        # 죽으면
                sonic_sprite.clip_draw(int(self.frame) * 40, 260, 40, 40, self.x, self.y-self.diedown, self.size, self.size)
        else:
            if self.GoDown2 == True:
                if self.firemode == True:
                    firesonic.clip_draw(int(self.frame) * 40, 140, 40, 40, self.x, self.y, self.size, self.size)
                else:
                    sonic_sprite.clip_draw(int(self.frame) * 40, 140, 40, 40, self.x, self.y, self.size, self.size)
                if self.frame > 7:
                    delay(0.2)
                    if self.GoDown2 == 1:
                        game_framework.change_state(stage1_3)
                    self.GoDown2 = False
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
    die = False
    global point
    x=0


    def __init__(self, x, y, Speed, kind):
        self.x2 = x
        self.y = y
        self.Speed = Speed
        self.kind = kind

    def update(self):
        if self.kind==0:                    # 굼바 프레임
            self.frame = (self.frame + 12* game_framework.frame_time) % 16

        elif self.kind == 1:                # 부끄부끄 프레임
            self.frame = (self.frame + 20* game_framework.frame_time) % 8
        self.x = self.x2+bmx
        self.left = self.x - 30
        self.right = self.x + 30
        self.top = self.y + 30
        self.bottom = self.y - 30


        if self.die == True and int(self.frame) == 10:
            wm.remove(self)

    def move(self):
        if self.kind == 0:                                      # 굼바
            self.x2 += self.dir * self.Speed*400* game_framework.frame_time
            for i in b:
                if crush(self, i) == 3:
                    if self.dir == 1:
                        if self.right > i.right:
                            self.dir = -1
                    else:
                        if self.left < i.left:
                            self.dir = 1

                if crush(self, i) == 1:
                    self.dir = -1
                if crush(self, i) == 2:
                    self.dir = 1

            self.Ground = False

            for i in b:
                if crush(self, i) == 3:
                    self.Ground = True
                    self.downpower = 0

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

    global bmx
    left = 0
    right = 0
    top = 0
    bottom = 0
    kind = 0
    frame = 0
    used = False
    notused = 0

    def __init__(self, left, right, top, bottom, kind):
        self.left2 = left
        self.right2 = right
        self.top = top
        self.bottom = bottom
        self.top2 = top
        self.bottom2 = bottom
        self.kind = kind

        # check = 0 전부
        # check = 1 왼,위,아래만
        # check = 2 우,위,아래만
        # check = 3 위,아래만

    def draw(self):
        if self.kind == 0:              # 땅
            pass
        elif self.kind == 1:            # 파이프
            pass
        elif self.kind == 2:            # 벽돌
            brick.clip_draw(int(self.frame) * 60, 180, 60, 60, self.left+(self.right-self.left)/2, self.bottom+(self.right-self.left)/2, self.right-self.left, self.top-self.bottom)
        elif self.kind == 3:            # 버섯이든 블럭
            brick.clip_draw(int(self.frame) * 60, 120, 60, 60, self.left+(self.right-self.left)/2, self.bottom+(self.right-self.left)/2, self.right-self.left, self.top-self.bottom)
        if self.used == True:
            brick.clip_draw(0, 60, 60, 60, self.left + (self.right - self.left) / 2,self.bottom + (self.right - self.left) / 2, self.right - self.left, self.top - self.bottom)


    def update(self):
        self.left = self.left2+bmx
        self.right = self.right2+bmx
        self.frame = (self.frame + 12* game_framework.frame_time) % 16

    def move(self):
        if self.notused == 1:
            self.top += 0.2
            self.bottom += 0.2
            if self.top >= self.top2 + 5.0:
                self.notused = 2

        if self.notused == 2:
            self.top -= 0.2
            self.bottom -= 0.2
            if self.top == self.top2:
                self.notused = 3
                if self.kind == 2:
                    if sonic.size== 48:
                        self.notused = 0
                    elif sonic.size == 54:
                        bb.append(BBlock(self.left2,self.right2,self.top2,self.bottom2))
                        b.remove(self)
                if self.kind == 3:
                    self.used = True

class BBlock:                         # 블럭

    global bmx
    left = 0
    right = 0
    top = 0
    bottom = 0
    kind = 0
    frame = 0
    used = False
    notused = 0
    diespeed = 0


    def __init__(self, left, right, top, bottom):
        self.left = left-5
        self.right = right+5
        self.left2 = left-5
        self.right2 = right+5
        self.top = top+5
        self.bottom = bottom-5

    def draw(self):
        brick.clip_draw(int(self.frame) * 60, 0, 60, 60, self.left+(self.right-self.left)/2, self.bottom+(self.right-self.left)/2, self.right-self.left+10, self.top-self.bottom+10)



    def update(self):
        self.frame = (self.frame + 12* game_framework.frame_time) % 16
        if self.frame > 3:
            self.frame = 3
            self.diespeed += 10 * game_framework.frame_time
        if self.top < 0:
            bb.remove(self)
        self.left = self.left2+bmx
        self.right = self.right2+bmx

    def move(self):
        if self.frame == 3:
            self.top -= self.diespeed
            self.bottom -= self.diespeed


def crush(A,B):
    if A.top > B.bottom and A.bottom < B.top and A.right > B.left and A.left < B.left:
        return 1
    if A.top > B.bottom and A.bottom < B.top and A.right > B.right and A.left < B.right:
        return 2
    if A.top+1 > B.bottom and A.bottom < B.bottom and A.right > B.left and A.left < B.right:
        return 4
    if A.top > B.top and A.bottom-1 < B.top and A.right > B.left and A.left < B.right:
        return 3
    return 0




def backmove():
    global bmx
    global bmy
    global sonic

    if sonic.dir == 1:
        if bmx > -370 and sonic.x > 400:
            if sonic.x - 0.6 <= 400:
                bmx -= sonic.plus_move* game_framework.frame_time
            else:
                bmx -= sonic.plus_move*2* game_framework.frame_time
            sonic.x -= sonic.plus_move*2* game_framework.frame_time
            if sonic.x < 400:
                sonic.x = 400
    elif sonic.dir == -1:
        if bmx < 0 and sonic.x < 600:
            if sonic.x - 0.6 >= 600:
                bmx += sonic.plus_move* game_framework.frame_time
            else:
                bmx += sonic.plus_move*2* game_framework.frame_time
            sonic.x += sonic.plus_move*2* game_framework.frame_time
            if sonic.x > 600:
                sonic.x = 600

def draw_back():                                   # 배경 그리기
    stage1_2.clip_draw(0, 0, 508, 187, 254*2.7+bmx, 187*1.6+bmy, 508*2.7, 187*3.2)

def enter():
    global sonic, b, wm, ite, fb, bb, life, diecount
    global WIDTH, HEIGHT, frame, x, y, walk_monster, point, coin, firesonic, money
    global sonic_sprite, stage1_2, num, score, it, star, fly_monster, brick, bmx, bmy

    sonic_sprite = load_image('sonic_sprite.png')
    walk_monster = load_image('walk_monster.png')
    fly_monster = load_image('fly_monster.png')
    stage1_2 = load_image('1-1-2.png')
    num = load_image('number.png')
    score = load_image('score.png')
    it = load_image('item.png')
    star = load_image('starsonic.png')
    firesonic = load_image('firesonic.png')
    coin = load_image('coin.png')
    brick = load_image('brick.png')

    WIDTH = 1000
    HEIGHT = 800

    b = [Block(-100, 513, 35, 0, 0), Block(-10, 30, 514, 0, 0), Block(600, 1400, 35, 0, 0)
        , Block(994, 1200, 90, 0, 0), Block(1124, 1400, 140, 0, 0), Block(1250, 1400, 510, 0, 0)
        , Block(1195, 1400, 245, 0, 1)]

    wm = []
    ite = []
    fb = []
    bb = []

    sonic = player(77, 400)
    bmx = 0
    bmy = 0

    point = stage1_1.point
    money = stage1_1.money
    life = stage1_1.life - diecount


def exit():
    global sonic, b, wm, ite
    global WIDTH, HEIGHT, frame, x, y, money, point
    global sonic_sprite, stage1_2, num, score, star, it, coin, firesonic, brick

    del (sonic_sprite)
    del (stage1_2)
    del (sonic)
    del (b)
    del (num)
    del (score)
    del (ite)
    del (it)
    del (star)
    del (coin)
    del (firesonic)
    del (brick)

def handle_events():
    global sonic
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 끄기
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:  # 키 다운
            if sonic.die == False and sonic.GoDown2 == False:
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
                elif event.key == SDLK_SPACE:  # 스페이스
                    if sonic.firemode == True:
                        fb.append(Fire(sonic.x,sonic.y,sonic.dir2))
                elif event.key == SDLK_ESCAPE:  # ESC
                    game_framework.change_state(Select_state)
                elif event.key == SDLK_j:
                    wm.append(Monster(100, 100, 0.2, 0))
                elif event.key == SDLK_k:
                    wm.append(Monster(500, 200, 0.2, 1))
                elif event.key == SDLK_l:
                    ite.append(item(sonic.x+100+bmx, sonic.y, 0))
                elif event.key == SDLK_r:
                    sonic.dir=0
                elif event.key == SDLK_UP:  # 위
                    if sonic.jumpcount == 2:
                        sonic.savey = sonic.y
                        sonic.savey2 = sonic.y
                        sonic.Jumping = True
                        sonic.jumpcount -= 1
                        if sonic.size == 60:
                            sonic.y += 10

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
    for i in b:
        i.update()
        i.move()
    for i in wm:
        i.update()
        i.move()
    for i in ite:
        i.update()
        i.move()
    for i in fb:
        i.update()
        i.move()
    for i in bb:
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
        i.draw()
    for i in ite:
        i.draw()
    for i in fb:
        i.draw()
    for i in bb:
        i.draw()
    if sonic.depencetime % 2 == 0:
        sonic.draw()
    update_canvas()

def pause():
    pass


def resume():
    pass