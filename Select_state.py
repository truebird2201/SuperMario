from random import randint
from pico2d import *
import game_framework
import Title_state
from math import *


sonic_sprite = load_image('sonic.png')
coin = load_image('coin.png')
red_coin = load_image('red_coin.png')
fly = load_image('fly_monster.png')
main_back = load_image('main_back.png')
main_sonic = load_image('main_sonic.png')
name = load_image('LeeSeoYeon.png')
Title = load_image('SuperSonic.png')
press = load_image('press.png')
pipe = load_image('pipe.png')
stage1 = load_image('world1-1.png')
select = load_image('select_back.png')
select_Stage = load_image('select_Stage.png')
select_Stage2 = load_image('select_Stage2.png')



fly_frame = 0
main_frame = 0
main_move = False



class player:
    global running
    global game

    frame =0
    ground = True
    dir = 0
    dir2 = 1
    gravity = 5
    jumpPower = 40
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
    plus_move = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def handle_events(self):

        global running
        global game
        global frame

        events = get_events()
        for event in events:

            if game == 0:  # 대기 화면
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_KEYDOWN:  # 키 다운
                    if event.key == SDLK_SPACE:  # 스페이스
                        game = 1

    def update(self):
        if sonic.dir == 0:  # 프레임
            self.frame = (self.frame + 0.5) % 8
        else:
            self.frame = (self.frame + 1) % 8
        self.left = self.x - 30
        self.right = self.x + 30
        self.top = self.y - 30
        self.bottom = self.y + 30

    def move(self):
        if self.dir != 0 and self.plus_move < 15:
            self.plus_move += 1
            if self.plus_move > 15:
                self.plus_move = 15

        elif self.dir == 0 and self.plus_move > 0:
            self.plus_move -= 2
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
                self.x += (self.dir * 2) + (self.dir2 * self.plus_move)
                delay(0.04)
            else:  # 대시 off
                self.x += self.dir2 * self.plus_move
                delay(0.04)
        self.Ground = False

        for i in b:
            if crush(self, i) == 3:
                self.Ground = True
                self.downpower = 0

        if self.Ground == False:
            self.y -= 3 + self.downpower
            self.downpower += 4

        for i in b:
            if crush(self, i) == 1:
                self.x = i.left - 20
            elif crush(self, i) == 2:
                self.x = i.right + 20
            elif crush(self, i) == 3:
                if self.GoDown == True and i.kind == 1:
                    self.GoDown2 = True
                    self.frame = 0
                    self.GoDown = False
                self.y = i.top + 30
                self.savey = self.y

    def draw(self):

        global running
        global game

        if self.Jumping:
            self.y = (self.jumpTime * self.jumpTime * (-self.gravity) / 2) + (self.jumpTime * self.jumpPower) + self.savey2
            self.jumpTime += 1
            if self.y < self.savey:
                self.y = self.savey
                self.Jumping = False
                self.jumpTime = 0.0
                self.jumpcount = 2

        if self.GoDown2 == True:
            sonic_sprite.clip_draw(int(self.frame) * 40, 300, 40, 40, self.x, self.y, 60, 60)
            if self.frame > 7:
                delay(0.2)
                game = 0
                self.GoDown2 = False
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

class Block:                         # 파이프
    global game

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

        global game

        if game == 1:
            if self.kind == 0:              # 땅
                pass
            elif self.kind == 1:
                    pipe.clip_draw(0, 300 - (self.top - self.bottom), 100, (self.top - self.bottom),(self.right + self.left) / 2, (self.top + self.bottom) / 2)

def crush(A,B):

    if y+30 > B.bottom and B.top > y-30 and x+20 > B.left and B.left > x-20:
        return 1
    elif y+30 > B.bottom and B.top > y-30 and x-20 < B.right and B.right < x+20:
        return 2
    if y-31 < B.top and y+30 > B.top and x+20 > B.left and B.right > x-20:
        return 3
    elif y-20 > B.bottom and y+20 < B.bottom and x+20 > B.left and B.right > x-20:
        return 4
    else:
        return 0

b = [Block(200,300,150,30,1),Block(450,550,200,30,1),Block(700,800,250,30,1),
     Block(0,930,25,0,0),Block(930,1000,70,0,0)]

def draw_back():                                   # 배경 그리기
    global game
    global main_frame
    global main_move

    if game == 0:
        main_back.clip_draw(0, 0, 1000, 800, 500, 400)
        main_sonic.clip_draw(0, 0, 400, 340, 150, 200 + main_frame)
        Title.clip_draw(0, 0, 1000, 300, 500, 600 - main_frame,800,200)
        name.clip_draw(0, 0, 1000, 300, 500, 750 - main_frame, 400, 120)


        if (int)(main_frame % 10) != 0:
            press.clip_draw(0, 0, 800, 300, 500, 400, 400, 150)

    elif game == 1:
        select.clip_draw(0, 0, 1000, 800, 500, 400)
        select_Stage.clip_draw(0, 0, 1000, 800, 520, 600, 800, 200 + (main_frame*3))
        select_Stage2.clip_draw(0, 0, 1000, 300, 500, 270 - (main_frame*2))

    if main_move == True:                           # 메인 움직임
        main_frame = main_frame + 0.1
    if main_frame > 20:
        main_move = False
    if main_move == False:
        main_frame = main_frame - 0.1
    if main_frame < 0:
        main_move = True



open_canvas(WIDTH, HEIGHT)

while running:
    clear_canvas()

    draw_back()                                     # 배경 그리기
    sonic.draw()                             # 플레이어 그리기
    for i in b:                                     # 파이프 그리기
        i.draw()
    update_canvas()
    sonic.handle_events()

    fly_frame = (fly_frame + 1) % 16



close_canvas()


def enter():
    global sonic, b
    global WIDTH, HEIGHT, frame, x, y

    sonic = player(30, 60)

def exit():
    global sonic, b
    global WIDTH, HEIGHT, frame, x, y
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
                game_framework.change_state(Title_state)
            elif event.key == SDLK_SPACE:  # 스페이스
                if sonic.jumpcount == 2:
                    sonic.savey = y
                    sonic.savey2 = y
                    sonic.Jumping = True
                    sonic.jumpcount -= 1

                elif sonic.jumpcount == 1:
                    sonic.jumpTime = 0
                    sonic.savey2 = y
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
    mario.update()
    mapmove()
    delay(0.001)

def draw():
    clear_canvas()
    map1.clip_draw(0, 0, 4222, 624, 2110 * 2.5 + moveWinx, 120 * 2.5 + moveWiny, 4224 * 2.5, 624 * 2.5)
    mario.draw()
    update_canvas()

def pause():
    pass


def resume():
    pass