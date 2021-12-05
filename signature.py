from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def signature():
    r = (255, 0, 0)
    b = (0, 0, 255)
    g = (0, 0, 0)
    w = (200, 200, 200)
    

    fond = [
        r,g,g,g,g,g,g,r,
        g,r,g,g,g,g,r,g,
        g,r,g,r,r,g,r,g,
        g,g,r,r,r,r,g,g,
        g,g,b,b,b,b,g,g,
        g,b,g,b,b,g,b,g,
        g,b,g,g,g,g,b,g,
        g,b,g,g,g,g,b,g]

    fond2 = [
        r,w,w,w,w,w,w,r,
        w,r,w,w,w,w,r,w,
        w,r,w,r,r,w,r,w,
        w,w,r,r,r,r,w,w,
        w,w,b,b,b,b,w,w,
        w,b,w,b,b,w,b,w,
        w,b,w,w,w,w,b,w,
        w,b,w,w,w,w,b,w]

    sense.show_message("Cree par William Michaud:")
    for o in range(0, 15):
        acc = sense.get_accelerometer_raw()
        x2 = acc["x"]
        y2 = acc["y"]
        z2 = acc["z"]
        x2 = round(x2, 0)
        y2 = round(y2, 0)
        if x2 == -1:
            sense.set_rotation(90)
        elif y2 == 1:
            sense.set_rotation(0)
        elif y2 == -1:
            sense.set_rotation(180)
        else:
            sense.set_rotation(270)
        sense.set_pixels(fond)
        sleep(0.5)
        sense.set_pixels(fond2)
        sleep(0.5)
        
