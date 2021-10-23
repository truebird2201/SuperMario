from random import randint
from pico2d import *
import game_framework
import Select_state
import stage1_2
from math import *

sonic_sprite = None
walk_monster = None
stage1_1 = None
bmx = 0
bmy = 0


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

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        if sonic.dir == 0:  # 프레임
            self.frame = (self.frame + 0.015) % 8
        else:
            self.frame = (self.frame + 0.03) % 8
        self.left = self.x - 20
        self.right = self.x + 20
        self.top = self.y + 30
        self.bottom = self.y - 30

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

        if self.dir != 0 and self.plus_move < 1.0:
            self.plus_move += 0.01
            if self.plus_move > 1.0:
                self.plus_move = 1.0

        elif self.dir == 0 and self.plus_move > 0:
            self.plus_move -= 0.01
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
                self.x += (self.dir * 0.05) + (self.dir2 * self.plus_move)
            else:  # 대시 off
                self.x += self.dir2 * self.plus_move / 2
        self.Ground = False

        for i in b:
            if crush(self, i) == 3:
                self.Ground = True
                self.downpower = 0

        if self.Ground == False:
            self.savey = 0
            if self.Jumping == False:
                self.y -= 0.2 + self.downpower
                self.downpower += 0.015

        for i in b:
            if crush(self, i) == 1:
                self.x = i.left - 20
            elif crush(self, i) == 2:
                self.x = i.right + 20
            elif crush(self, i) == 3:
                self.y = i.top + 30
                self.savey = self.y

    def draw(self):
        if self.GoDown2 == True:
            sonic_sprite.clip_draw(int(self.frame) * 40, 300, 40, 40, self.x, self.y, 60, 60)
            if self.frame > 7:
                delay(0.2)
                self.GoDown2 = False
                game_framework.change_state(stage1_2)
        else:
            if self.dir == 1:  # 오른쪽
                if self.fast:  # 대시
                    sonic_sprite.clip_draw(int(self.frame) * 40, 380, 40, 40, self.x, self.y, 60, 60)
                else:
                    if self.Jumping:
                        sonic_sprite.clip_draw(int(self.frame) * 40, 340, 40, 40, self.x, self.y, 60, 60)
                    else:
                        sonic_sprite.clip_draw(int(self.frame) * 40, 460, 40, 40, self.x, self.y, 60, 60)

            elif self.dir == -1:  # 왼쪽
                if self.fast:  # 대시
                    sonic_sprite.clip_composite_draw(int(self.frame) * 40, 380, 40, 40, 0, 'h', self.x, self.y, 60, 60)
                else:
                    if self.Jumping:
                        sonic_sprite.clip_composite_draw(int(self.frame) * 40, 340, 40, 40, 0, 'h', self.x, self.y, 60, 60)
                    else:
                        sonic_sprite.clip_composite_draw(int(self.frame) * 40, 460, 40, 40, 0, 'h', self.x, self.y, 60, 60)

            elif self.dir == 0 and self.dir2 == 1:  # 마지막이 오른쪽이였던 멈춤
                if self.Jumping == False:
                    sonic_sprite.clip_draw(int(self.frame) * 40, 420, 40, 40, self.x, self.y, 60, 60)
                else:
                    sonic_sprite.clip_draw(int(self.frame) * 40, 340, 40, 40, self.x, self.y, 60, 60)

            elif self.dir == 0 and self.dir2 == -1:  # 마지막이 왼쪽이였던 멈춤
                if self.Jumping == False:
                    sonic_sprite.clip_composite_draw(int(self.frame) * 40, 420, 40, 40, 0, 'h', self.x, self.y, 60, 60)
                else:
                    sonic_sprite.clip_composite_draw(int(self.frame) * 40, 340, 40, 40, 0, 'h', self.x, self.y, 60, 60)

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

    def __init__(self, x, y, Speed):
        self.x = x
        self.y = y
        self.Speed = Speed

    def update(self):
        self.frame = (self.frame + 0.03) % 16
        self.left = self.x - 20
        self.right = self.x + 20
        self.top = self.y + 20
        self.bottom = self.y - 20

        if crush(sonic, self) == 3:
            self.die = True
            self.frame = 0
        if self.die == True and int(self.frame) == 10:
            self.life = False

    def move(self):
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


    def draw(self):


        if self.die == True:
            if self.dir == 1:  # 오른쪽
                walk_monster.clip_composite_draw(1296, 0, 109, 93, 0, 'h', self.x, self.y, 50, 40)
            elif self.dir == -1:  # 왼쪽
                walk_monster.clip_draw(1296, 0, 109, 93, self.x, self.y, 50, 40)
        else:
            if self.dir == 1:  # 오른쪽
                walk_monster.clip_composite_draw(int(self.frame) * 81, 0, 81, 93, 0, 'h', self.x, self.y, 40, 40)

            elif self.dir == -1:  # 왼쪽
                walk_monster.clip_draw(int(self.frame) * 81, 0, 81, 93, self.x, self.y, 40, 40)


class Block:                         # 파이프

    left = 0
    right = 0
    top = 0
    bottom = 0
    kind = 0

    def __init__(self, left, right, top, bottom, kind):
        self.kind = kind
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def draw(self):
        if self.kind == 0:              # 땅
            pass
        elif self.kind == 1:
            pass

def crush(A,B):

    if A.y+30 > B.bottom and B.top > A.y-30 and A.x+20 > B.left and B.left > A.x-20:
        return 1
    if A.y+30 > B.bottom and B.top > A.y-30 and A.x-20 < B.right and B.right < A.x+20:
        return 2
    if A.y-31 < B.top and A.y+30 > B.top and A.right > B.left and B.right > A.left:
        return 3
    if A.y-30 > B.bottom and A.y+30 < B.bottom and A.right > B.left and B.right > A.left:
        return 4
    else:
        return 0

def backmove():
    global bmx
    global bmy
    global sonic

    if sonic.dir == 1:
        bmx -= sonic.plus_move/2
    elif sonic.dir == -1:
        bmx += sonic.plus_move/2

def draw_back():                                   # 배경 그리기
    stage1_1.clip_draw(0, 0, 2357, 314, 1178.5*2.7+bmx, 157*2.7+bmy, 2357*2.7, 314*2.7)

def enter():
    global sonic, b, wm
    global WIDTH, HEIGHT, frame, x, y, walk_monster
    global sonic_sprite, stage1_1

    sonic_sprite = load_image('sonic.png')
    walk_monster = load_image('walk_monster.png')
    stage1_1 = load_image('1-1-1.png')

    WIDTH = 1000
    HEIGHT = 800

    b = [Block(0, 930, 25, 0, 0), Block(930, 1000, 70, 0, 0)]
    wm = [Monster(100,100,0.2)]

    sonic = player(30, 60)

def exit():
    global sonic, b
    global WIDTH, HEIGHT, frame, x, y
    global sonic_sprite, stage1_1

    del(sonic_sprite)
    del(stage1_1)

    del(sonic)
    del(b)

def handle_events():
    global sonic
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 끄기
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:  # 키 다운
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
    sonic.update()
    sonic.move()
    backmove()
    for i in wm:
        i.update()
        i.move()

def draw():
    clear_canvas()
    draw_back()
    for i in b:
        i.draw()
    for i in wm:
        if i.life == True:
            i.draw()
    sonic.draw()
    update_canvas()

def pause():
    pass


def resume():
    pass