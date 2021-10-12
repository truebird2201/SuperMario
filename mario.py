from random import randint
from pico2d import *


WIDTH, HEIGHT = 1020, 800

x, y = WIDTH // 2, HEIGHT // 2

def handle_events():
    global running
    global dir
    global dir2
    global fast
    global game

    events = get_events()
    for event in events:

        if game == 0:                                   # 대기 화면
            if event.type == SDL_QUIT:
                running = False

        elif game == 1:                                 # 게임 진행
            if event.type == SDL_QUIT:          # 끄기
                running = False

            elif event.type == SDL_KEYDOWN:         # 키 다운
                if event.key == SDLK_RIGHT:     # 오른쪽
                    dir2 = 1
                    dir += 1
                elif event.key == SDLK_LEFT:    # 왼쪽
                    dir2 = -1
                    dir -= 1
                elif event.key == SDLK_ESCAPE:  # ESC
                    running = False
                elif event.key == SDLK_LSHIFT or event.key == SDLK_RSHIFT:  # 쉬프트
                    fast = True

            elif event.type == SDL_KEYUP:           # 키 업
                if event.key == SDLK_RIGHT:     # 오른쪽
                    dir -= 1
                elif event.key == SDLK_LEFT:    # 왼쪽
                    dir += 1
                elif event.key == SDLK_LSHIFT or event.key == SDLK_RSHIFT:  # 쉬프트
                    fast = False
    pass

open_canvas(WIDTH, HEIGHT)

sonic = load_image('sonic.png')
coin = load_image('coin.png')
red_coin = load_image('red_coin.png')
fly = load_image('fly_monster.png')

running = True
fast = False

game = 0
dir = 0
dir2 = 1
frame = 0
fly_frame = 0

while running:
        clear_canvas()
        if game == 0:
            update_canvas()
            handle_events()
        elif game == 1:
            fly.clip_draw(int(fly_frame) * 116, 0, 116, 115, 500, 400, 40, 40)

            if dir == 1:                        # 오른쪽
                if fast:                       # 대시
                    sonic.clip_draw(int(frame) * 40, 380, 40, 40, x, y)
                else:
                    sonic.clip_draw(int(frame) * 40, 460, 40, 40, x, y)
                coin.clip_draw(int(frame) * 20, 0, 20, 20, x+60, y)

            elif dir == -1:                     # 왼쪽
                if fast:                       # 대시
                    sonic.clip_composite_draw(int(frame) * 40, 380, 40, 40, 0, 'h', x, y, 40, 40)
                else:
                    sonic.clip_composite_draw(int(frame) * 40, 460, 40, 40, 0, 'h', x, y, 40, 40)
                red_coin.clip_draw(int(frame) * 20, 0, 20, 20, x + 60, y)

            elif dir == 0 and dir2 == 1:        # 마지막이 오른쪽이였던 멈춤
                sonic.clip_draw(int(frame) * 40, 420, 40, 40, x, y)

            elif dir == 0 and dir2 == -1:       # 마지막이 왼쪽이였던 멈춤
                sonic.clip_composite_draw(int(frame) * 40, 420, 40, 40, 0, 'h', x, y, 40, 40)

            update_canvas()

            if dir == 0:                                    # 프레임
                frame = (frame + 0.5) % 8
            else:
                frame = (frame + 1) % 8

            fly_frame = (fly_frame + 1) % 16

            handle_events()

            if fast and dir != 0:                           # 대시 on
                x += dir * 10
                delay(0.04)
            else:                                           # 대시 off
                x += dir * 6
                delay(0.04)


close_canvas()