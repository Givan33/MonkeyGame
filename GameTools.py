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
SPEED = 1
PLAYER_SIZE = 15
PLAYER_SPEED = 1
PLAYER_JUMP_SIZE = 50
BANANA_SIZE = 10
BANANA_SPEED = 2
COCO_SIZE = 10
COCO_SPEED = 4
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480 
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


#Clase Player
class Player:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.isJump = False
        
    def dibuja(self):
        pygame.draw.circle(self.screen, RED, ( int(self.x), int(self.y) ), PLAYER_SIZE)
        
    def mover_left(self, speed):
        self.x += -speed
    
    def mover_right(self, speed):
         self.x = SCREEN_WIDTH - ( SCREEN_WIDTH - (self.x + speed) )
    
    def Jump(self):
        if self.isJump:
            self.y -= self.speed * PLAYER_JUMP_SIZE
            
        self.speed = -self.speed
        self.y += self.speed             
        self.isJump = False

     
#Clase banana 
class Fruta:
    def __init__(self, screen, x, y, vel, size, color):
        self.screen = screen
        self.x = x;
        self.y = y
        self.vel = vel
        self.size = size
        self.color = color

#Clase para banana
class Banana(Fruta):        
    def dibuja(self):
        pygame.draw.circle(self.screen, self.color, ( int(self.x), int(self.y) ), self.size)
    
    def mover(self):
        self.y += self.vel
 
#Clase para cocos       
class Coco(Fruta):
    def dibuja(self):
        pygame.draw.circle(self.screen, self.color, ( int(self.x), int(self.y) ), self.size)
    
    def mover(self):
        self.y += self.vel
    
    
#Crea una fruta        
def crearFruta(screen, color):
    if color == BLUE:
        x = random.randint(BANANA_SIZE, SCREEN_WIDTH - BANANA_SIZE )
        y = BANANA_SIZE
        fruta = Banana(screen, x, y, BANANA_SPEED, BANANA_SIZE, BLUE)
    
    elif color == WHITE:
        x = random.randint(COCO_SIZE, SCREEN_WIDTH - COCO_SIZE )
        y = COCO_SIZE    
        fruta = Coco(screen, x, y, COCO_SPEED, COCO_SIZE, WHITE)
    
    return fruta
        
       
#Crea una lista de bananas        
def createListaBananas(screen, num_bananas):
    my_bananas = []

    for i in range(num_bananas):
        x = random.randint(BANANA_SIZE, SCREEN_WIDTH - BANANA_SIZE )
        y = BANANA_SIZE
    
#        banana = Banana(screen, x, y, BANANA_SIZE, BLUE, speed)
#        my_bananas.append(banana)
        
    return my_bananas


#Verifica la collision de una fruta con el monkey
def colision(fruta, player):
    colision = False
    record = 0
    
    if fruta.color == WHITE:
         if (fruta.x + COCO_SIZE > player.x - PLAYER_SIZE) and (fruta.x - COCO_SIZE < player.x + PLAYER_SIZE):
            if (fruta.y + fruta.size) > player.y - PLAYER_SIZE:
                colision = True
                record = -1
    
    elif fruta.color == BLUE:
        if (fruta.x + BANANA_SIZE > player.x - PLAYER_SIZE) and (fruta.x - BANANA_SIZE < player.x + PLAYER_SIZE):
            if (fruta.y + fruta.size) > player.y - PLAYER_SIZE:
                colision = True
                record = 1
              
    return (colision, record)


#Verifica si Player esta dentro de la pantalla
def checkLimitX(player, direccion):
    if (direccion == 'LEFT') and (player.x - PLAYER_SIZE) >= 0:
        return True
    elif (direccion == 'RIGHT') and (player.x + PLAYER_SIZE) <= SCREEN_WIDTH:
        return True
    else:
        return False
  
    
#Verifica si la banana toco el piso
def checkLimitY(banana):
    if banana.y > 0:
        if (banana.y + BANANA_SIZE) > SCREEN_HEIGHT:
            #banana.y = SCREEN_HEIGHT - BANANA_SIZE
            return True