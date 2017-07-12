# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:45:17 2017

@author: Gaspar
"""
import pygame
from pygame.locals import *
from sys import exit
import random


# Variables Globales
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PLAYER_SIZE = 15
BANANA_SIZE = 10
PLAYER_SPEED = 1
BANANA_SPEED = 2
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480 
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


#Clase Player
class Player:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 1
        
    def dibuja(self):
        pygame.draw.circle(self.screen, RED, ( int(self.x), int(self.y) ), PLAYER_SIZE)
        
    def move_left(self):
        self.x += -self.speed
    
    def move_right(self):
         self.x = SCREEN_WIDTH - ( SCREEN_WIDTH - (self.x + self.speed) )

     
#Clase banana 
class Banana:
    def __init__(self, screen, x, y, size, color):
        self.screen = screen
        self.x = x;
        self.y = y
        self.size = size
        self.color = color
        self.speed = 0.5
        
    def dibuja(self):
        pygame.draw.circle(self.screen, BLUE, ( int(self.x), int(self.y) ), self.size)
    
    def move(self):
        self.y += self.speed
        
        
#Crea una lista de bananas        
def createBananas(screen, num_bananas):
    my_bananas = []

    for i in range(num_bananas):
        x = random.randint(BANANA_SIZE, SCREEN_WIDTH - BANANA_SIZE )
        y = BANANA_SIZE
    
        banana = Banana(screen, x, y, BANANA_SIZE, BLUE)
        my_bananas.append(banana)
        
    return my_bananas


#Verifica la collision
def collision(banana, player):
     if (banana.x + BANANA_SIZE > player.x - PLAYER_SIZE) and (banana.x - BANANA_SIZE < player.x + PLAYER_SIZE):
        if (banana.y + banana.size) > player.y - PLAYER_SIZE:
            return True
        else:
            return False

#Verifica si Player esta dentro de la pantalla
def checkLimitX(player, direccion):
    if direccion == 'LEFT' and (player.x - PLAYER_SIZE) >= 0:
        return True
    elif direccion == 'RIGHT' and (player.x + PLAYER_SIZE) <= SCREEN_WIDTH:
        return True
    else:
        return False

def checkLimitY(banana):
    if banana.y > 0:
        if (banana.y + BANANA_SIZE) > SCREEN_HEIGHT:
            banana.y = SCREEN_HEIGHT - BANANA_SIZE