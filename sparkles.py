from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.clear()

def effet():
    for o in range(0, 500):
        x = randint(0 ,7)
        y = randint(0 ,7)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        sleep(0.1)
        sense.set_pixel(x ,y ,r ,g ,b)
        for event in sense.stick.get_events():
            if event.action =="pressed":
                print('stop')
                o = 500
