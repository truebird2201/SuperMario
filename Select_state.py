from random import randint
from pico2d import *
import game_framework
import Title_state
import stage1_1
import stage2_1
import stage3_1
from math import *

sonic_sprite = None
pipe = None
stage1 = None
select = None
select_Stage = None
select_Stage2 = None

lock = 1
main_frame = 0
main_move = False

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
    GoDown2 = 0
    plus_move = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Sjump = load_wav('Sjump.wav')
        self.Spipe = load_wav('Spipe.wav')

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
            self.y = (self.jumpTime * self.jumpTime * (-self.gravity) / 2) + (self.jumpTime * self.jumpPower) + self.savey2
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
                self.x += self.dir2 * self.plus_move/2
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
                if self.GoDown == True:
                    if i.kind == 1:
                        self.GoDown2 = 1
                        self.frame = 0
                        sonic.Spipe.set_volume(64)
                        sonic.Spipe.play(1)
                    if i.kind == 2 and lock < 3:
                        self.GoDown2 = 2
                        self.frame = 0
                        sonic.Spipe.set_volume(64)
                        sonic.Spipe.play(1)
                    if i.kind == 3 and lock < 2:
                        self.GoDown2 = 3
                        self.frame = 0
                        sonic.Spipe.set_volume(64)
                        sonic.Spipe.play(1)
                    self.GoDown = False
                self.y = i.top + 30
                self.savey = self.y

    def draw(self):
        if self.GoDown2 == 1 or self.GoDown2 == 2 or self.GoDown2 == 3:
            sonic_sprite.clip_draw(int(self.frame) * 40, 300, 40, 40, self.x, self.y, 60, 60)
            if self.frame > 7:
                delay(0.1)
                if self.GoDown2 == 1:
                    game_framework.change_state(stage1_1)
                if self.GoDown2 == 2:
                    game_framework.change_state(stage2_1)
                if self.GoDown2 == 3:
                    game_framework.change_state(stage3_1)
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
        self.backsound = load_music('Stitle.mp3')
        self.backsound.set_volume(64)
        self.backsound.repeat_play()

    def draw(self):
        if self.kind == 0:              # 땅
            pass
        elif self.kind == 1:
            pipe.clip_draw(0, 300 - (self.top - self.bottom), 100, (self.top - self.bottom),(self.right + self.left) / 2, (self.top + self.bottom) / 2)
        elif self.kind == 2:
            if lock > 2:
                pipe.clip_draw(100, 300 - (self.top - self.bottom), 100, (self.top - self.bottom),(self.right + self.left) / 2, (self.top + self.bottom) / 2)
            else:
                pipe.clip_draw(0, 300 - (self.top - self.bottom), 100, (self.top - self.bottom),(self.right + self.left) / 2, (self.top + self.bottom) / 2)

        elif self.kind == 3:
            if lock > 1:
                pipe.clip_draw(100, 300 - (self.top - self.bottom), 100, (self.top - self.bottom),(self.right + self.left) / 2, (self.top + self.bottom) / 2)
            else:
                pipe.clip_draw(0, 300 - (self.top - self.bottom), 100, (self.top - self.bottom),(self.right + self.left) / 2, (self.top + self.bottom) / 2)
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

def draw_back():                                   # 배경 그리기
    global main_frame
    global main_move

    select.clip_draw(0, 0, 1000, 800, 500, 400)
    select_Stage.clip_draw(0, 0, 1000, 800, 520, 450, 800, 200 + (main_frame * 3))
    select_Stage2.clip_draw(0, 0, 1000, 300, 500, 270 - (main_frame * 2))

    if main_move == True:                           # 메인 움직임
        main_frame = main_frame + 0.03
    if main_frame > 10:
        main_move = False
    if main_move == False:
        main_frame = main_frame - 0.03
    if main_frame < 0:
        main_move = True


def enter():
    global sonic, b
    global WIDTH, HEIGHT, frame, x, y
    global sonic_sprite, coin, red_coin, fly
    global pipe, stage1, select, select_Stage, select_Stage2
    sonic_sprite = load_image('sonic_sprite.png')
    pipe = load_image('pipe.png')
    select = load_image('select_back.png')
    select_Stage = load_image('select_Stage.png')
    select_Stage2 = load_image('select_Stage2.png')

    WIDTH = 1000
    HEIGHT = 800
    stage1_1.life = 3

    b = [Block(200, 300, 150, 30, 1), Block(450, 550, 200, 30, 2), Block(700, 800, 250, 30, 3),
         Block(0, 930, 25, 0, 0), Block(930, 1000, 70, 0, 0)]

    sonic = player(30, 60)

def exit():
    global sonic, b
    global WIDTH, HEIGHT, frame, x, y
    global sonic_sprite, pipe, select, select_Stage, select_Stage2
    del(sonic)
    del(pipe)
    del(select)
    del(select_Stage)
    del(select_Stage2)
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
            elif event.key == SDLK_UP:  # 스페이스
                if sonic.jumpcount == 2:
                    sonic.savey = sonic.y
                    sonic.savey2 = sonic.y
                    sonic.Jumping = True
                    sonic.jumpcount -= 1
                    sonic.Sjump.set_volume(64)
                    sonic.Sjump.play(1)

                elif sonic.jumpcount == 1:
                    sonic.jumpTime = 0
                    sonic.savey2 = sonic.y
                    sonic.Jumping = True
                    sonic.jumpcount -= 1
                    sonic.Sjump.set_volume(64)
                    sonic.Sjump.play(1)


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


def draw():
    clear_canvas()
    draw_back()
    for i in b:
        i.draw()
    sonic.draw()
    update_canvas()

def pause():
    pass


def resume():
    pass