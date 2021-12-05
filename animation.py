import picamera
from time import sleep
#from RPi import GPIO

#button = 17

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

with picamera.PiCamera() as camera:
    camera.start_preview()
    frame = 1
    while True:
        sleep(5)
#        GPIO.wait_for_edge(button, GPIO.FALLING)
        camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        frame += 1
    camera.stop_preview()
