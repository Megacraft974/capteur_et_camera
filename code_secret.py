def code_secret():
    ##### Libraries #####
    from sense_hat import SenseHat
    from time import sleep
    import random

    ##### Functions #####
    def Secousses():
        o=1
        while o==1:
            x, y, z = sense.get_accelerometer_raw().values()
            
            x = abs(x)
            y = abs(y)
            z = abs(z)
            
            if x > 3 or y > 3 or z > 3:
                o=2

    def Pression():
        o = sense.get_pressure()
        o2 = o + 1
        while o < o2:
            o = sense.get_pressure()

    def Sens():
        pause = 3
        score = 0
        angle = 0
        go = True
            
        while go:
            angle2 = angle
            while angle == angle2:
                angle = random.choice([0, 90, 180, 270])
            sense.set_rotation(angle)
            sense.set_pixels(fleche)
            sleep(pause)
            
            x, y, z = sense.get_accelerometer_raw().values()
            x = round(x, 0)
            y = round(y, 0)
            print('X: '+str(x)+' Y: '+str(y))
            if x == -1 and angle == 180:
                sense.set_pixels(fleche)
                score += 1
            elif x == 1 and angle == 0:
                sense.set_pixels(fleche)
                score += 1
            elif y == -1 and angle == 90:
                sense.set_pixels(fleche)
                score += 1
            elif y == 1 and angle == 270:
                sense.set_pixels(fleche)
                score += 1
            else:
                go = False
                sense.show_message("Voleur!")
            if score == 5:
                go = False
                sense.set_rotation(0);s
                Debloque()
        sleep(0.5)

    def Verrous():
        sense.clear([0, 0, 0])
        sense.show_letter("1")
        sleep(1)
        sense.set_pixels(locked)
        Secousses()
        sense.clear([0 ,0 ,0])
        sense.show_letter("2")
        sleep(1)
        sense.set_pixels(locked)
        Pression()
        sense.clear([0 ,0 ,0])
        sense.show_letter("3")
        sleep(1)
        sense.set_pixels(locked)
        Sens()
    def Debloque():
        sense.set_pixels(unlocked)
        sleep(2)
        sense.show_message("Vous avez trouves le tresor!",scroll_speed=0.1,text_colour=(255,0,0),back_colour=(0,0,255))
        boucle = 1
        while not boucle == 5 :
            sense.set_pixels(coffre)
            sleep(0.3)
            sense.set_pixels(coffre2)
            sleep(0.3)
            boucle = boucle + 1
    ##### Pixel Art #####
    r = (255, 0, 0)
    g = (0, 255, 0)
    w = (255, 255, 255)
    e = (0, 0, 0)
    j = (255,255,0)
    m = (102,51,00) 

    locked = [
    e,e,e,e,e,e,e,e,
    e,e,e,w,w,e,e,e,
    e,e,w,e,e,w,e,e,
    e,e,w,e,e,w,e,e,
    e,e,r,r,r,r,e,e,
    e,e,r,r,r,r,e,e,
    e,e,r,r,r,r,e,e,
    e,e,e,e,e,e,e,e
    ]

    unlocked = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,w,w,e,
    e,e,e,e,w,e,e,w,
    e,e,e,e,w,e,e,w,
    e,e,g,g,g,g,e,e,
    e,e,g,g,g,g,e,e,
    e,e,g,g,g,g,e,e,
    e,e,e,e,e,e,e,e
    ]

    fleche = [
    e,e,e,e,e,e,e,e,
    e,e,e,r,r,e,e,e,
    e,e,r,r,r,r,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

    coffre = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,j,j,e,e,e,
    e,e,j,j,j,j,e,e,
    e,e,m,m,m,m,e,e,
    j,e,m,m,m,m,e,j,
    e,e,m,m,m,m,e,e,
    e,e,e,e,e,e,e,e,
    ]

    coffre2 = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,j,j,e,e,e,
    e,e,j,j,j,j,e,e,
    e,j,m,m,m,m,j,e,
    e,e,m,m,m,m,e,e,
    e,e,m,m,m,m,e,e,
    e,e,e,e,e,e,e,e,
    ]

    #### Programme principal ####
    sense=SenseHat()
    sense.set_pixels(locked)
    sleep(2)

    ##### Locks #####
    Verrous()
    ##### Unlocked #####
    sense.clear()
