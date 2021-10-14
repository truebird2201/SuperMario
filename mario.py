from random import randint
from pico2d import *
from math import *


WIDTH, HEIGHT = 1020, 800

x, y = WIDTH // 2, HEIGHT // 2

class player:
    global running
    global game
    global x
    global y
    global frame
    dir = 0
    dir2 = 1
    frame = 0
    gravity = 5
    jumpPower = 40
    jumpTime = 0
    left = x - 20
    right = x + 20
    top = y - 20
    bottom = y + 20
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

        events = get_events()
        for event in events:

            if game == 0:  # 대기 화면
                if event.type == SDL_QUIT:
                    running = False

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

        self.left = x - 20
        self.right = x + 20
        self.top = y - 20
        self.bottom = y + 20

        if game == 0:
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
                    sonic_sprite.clip_draw(int(frame) * 40, 380, 40, 40, x, y)
                else:
                    if self.Jumping:
                        sonic_sprite.clip_draw(int(frame) * 40, 340, 40, 40, x, y)
                    else:
                        sonic_sprite.clip_draw(int(frame) * 40, 460, 40, 40, x, y)

            elif self.dir == -1:                     # 왼쪽
                if self.fast:                       # 대시
                    sonic_sprite.clip_composite_draw(int(frame) * 40, 380, 40, 40, 0, 'h', x, y, 40, 40)
                else:
                    if self.Jumping:
                        sonic_sprite.clip_composite_draw(int(frame) * 40, 340, 40, 40, 0, 'h', x, y, 40, 40)
                    else:
                        sonic_sprite.clip_composite_draw(int(frame) * 40, 460, 40, 40, 0, 'h', x, y, 40, 40)

            elif self.dir == 0 and self.dir2 == 1:        # 마지막이 오른쪽이였던 멈춤
                sonic_sprite.clip_draw(int(frame) * 40, 420, 40, 40, x, y)

            elif self.dir == 0 and self.dir2 == -1:       # 마지막이 왼쪽이였던 멈춤
                sonic_sprite.clip_composite_draw(int(frame) * 40, 420, 40, 40, 0, 'h', x, y, 40, 40)

            update_canvas()


            self.handle_events(player)

            if self.fast and self.dir != 0:                           # 대시 on
                x += self.dir * 12
                delay(0.04)
            else:                                           # 대시 off
                x += self.dir * 6
                delay(0.04)



open_canvas(WIDTH, HEIGHT)

sonic_sprite = load_image('sonic.png')
coin = load_image('coin.png')
red_coin = load_image('red_coin.png')
fly = load_image('fly_monster.png')

running = True
game = 1
fly_frame = 0
frame = 0

while running:
    clear_canvas()
    player.draw(player)

    if player.dir == 0:  # 프레임
        frame = (frame + 0.5) % 8
    else:
        frame = (frame + 1) % 8
    fly_frame = (fly_frame + 1) % 16

close_canvas()