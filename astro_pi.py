from sense_hat import SenseHat
from app import*
from time import sleep

x=0
y=0
clique = 0
r=(255,0,0)
e=(0,0,255)
a=(0,255,0)

fond = [
    e,e,e,e,e,e,e,r,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    a,a,a,a,a,a,a,a,
    ]

sense = SenseHat()
sense.set_pixels(fond)
sense.set_pixel(0, 0, 255,0,0)

def apps(x):
    x=x+1
    if x ==1:
        a1()
    elif x==2:
        b2()
    elif x==3:
        c3()
    elif x==4:
        d4()
    elif x==5:
        e5()
    elif x==6:
        f6()
    elif x==7:
        g7()
    elif x==8:
        h8()
pos1x2=['right','left','up','down']
pos2x2=['left','right','down','up']
pos1y2=['down','up','right','left']
pos2y2=['up','down','left','right']
pos=[]
def joystick():
    running = True
    clique = 0
    x = 0
    y = 0
    while running:
        acc = sense.get_accelerometer_raw()
        x2 = acc["x"]
        y2 = acc["y"]
        z2 = acc["z"]
        x2 = round(x2, 0)
        y2 = round(y2, 0)
        if x2 == -1:
            sense.set_rotation(90)
            pos=pos2x2
        elif y2 == 1:
            sense.set_rotation(0)
            pos=pos1y2
        elif y2 == -1:
            sense.set_rotation(180)
            pos=pos2y2
        else:
            sense.set_rotation(270)
            pos=pos1x2
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                sense.set_pixel(x, y, 0,0,255)
                if event.direction == pos[0] and y < 6:
                    y = y + 1
                elif event.direction == pos[1] and y > 0:
                    y = y - 1
                elif event.direction == pos[2] and x < 7:
                    x = x + 1
                elif event.direction == pos[3] and x > 0:
                    x = x - 1
                if event.direction == 'middle':
                    clique = 1
                else:
                    clique = 0
            if clique == 1 and y == 6:
                apps(x)
                clique = 0
                sense.set_pixels(fond)
            elif clique == 1 and y == 0 and x == 7:
                sense.clear((0,0,255))
                sleep(1)
                sense.show_message('Au revoir!',back_colour=(0,0,255))
                sense.clear()
                running = False
            else:
                sense.set_pixels(fond)
                sense.set_pixel(x, y, 255,0,0)
        
joystick()
