from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
def Slug():
    global slug, slugtrail, white,blank,red,direction,vegetables,score,pause,dead
    slug = [[2,4],[3,4],[4,4]]
    slugtrail = []
    white = (255, 255, 255)
    blank = (0,0,0)
    red = (255, 0, 0)
    direction = "right"
    vegetables = []
    score = 0
    pause = 0.5
    dead = False
    Slug_game()
# Functions ---------------------------
def draw_slug (slug):
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], white)

def move():
    global score,pause,dead
    remove = True
    last = slug[-1]
    first = slug[0]
    next = list(last)

    if direction == "right":
        next[0] = last[0] + 1
    elif direction == "left":
        next[0] = last[0] - 1
    elif direction == "up":
        next[1] = last[1] - 1
    elif direction == "down":
        next[1] = last[1] + 1
        
    next = wrap(next)

    if next in slug:
        dead = True
        
    slug.append(next)
    sense.set_pixel(next[0], next[1], white)

    if next in vegetables:
        vegetables.remove(next)
        score += 1
        if score % 5 == 0:
            remove = False
            pause = pause * 0.8
    
    if remove == True:
        sense.set_pixel(first[0], first[1], (0,randint(20,255),randint(20,255)))
        slug.remove(first)
        if not first in slugtrail:
            slugtrail.append(first)

def wrap(pix):
    if pix[0] > 7:
        pix[0] = 0
    if pix[0] < 0:
        pix[0] = 7
        
    if pix[1] < 0:
        pix[1] = 7
    if pix[1] > 7:
        pix[1] = 0

    return pix

def joystick_moved(event):
    global direction
    direction = event.direction

def make_veg():
    veg_x = randint(0,7)
    veg_y = randint(0,7)
    while [veg_x,veg_y] in slug or [veg_x, veg_y] in slugtrail:
        veg_x = randint(0,7)
        veg_y = randint(0,7)
    sense.set_pixel(veg_x, veg_y, red)
    vegetables.append([veg_x,veg_y])
    
# Main program ------------------------
def Slug_game():
    global vegetables, slugtrail, slug, pause, score, dead, direction
    sense.clear()
    draw_slug(slug)
    while dead == False:
        sense.stick.direction_any = joystick_moved
        move()
        if len(vegetables) < 3 and randint(0,4) == 1:
            make_veg()
        if len(slugtrail) > len(slug)*3 and not slugtrail[0] in slug and not slugtrail[0] in slugtrail[1:]:
            sense.set_pixel(slugtrail[0][0],slugtrail[0][1],blank)
            slugtrail.remove(slugtrail[0])
        sleep(pause)

    sense.show_message(str(score) + " points")
