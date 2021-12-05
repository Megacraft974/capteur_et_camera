from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

def divination():
    sense.show_message("Posez une question.")
    time.sleep(3)
    reponses = ['Les signes pointent vers oui.' , 'Sans aucun doute.' , 'Vous pouvez compter sur elle.']
    x,y,z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)
    boucle=True
    while boucle:
        x,y,z = sense.get_accelerometer_raw().values()
        x = abs(x)
        y = abs(y)
        z = abs(z)
        if x > 2 or y > 2 or z > 2:
            sense.show_message(random.choice(reponses))
            boucle=False
        else:
            sense.clear()
