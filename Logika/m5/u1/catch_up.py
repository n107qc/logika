from pygame import *

#створи вікно гри
window = display.set_mode([700, 500])
display.set_caption("Доганялки")


#задай фон сцени
imgb = image.load("u1/background.png")

clock = time.Clock()
FPS = 144
SPEED = 10
bk = transform.scale(imgb,(700, 500))
#створи 2 спрайти та розмісти їх на сцені
sprite1 = transform.scale(image.load("u1/sprite1.png"),(100,100))
x1 = 200
y1 = 300

sprite2 = transform.scale(image.load("u1/sprite2.png"),(100,100))
x2 = 553
y2 = 400

game = True

while game:
    window.blit(bk, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    key_pressed = key.get_pressed()

    if key_pressed[K_LEFT] and x1 > 5:
        x1 -= SPEED
    
    if key_pressed[K_RIGHT] and x1 < 610:
        x1 += SPEED

    if key_pressed[K_UP] and y1 > 5:
        y1 -= SPEED

    if key_pressed[K_DOWN] and y1 < 400:
        y1 += SPEED

    
    if key_pressed[K_a] and x2 > 5:
        x2 -= SPEED
    
    if key_pressed[K_d] and x2 < 610:
        x2 += SPEED

    if key_pressed[K_w] and y2 > 5:
        y2 -= SPEED

    if key_pressed[K_s] and y2 < 400:
        y2 += SPEED

    display.update()
    clock.tick(FPS)



#оброби подію «клік за кнопкою "Закрити вікно"»