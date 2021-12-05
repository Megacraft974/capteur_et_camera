from sense_hat import SenseHat
from pygame.locals import*
import pygame
import random
from time import sleep

sense = SenseHat()
sense.clear()
pygame.init()
bg = pygame.display.set_mode((1,1), 0, 24)

r = (255,0,0)
v = (0,255,0)
b = (0,0,255)
e = (0,0,0)

x = 4
x2 = 0
y2 = 0
vies = 3
sens = 1

fond = [b,b,b,b,b,b,b,b,
      b,b,b,b,b,b,b,b,
      b,b,b,b,b,b,b,b,
      b,b,b,b,b,b,b,b,
      b,b,b,b,b,b,b,b,
      b,b,b,b,b,b,b,b,
      b,r,b,r,r,b,r,b,
      b,b,b,b,b,b,b,b]

def alien():
    global run, sens, x2, y2
    for o in range(0,3):
        for i in range(0,2):
            sense.set_pixel(o + x2,i + y2,r)
    if x2 == 0 and sens == 0:
        y2 += 1
        sens == 1
    elif x2 == 5 and sens == 1:
        y2 += 1
        sens == 0
        x2 = 0
    elif sens == 1:
        x2 += 1
    if y2 >= 5 :
        run = 'Perdu!'
def invasion():
    global x
    
    run = True
    while run:
        
        if vies == 0:
            run = 'Perdu!'
            
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT and x > 0:
                    x -= 1
                elif event.key == K_RIGHT and x < 7:
                    x += 1
        sense.set_pixels(fond)
        sense.set_pixel(x,7,v)

        alien()

        sleep(1)
           
    sense.show_message(run)
invasion()
