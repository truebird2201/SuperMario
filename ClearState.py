import game_framework
import Title_state
from pico2d import *

main_frame = 0
main_move = False

back = None
press = None
backsound = None

def draw_back():                                   # 배경 그리기
    back.clip_draw(0, 0, 1000, 600, 500, 300)

def enter():
    global back,backsound

    back = load_image('clearback.png')
    backsound = load_wav('Sclear.wav')
    backsound.set_volume(64)
    backsound.play(1)

def exit():
    global back
    del(back)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

def draw():
    clear_canvas()
    draw_back()
    update_canvas()

def update():
    global main_frame
    global main_move

    if main_move == True:                           # 메인 움직임
        main_frame = main_frame + 0.1
    if main_frame > 40:
        main_move = False
    if main_move == False:
        main_frame = main_frame - 0.1
    if main_frame < 0:
        main_move = True


def pause():
    pass


def resume():
    pass