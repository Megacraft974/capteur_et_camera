from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

def baton(y,last_y):
    sense.set_pixel(0,last_y,(0,0,0))
    sense.set_pixel(7,last_y,(0,0,0))
    
    sense.set_pixel(0,y,(200,200,200))
    sense.set_pixel(0,y+1,(200,200,200))
    sense.set_pixel(0,y-1,(200,200,200))
    
    sense.set_pixel(7,y,(200,200,200))
    sense.set_pixel(7,y+1,(200,200,200))
    sense.set_pixel(7,y-1,(200,200,200))

def ping():
    score=0
    y = 4
    last_y = 0
    ball_position=[6,3]
    ball_speed=[-0.5,-0.5]
    jouer=True
    while jouer:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'down' and y < 6:
                    y += 1
                    last_y = y-2
                elif event.direction == 'up' and y > 1:
                    y -= 1
                    last_y = y+2

        sleep(0.25-(score/100))

        sense.set_pixel(ball_position[0],ball_position[1],0,0,0)
        baton(y,last_y)

        ball_position[0] += ball_speed[0]
        ball_position[1] += ball_speed[1]

        if ball_position[1] == 0 or ball_position[1] == 7:
            ball_speed[1] = -ball_speed[1]
        if ball_position[0] == 1 and y-1 <= ball_position[1] <= y+1:
            ball_speed[0] = -ball_speed[0]
            score += 1
        if ball_position[0] == 6 and y-1 <= ball_position[1] <= y+1:
            ball_speed[0] = -ball_speed[0]
            score += 1
        if ball_position[0] == 0:
            sense.show_message('Tu as perdu!')
            jouer=False
            break
        if ball_position[0] == 7:
            sense.show_message('Tu as perdu!')
            jouer=False
            break
        
        sense.set_pixel(ball_position[0],ball_position[1],0,0,255)
        
    sense.show_message(str(score) + " pts!")
