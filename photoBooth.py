#!/usr/bin/python
import os
import pygame, sys
from pygame.locals import *
import picamera
import time
import datetime

width = 1280
height = 720
 
with picamera.PiCamera() as camera:
    camera.resolution = (width, height)
    camera.framerate = 24
    camera.start_preview()
    camera.annotate_text = 'my Anottation!'
    time.sleep(2)
    camera.capture('myPic.jpg')

pygame.init()

dgryColor = pygame.Color(64,64,64)
greenColor = pygame.Color(0,255,0)
yellowColor = pygame.Color(255,255,0)
redColor = pygame.Color(255,0,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
greyColor = pygame.Color(128,128,128)
blackColor = pygame.Color(0,0,0)
purpleColor = pygame.Color(255,0,255)
lgryColor = pygame.Color(192,192,192)

windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
pygame.display.set_caption(' Text on Image ')

# load image
imagefile = ('myPic.jpg')
image = pygame.image.load(imagefile)
windowSurfaceObj.blit(image,(0,0))
pygame.display.flip()

# define time format and colors
now = datetime.datetime.now()
msg = now.strftime("%Y/%m/%d %H:%M:%S")
fsize = 16 #font size
textcolor = 5 # 0 to 9
backcolor = 0 # 0 to 9, -1 for no background
fx = 1  # x position of text
fy = height - fsize # y postion of text

# put text on image and save
colors = [dgryColor,yellowColor,redColor,greenColor,blueColor,whiteColor,greyColor,blackColor,purpleColor,lgryColor]
tcolor = colors[textcolor]
lt = (len(msg) * (fsize/2))
if backcolor > -1:
   bcolor = colors[backcolor]
   pygame.draw.rect(windowSurfaceObj,bcolor,Rect(fx,fy, lt, fsize))
fontObj = pygame.font.Font('freesansbold.ttf',fsize)
msgSurfaceObj = fontObj.render(msg, False,tcolor)
msgRectobj = msgSurfaceObj.get_rect()
msgRectobj.topleft =(fx,fy)
windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
pygame.display.update(pygame.Rect(fx,fy,lt,fsize))
pygame.image.save(windowSurfaceObj,'myPic.jpg')
pygame.display.quit()
