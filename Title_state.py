import game_framework
import Select_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('Mario_credit.png')

def exit():
    global image
    del(image)

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
    image.draw(512, 300, 1024, 600)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass