#створи гру "Лабіринт"!
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
        win.blit(self.image,(self.rect.x, self.rect.y))


win_width = 700
win_height = 500

win = display.set_mode((win_width, win_height))

bk = scale(load("background.jpg"),(win_width,win_height))
player = GameSprite("hero.png", 5,win_height - 65, 4)
villain = GameSprite("cyborg.png", win_width - 150,win_height - 250, 2)


game = True
clock = time.Clock()
FPS = 144

mixer.init()
mixer.music.load("jungles.ogg")
mixer_music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    win.blit(bk, (0, 0))
    player.reset()
    villain.reset()



    display.update()
    clock.tick(FPS)

