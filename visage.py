from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

O = (0, 255, 0) # Green
X = (0, 0, 0) # Black
B = (102, 51, 0)#Brown
b = (0, 0, 255)#Blue
S = (205,133,63)#Beige
W = (255, 255, 255)#White
R = (255, 0, 0)#Red

creeper = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, X, X, O, O, X, X, O,
    O, X, X, O, O, X, X, O,
    O, O, O, X, X, O, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, O, O, X, O, O
]

steve = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, S, S, S, S, S, S, B,
    S, S, S, S, S, S, S, S,
    S, W, b, S, S, b, W, S,
    S, S, S, B, B, S, S, S,
    S, S, B, S, S, B, S, S,
    S, S, B, B, B, B, S, S
]

def visage():
    sense.set_pixels(creeper)
    sleep(5)
    sense.set_pixels(steve)
    sleep(5)
    sense.clear()
