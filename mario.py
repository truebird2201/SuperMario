from random import randint
from pico2d import *


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

def handle_events():
    global running
    global dir
    global dir2

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir2 = 1
                dir += 1
            elif event.key == SDLK_LEFT:
                dir2 = -1
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)

sonic = load_image('sonic.png')

running = True

x2, y2 = randint(0, KPU_WIDTH), randint(0, KPU_HEIGHT)
dir = 0
dir2 = 1
frame = 0

while running:
        clear_canvas()
        if dir == 1 and dir2 == 1:
            sonic.clip_draw(int(frame) * 40, 460, 40, 40, x, y)
        elif dir == -1 and dir2 == -1:
            sonic.clip_composite_draw(int(frame) * 40, 460, 40, 40, 0, 'h', x, y, 40, 40)
        elif dir == 0 and dir2 == 1:
            sonic.clip_draw(int(frame) * 40, 420, 40, 40, x, y)
        elif dir == 0 and dir2 == -1:
            sonic.clip_composite_draw(int(frame) * 40, 420, 40, 40, 0, 'h', x, y, 40, 40)
        update_canvas()

        if dir == 0:
            frame = (frame + 0.5) % 8
        else:
            frame = (frame + 1) % 8

        handle_events()

        x += dir * 7
        delay(0.04)

close_canvas()