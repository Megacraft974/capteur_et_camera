from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()

def RPG():
    global max_x,max_y,wall_chance,quit1,theMap,P_x,P_y,Wx,Wy,isWin,Quit,w,b,r,v
    max_x = 50
    max_y = max_x
    wall_chance = 4
    quit1 = 0
    theMap = []
    P_x = round(max_x/2)
    P_y = round(max_y/2)
    Wx = random.randint(11,max_x-9)
    Wy = random.randint(11,max_y-9)

    isWin = False
    Quit = False

    w=(200,200,200)
    b=(0,0,250)
    r=(250,0,0)
    v=(0,250,0)
    
    Map()  
    Player()

def Map():
    global theMap,w,b,r,Wx,Wy
    x = 0
    while x < max_x:
        theMap.append([])
        y = 0
        while y < max_y:
            if random.randint(0,wall_chance) == 1:
                theMap[x].append(w)
            else:
                theMap[x].append(b)
            if x <= 10:
                theMap[x][y] = w
            elif x >= max_x-7:
                theMap[x][y] = w
            elif y >= max_y-7:
                theMap[x][y] = w
            elif y <= 10:
                theMap[x][y] = w
            y = y + 1
        x = x + 1
        
    while theMap[Wx][Wy] != b:
        Wx = random.randint(11,max_x-9)
        Wy = random.randint(11,max_y-9)
    theMap[Wy][Wx] = r

def MoveMap(pos_y,pos_x):
    toShow = []
    x = 0
    while x < 8:
        y = 0
        while y < 8:
            toShow.append(theMap[pos_x+x][pos_y+y])
            y = y + 1
        x = x + 1
    toShow[8*3+3] = v
    sense.set_pixels(toShow)
    
def Player():
    global P_x,P_y,isWin,Quit,quit1
    while isWin == False and Quit == False:
        sleep(0.2)
        last_x = P_x
        last_y = P_y
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == 'down' and P_y < max_y - 8 and theMap[P_y + 4][P_x + 3] != w:
                    P_y = P_y + 1
                elif event.direction == 'up' and P_y > 8 and theMap[P_y + 3][P_x + 3] != w:
                    P_y = P_y - 1
                elif event.direction == 'left' and P_x > 8 and theMap[P_y + 3][P_x + 2] != w:
                    P_x = P_x - 1
                elif event.direction == 'right' and P_x < max_x - 8 and theMap[P_y + 3][P_x + 4] != w:
                    P_x = P_x + 1
                if event.direction == 'middle':
                    quit1 += 1
                    print(quit1)
                    if quit1 > 4:
                        Quit = True
        
        if theMap[P_y + 3][P_x + 3] == r:
            sense.show_message('Tu as gagne!')
            isWin == True
            break
        
        if theMap[P_y + 3][P_x + 3] == w:
            P_x = last_x
            P_y = last_y

        if P_x < max_x - 7 and P_x > 7 and P_y < max_y - 7 and P_y > 7:
            MoveMap(P_x, P_y)
    if isWin == True and Quit == False:
        sense.show_message("Tu as gagne!")
