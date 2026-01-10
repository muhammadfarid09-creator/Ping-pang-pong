
from pygame import *

background_color = (238, 255, 208)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('pingpong')
window.fill(background_color)


game = True

while  game:
    for e in event.get ():
        if e.type == QUIT:
            game = False


    display.update()