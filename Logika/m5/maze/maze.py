#створи гру "Лабіринт"!
from typing import Any
from pygame import *

from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image =  scale(load(player_image), (65, 65))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        wind.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed

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

class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        

        self.image = Surface([self.width, self.height]) 
        self.image.fill((23,58,212))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def reset(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500

wind = display.set_mode((win_width, win_height))

bk = scale(load("background.jpg"),(win_width,win_height))
player = Player("hero.png", 5,win_height - 65, 5)
villain = Enemy("cyborg.png", win_width - 150,win_height - 250, 5)
treasure = GameSprite("treasure.png", win_width-80, win_height-80, 0)


Wall1 = Wall(100, 75, 15, 450)
Wall2 = Wall(200, 0  ,15, 250)
Wall3 = Wall(200, 320, 15, 80)
Wall4 = Wall(300, 320,15, 300)
Wall5 = Wall(300, 70, 15, 180)
Wall6 = Wall(400, 0,  15, 250)
Wall7 = Wall(400, 320,15, 105)
Wall8 = Wall(500, 70, 15, 180)
Wall9 = Wall(500, 320,15, 300)
Wall10 = Wall(600, 0, 15, 250)
walls = [Wall1,Wall2,Wall3,Wall4,Wall5,Wall6,Wall7,Wall8,Wall9,Wall10]

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()

f = font.Font(None, 70)
win = f.render('MOLODEC', True, (23, 79, 146))
lose = f.render('NE MOLODEC', True, (69, 12, 99))

mixer.init()
mixer.music.load("jungles.ogg")
mixer_music.play()

final_sound = mixer.Sound('money.ogg')
kick_sound = mixer.Sound('kick.ogg')
print(True)
print(False)

flag  = 'not collide'
tick = FPS
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        wind.blit(bk, (0, 0))
        player.reset()
        villain.reset()
        treasure.reset()
        for w in walls:
            w.reset()
            if sprite.collide_rect(player,w): 
                # flag = 'collide'
                # if tick != 0 and flag == 'collide':

                #     player.rect.x -= 5
                #     tick-=2
                # else:
                #     tick = FPS
                #     flag = 'not collide'
                finish = True
                wind.blit(lose, (200, 200))
                kick_sound.play()


        player.update()
        villain.update()
        if  sprite.collide_rect(player, treasure):
            finish = True
            wind.blit(win, (200, 200))
            final_sound.play()
        if sprite.collide_rect(player,villain):
            finish = True
            wind.blit(lose, (200, 200))
            kick_sound.play()

        


    display.update()
    clock.tick(FPS)

