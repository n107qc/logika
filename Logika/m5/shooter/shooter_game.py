#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

lost = 0
score = 0

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
       self.rect.y+=self.speed 
       global lost
       if self.rect.y>win_height:
           self.rect.x=randint(0, win_width-100)
           self.rect.y=0
           self.rect.x=randint(0, win_width-100)
           lost = lost + 1
           
                         

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
bk = scale(load("galaxy.jpg"),(win_width,win_height))
hero = Player("rocket.png", 5,win_height - 100, 80, 100, 5)

monsters = sprite.Group()
for i in range(2):
    villain = Enemy("ufo.png", randint(0,win_width-100), 0, 100, 80, randint(1,3))
    monsters.add(villain)
for i in range(2):
    villain2 = Enemy("asteroid.png", randint(0,win_width-100), 0, 100, 80, randint(1,3))
    monsters.add(villain2)

game = True 
finish = False



mixer.init()
mixer.music.load("space.ogg")
mixer_music.play()
mixer.music.set_volume(0.05)

font.init()
f = font.SysFont('Arial', 36)


clock = time.Clock()
FPS = 144

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(bk, (0, 0))
        txt_lose = f.render(f'Пропущено:{lost}',True,(255,255,255))
        txt_score = f.render(f'Рахунок:{score}',True,(255,255,255))
        window.blit(txt_lose, (0,50))
        window.blit(txt_score, (0,0))
        hero.reset() 
        villain.reset()
        monsters.draw(window)

        monsters.update()
        villain.update()
        hero.update()

        
                

    display.update()
    clock.tick(FPS)