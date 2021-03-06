import game_framework
import Title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0




def enter():
    global image, backsound
    image = load_image('start.png')



def exit():
    global image, backsound
    del(image)




def update():
    global logo_time, backsound, check
    if (logo_time > 1.0):
        logo_time = 0
        game_framework.change_state(Title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(500, 300)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass