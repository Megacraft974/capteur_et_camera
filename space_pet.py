from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()
def space_pet():
    
    p = [0, 0, 255]
    g = [255, 0, 0]
    w = [200, 200, 200]
    e = [0, 0, 0]
    y = [50, 160, 30]
    
    pet1 = [
        e, e, e, e, e, e, e, e,
        p, e, e, e, e, e, e, e,
        e, p, e, e, p, e, p, e,
        e, p, g, g, p, w, w, e,
        e, g, g, g, w, y, w, y,
        e, g, g, g, g, w, w, e,
        e, g, e, g, e, g, e, e,
        e, e, e, e, e, e, e, e
        ]
    
    pet2 = [
        e, e, e, e, e, e, e, e,
        p, e, e, e, e, e, e, e,
        e, p, e, e, p, e, p, e,
        e, p, g, g, p, w, w, e,
        e, g, g, g, w, y, w, y,
        e, g, g, g, g, w, w, e,
        e, e, g, e, g, e, e, e,
        e, e, e, e, e, e, e, e
        ]
    
    x, y, z = sense.get_accelerometer_raw().values()
    
    def walking():
        for i in range(10):
            sense.set_pixels(pet1)
            time.sleep(0.5)
            sense.set_pixels(pet2)
            time.sleep(0.5)
    
    while x<2 and y<2 and z<2:
        x, y, z = sense.get_accelerometer_raw().values()
    
    walking()
