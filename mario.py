from random import randint
from pico2d import *
from math import *


WIDTH, HEIGHT = 1000, 800

running = True
game = 0
fly_frame = 0
frame = 0
main_frame = 0
main_move = False

x, y = 60, 60

def crush(A,B):
    if y+30 > B.bottom and B.top > y-30 and x+30 > B.left and B.left > x-30:
        return 1
    elif y+30 > B.bottom and B.top > y-30 and x-30 < B.right and B.right < x+30:
        return 2
    if y-30 < B.top and y+10 > B.top and x+30 > B.left and B.right > x-30:
        return 3
    else:
        return 0

class player:
    global running
    global game
    global x
    global y
    global frame
    ground = True
    dir = 0
    dir2 = 1
    gravity = 5
    jumpPower = 40
    jumpTime = 0
    left = x - 30
    right = x + 30
    top = y - 30
    bottom = y + 30
    savey = 0
    savey2 = 0
    jumpcount = 2
    Jumping = False
    fast = False
    plus_move = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def handle_events(self):

        global running
        global game
        global x
        global y
        global frame

        events = get_events()
        for event in events:

            if game == 0:  # 대기 화면
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_KEYDOWN:  # 키 다운
                    if event.key == SDLK_SPACE:  # 스페이스
                        game = 1

            elif game == 1:  # 게임 선택
                if event.type == SDL_QUIT:  # 끄기
                    running = False

                elif event.type == SDL_KEYDOWN:  # 키 다운
                    if event.key == SDLK_RIGHT:  # 오른쪽
                        self.plus_move = 0
                        self.dir2 = 1
                        self.dir += 1
                    elif event.key == SDLK_LEFT:  # 왼쪽
                        self.plus_move = 0
                        self.dir2 = -1
                        self.dir -= 1
                    elif event.key == SDLK_ESCAPE:  # ESC
                        self.running = False
                    elif event.key == SDLK_SPACE:  # 스페이스
                        if self.jumpcount == 2:
                            self.savey = y
                            self.savey2 = y
                            self.Jumping = True
                            self.jumpcount -= 1

                        elif self.jumpcount == 1:
                            self.jumpTime = 0
                            self.savey2 = y
                            self.Jumping = True
                            self.jumpcount -= 1

                    elif event.key == SDLK_LSHIFT or event.key == SDLK_RSHIFT:  # 쉬프트
                        self.fast = True

                elif event.type == SDL_KEYUP:  # 키 업
                    if event.key == SDLK_RIGHT:  # 오른쪽
                        self.dir -= 1
                    elif event.key == SDLK_LEFT:  # 왼쪽
                        self.dir += 1
                    elif event.key == SDLK_LSHIFT or event.key == SDLK_RSHIFT:  # 쉬프트
                        self.fast = False

    def draw(self):

        global running
        global game
        global x
        global y
        global frame

        self.left = x - 30
        self.right = x + 30
        self.top = y - 30
        self.bottom = y + 30



        if game == 1:
            self.left = x - 30
            self.right = x + 30
            self.top = y - 30
            self.left = x - 30

            if self.Jumping:
                y = (self.jumpTime * self.jumpTime * (-self.gravity) / 2) + (self.jumpTime * self.jumpPower) + self.savey2
                self.jumpTime += 1
                if y < self.savey:
                    y = self.savey
                    self.Jumping = False
                    self.jumpTime = 0.0
                    self.jumpcount = 2

            if self.dir == 1:                        # 오른쪽
                if self.fast:                       # 대시
                    sonic_sprite.clip_draw(int(frame) * 40, 380, 40, 40, x, y, 60, 60)
                else:
                    if self.Jumping:
                        sonic_sprite.clip_draw(int(frame) * 40, 340, 40, 40, x, y, 60, 60)
                    else:
                        sonic_sprite.clip_draw(int(frame) * 40, 460, 40, 40, x, y, 60, 60)

            elif self.dir == -1:                     # 왼쪽
                if self.fast:                       # 대시
                    sonic_sprite.clip_composite_draw(int(frame) * 40, 380, 40, 40, 0, 'h', x, y, 60, 60)
                else:
                    if self.Jumping:
                        sonic_sprite.clip_composite_draw(int(frame) * 40, 340, 40, 40, 0, 'h', x, y, 60, 60)
                    else:
                        sonic_sprite.clip_composite_draw(int(frame) * 40, 460, 40, 40, 0, 'h', x, y, 60, 60)

            elif self.dir == 0 and self.dir2 == 1:        # 마지막이 오른쪽이였던 멈춤
                sonic_sprite.clip_draw(int(frame) * 40, 420, 40, 40, x, y, 60, 60)

            elif self.dir == 0 and self.dir2 == -1:       # 마지막이 왼쪽이였던 멈춤
                sonic_sprite.clip_composite_draw(int(frame) * 40, 420, 40, 40, 0, 'h', x, y, 60, 60)

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

            if x > 970 and self.dir != -1:
                x = 970
            elif x < 30 and self.dir != 1:
                x = 30
            else:
                if self.fast and self.dir != 0:  # 대시 on
                    x += (self.dir * 2) + (self.dir2 * self.plus_move)
                    delay(0.04)
                else:  # 대시 off
                    x += self.dir2 * self.plus_move
                    delay(0.04)
            for i in p:
                if crush(self, i) == 1:
                    x = i.left-30
                elif crush(self, i) == 2:
                    x = i.right+30
                if crush(self, i) == 3:
                    y = i.top+30
                    self.savey = y

class Ground:                         # 파이프
    global game

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
        self.kind = 0 # 땅

    def draw(self):

        global game

        if game == 1:
            if self.kind == 0:
                pass
class Pipe:                         # 파이프
    global game

    left = 0
    right = 0
    top = 0
    bottom = 0

    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def draw(self):

        global game

        if game == 1:
            pipe.clip_draw(0, 300-(self.top-self.bottom), 100, (self.top-self.bottom), (self.right+self.left)/2, (self.top+self.bottom)/2)



p = [Pipe(200,300,150,30),Pipe(450,550,200,30),Pipe(700,800,250,30)]
g = [Ground(0,930,0,25),Ground(930,1000,0,70)]

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

while running:
    clear_canvas()

    draw_back()                                     # 배경 그리기
    player.draw(player)                             # 플레이어 그리기
    for i in p:                                     # 파이프 그리기
        i.draw()
    update_canvas()
    player.handle_events(player)

    if player.dir == 0:                              # 프레임
        frame = (frame + 0.5) % 8
    else:
        frame = (frame + 1) % 8

    fly_frame = (fly_frame + 1) % 16



close_canvas()