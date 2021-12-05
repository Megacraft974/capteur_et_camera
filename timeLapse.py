import picamera
from os import system
from time import sleep
            
camera = picamera.PiCamera()
camera.resolution = (1024, 768)

rangeRepeat = int(input("Range :"))
time = int(input("Interval: "))
image="e.jpg"

for i in range(rangeRepeat):
    camera.start_preview()
    #camera.capture('image{0:04d}.jpg'.format(i))
    camera.capture(image)
    sleep(time)
    camera.stop_preview()

system('convert -delay 10 -loop 0 image*.jpg animation.gif')
