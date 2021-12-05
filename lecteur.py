import pygame
from time import sleep
import picamera

def lecteur():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
    pygame.display.set_caption('Lecteur de film')
    running=True
    compteur=1
    while running:
        try:
            img = pygame.image.load(str(compteur) + '.png')
            DISPLAYSURF.blit(img)
            compteur = compteur+1
            sleep(0.5)
        except:
            running == True

def camera():
    for compteur in range(0,10):
        camera=picamera.PiCamera()
        camera.resolution = (400, 300)
        camera.capture(str(compteur) + '.png')
        sleep(1)

