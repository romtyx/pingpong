from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressd()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressd()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

BACK = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(BACK)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket_l = Player('racket.png', 30, 200, 4, 50, 150)
racket_r = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball2.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
losel = font.render('проиграл левый игрок!', True, (200, 5, 5))
loser = font.render('проиграл правый игрок!', True, (200, 5, 5))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(BACK)
        racket_l.update_l()
        racket_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            speed_x *= -1
        if ball.rect.y > win_height - 50 or  ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(losel, (200, 200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(loser, (200, 200))
        racket_l.reset()
        racket_r.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
