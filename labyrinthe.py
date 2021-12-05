from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()

r = (0, 0, 255)
c = (255,0,0)
b = (0, 0, 0)
w = (255, 255, 255)

x = 1
y = 1

maze1 = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,b,b,b,r],
        [r,r,r,r,r,r,r,r]]

maze2 = [[r,r,r,r,r,r,r,r],
        [r,b,b,r,b,r,r,r],
        [r,r,b,b,b,r,b,r],
        [r,b,b,r,b,b,b,r],
        [r,b,b,r,r,r,b,r],
        [r,b,r,r,b,b,b,r],
        [r,b,b,r,b,r,r,r],
        [r,r,r,r,r,r,r,r]]

maze = []
win=[(7, 5), (3, 7), (4, 2), (7, 3)]

        
def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 1 < pitch < 179 and x != 0:
        new_x -= 1
    elif 359 > pitch > 179 and x != 7:
        new_x += 1
    if 1 < roll < 179 and y != 7:
        new_y += 1
    elif 359 > roll > 179 and y != 0 :
        new_y -= 1
    x,y = check_wall(x,y,new_x,new_y)
    return x,y

def check_wall(x,y,new_x,new_y):
    if maze[new_y][new_x] != r:
        return new_x, new_y
    elif maze[new_y][x] != r:
        return x, new_y
    elif maze[y][new_x] != r:
        return new_x, y
    return x,y

def check_win(x,y):
    global game_over
    if maze[y][x] == c:
        game_over = True
        sense.show_message('Tu as gagne!')
        return True


    
def labyrinthe():
    global maze
    chiffre1=random.randint(1,2)
    if chiffre1==1:
        maze = maze1
    elif chiffre1==2:
        maze = maze2
         
    chiffre=random.randint(1,4)
    if chiffre==1:
        maze[6][4]=c
    elif chiffre==2:
        maze[2][6]=c
    elif chiffre==3:
        maze[3][1]=c
    elif chiffre==4:
        maze[6][2]=c
    game_over = False
    x = 1
    y = 1
    while not game_over:
        pitch = sense.get_orientation()['pitch']
        roll = sense.get_orientation()['roll']
        x,y = move_marble(pitch,roll,x,y)
        game_over=check_win(x,y)
        maze[y][x] = w
        sense.set_pixels(sum(maze,[]))
        sleep(0.05)
        maze[y][x] = b
