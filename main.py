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

class Player(GameSprite):
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def move_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


raket_1 =  Player('raket.png', 30, 200, 5, 40, 115)
raket_2 = Player('raket.png', 520, 200, 5, 40, 115)
ball = GameSprite('tennis_ball.png', 200, 200, 5, 40, 40)

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 35)
lose1 = font.render('PEMAIN SATU KALAH', True, (200, 0, 0))
lose2 = font.render('PEMAIN DUA KALAH', True, (200, 0, 0))




game = True
clock = time.Clock()
FPS = 60

finish = False

while  game:  
    for e in event.get ():
        if e.type == QUIT:
            game = False

    if finish != True :

        window.fill(background_color)
        raket_1.move_l()
        raket_2.move_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(raket_1, ball) or sprite.collide_rect(raket_2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True 
            window.blit(lose1, (180, 200))

        if ball.rect.x > win_width:
            finish = True 
            window.blit(lose2, (180, 200))
        
        raket_1.reset()
        raket_2.reset() 
        ball.reset()


    display.update()
    clock.tick(FPS)




    display.update()
    clock.tick(FPS)


