import pygame
from pygame.locals import *

arrow = ( "                        ",
          "XXXXXXXXXXXXXXXXXXXXXXXX",
          "X......................X",
          "X......................X",
          "X......................X",
          "X....XXX........XXX....X",
          "X....X.X........X.X....X",
          "X....XXX........XXX....X",
          "X......................X",
          "X......................X",
          "X......................X",
          "X..........XXX.........X",
          "X..........XXX.........X",
          "X..........XXX.........X",
          "X......................X",
          "X......................X",
          "X......................X",
          "X.....X..........X.....X",
          "X.....X..........X.....X",
          "X.....XXXXXXXXXXXX.....X",
          "X......................X",
          "X......................X",
          "XXXXXXXXXXXXXXXXXXXXXXXX",
          "                        ")

def Test(arrow):
    hotspot = None
    y = 1
    for y in range(len(arrow)):
        for x in range(len(arrow[y])):
            if arrow[y][x] in ['x', ',', '.']:
                hotspot = x,y
                break
        if hotspot != None:
            break
    if hotspot == None:
        raise Exception("No hotspot specified for cursor '%s'!" %
cursorname)
    s2 = []
    for ligne in arrow:
        s2.append(ligne.replace('x', 'X').replace(',', '.').replace('O',
'o'))
    curseur, masque = pygame.cursors.compile(s2, 'X', '.', 'o')
    taille = len(arrow[0]), len(arrow)
    pygame.mouse.set_cursor(taille, hotspot, curseur, masque)

def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    bg = pygame.display.set_mode((1775, 863), 0, 24)
    pygame.display.update()
    for curseur in [arrow]:
        Test(curseur)
        marche = True
        if marche:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == QUIT:
                    marche = False

main()
