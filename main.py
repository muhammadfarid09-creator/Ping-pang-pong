from pygame import *

background_color = (238, 255, 208)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('pingpong')
window.fill(background_color)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

raket_1 =  GameSprite('raket.png', 30, 200, 5, 40, 115)
raket_2 = GameSprite('raket.png', 520, 200, 5, 40, 115)
ball = GameSprite('tennis_ball.png', 200, 200, 5, 40, 40)


game = True

while  game:
    for e in event.get ():
        if e.type == QUIT:
            game = False
    
    raket_1.reset()
    raket_2.reset()
    ball.reset()


    display.update()

