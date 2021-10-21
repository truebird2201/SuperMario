import game_framework
import Select_state
import Start_state
from pico2d import *

main_frame = 0
main_move = False

main_back = None
main_sonic = None
name = None
Title = None
press = None

def draw_back():                                   # 배경 그리기
    global main_frame
    global main_move

    main_back.clip_draw(0, 0, 1000, 800, 500, 400)
    main_sonic.clip_draw(0, 0, 400, 340, 150, 200 + main_frame)
    Title.clip_draw(0, 0, 1000, 300, 500, 600 - main_frame, 800, 200)
    name.clip_draw(0, 0, 1000, 300, 500, 750 - main_frame, 400, 120)

    if (int)(main_frame % 10) != 0:
        press.clip_draw(0, 0, 800, 300, 500, 400, 400, 150)

def enter():
    global main_back, main_sonic, name, Title, press

    main_back = load_image('main_back.png')
    main_sonic = load_image('main_sonic.png')
    name = load_image('LeeSeoYeon.png')
    Title = load_image('SuperSonic.png')
    press = load_image('press.png')

def exit():
    global main_back, main_sonic, name, Title, press
    del(main_back)
    del(main_sonic)
    del(name)
    del(Title)
    del(press)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(Select_state)

def draw():
    clear_canvas()
    draw_back()
    update_canvas()

def update():
    global main_frame
    global main_move

    if main_move == True:                           # 메인 움직임
        main_frame = main_frame + 0.1
    if main_frame > 20:
        main_move = False
    if main_move == False:
        main_frame = main_frame - 0.1
    if main_frame < 0:
        main_move = True


def pause():
    pass


def resume():
    pass