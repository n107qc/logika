#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y,player_width, player_height, player_speed):
        super().__init__()
        self.image =  scale(load(player_image), (player_width, player_height))
        self.speed = player_speed
        
        self.width = player_width
        self.height = player_height
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-self.width - 10:
            self.rect.x += self.speed

    def fire(self):
        pass

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
                         
        if self.rect.x <= 110:
            self.direction = 'right'
        if self.rect.x >= win_width-80:
            self.direction = 'left'

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
bk = scale(load("galaxy.jpg"),(win_width,win_height))
hero = Player("rocket.png", 5,win_height - 100, 80, 100, 5)
villain = Enemy("ufo.png", 320, 0, 80, 80, 10)


game = True 
finish = False

font.init()
f = font.Font(None, 70)
win = f.render('MOLODEC', True, (23, 79, 146))
lose = f.render('NE MOLODEC', True, (69, 12, 99))

mixer.init()
mixer.music.load("space.ogg")
mixer_music.play()
mixer.music.set_volume(0.05)

clock = time.Clock()
FPS = 144

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(bk, (0, 0))
        hero.reset() 
        villain.reset()


        villain.reset()
        hero.update()

        if sprite.collide_rect(hero,villain):
                finish = True
                window.blit(lose, (200, 200))
                

    display.update()
    clock.tick(FPS)