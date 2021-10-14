from random import randint
from pico2d import *
from math import *


WIDTH, HEIGHT = 1000, 800

running = True
game = 0
fly_frame = 0
frame = 0
main_frame = False
main_move = False

x, y = WIDTH // 2, HEIGHT // 2

class player:
    global running
    global game
    global x
    global y
    global frame
    global main_frame
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

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def handle_events(self):

        global running
        global game
        global x
        global y
        global frame
        global main_frame

        events = get_events()
        for event in events:

            if game == 0:  # 대기 화면
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_KEYDOWN:  # 키 다운
                    if event.key == SDLK_SPACE:  # 스페이스
                        game = 1

            elif game == 1:  # 게임 진행
                if event.type == SDL_QUIT:  # 끄기
                    running = False

                elif event.type == SDL_KEYDOWN:  # 키 다운
                    if event.key == SDLK_RIGHT:  # 오른쪽
                        self.dir2 = 1
                        self.dir += 1
                    elif event.key == SDLK_LEFT:  # 왼쪽
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
        global main_frame

        self.left = x - 30
        self.right = x + 30
        self.top = y - 30
        self.bottom = y + 30

        if game == 0:
            main_back.clip_draw(0, 0, 1000, 800, 500, 400)
            main_sonic.clip_draw(0, 0, 400, 340, 150, 200 + main_frame)
            Title.clip_draw(0, 0, 1000, 300, 500, 600 - main_frame,800,200)
            name.clip_draw(0, 0, 1000, 300, 500, 750 - main_frame, 400, 120)
            if (int)(main_frame % 10) != 0:
                press.clip_draw(0, 0, 800, 300, 500, 400, 400, 150)
            update_canvas()
            self.handle_events(player)

        elif game == 1:
            self.left = x - 20
            self.right = x + 20
            self.top = y - 20
            self.left = x - 20

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

            if self.fast and self.dir != 0:  # 대시 on
                x += self.dir * 16
                delay(0.04)
            else:  # 대시 off
                x += self.dir * 10
                delay(0.04)

        update_canvas()
        self.handle_events(player)

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

while running:
    clear_canvas()

    player.draw(player)

    if player.dir == 0:  # 프레임
        frame = (frame + 0.5) % 8
    else:
        frame = (frame + 1) % 8
    fly_frame = (fly_frame + 1) % 16

    if main_move == True:
        main_frame = main_frame + 0.2
    if main_frame > 10:
        main_move = False
    if main_move == False:
        main_frame = main_frame - 0.2
    if main_frame < 0:
        main_move = True


    else:
        pass

close_canvas()