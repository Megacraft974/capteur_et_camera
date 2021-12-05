# -*- coding: utf-8 -*-
from sense_hat import SenseHat
#import os
from code_secret import*
from slug import*
from labyrinthe import*
from space_pet import*
from sparkles import*
from RPG import*
from ping import*
from signature import*

sense=SenseHat()

def a1():
    sense.show_message("Code secret.")
    code_secret()

def b2():
    sense.show_message("Slug.")
    Slug()

def c3():
    sense.show_message("Labyrinthe.")
    labyrinthe()

def d4():
    sense.show_message("Animal de compagnie.")
    space_pet()

def e5():
    sense.show_message("Economiseur d'ecran.")
    effet()

def f6():
    sense.show_message("RPG.")
    RPG()

def g7():
    sense.show_message("Ping-pong.")
    ping()
    
def h8():
    sense.show_message("Signature.")
    signature()
