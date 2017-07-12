#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 13:52:25 2017

@author: Gaspar
"""
import pygame
from pygame.locals import *
from sys import exit
import GameTools
from GameTools import *
import random
import math
 

#Iniciamos Pygame
pygame.init()
screen = pygame.display.set_mode(playtools.SCREEN_SIZE)
pygame.display.set_caption("THE MONKEY GAME")

#Crea el monkey y las bananas
monkey = Player(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT - 20) #Creamos el Monkey al centro de la pantalla
num_bananas = 20
lista_bananas = [] 
lista_bananas = createBananas(screen, num_bananas)   

#Ciclo infinito para dibujar
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #necesario para cerrar la ventana al presionar X sino se usa se traba 
            running = False
            exit()
    
    #Revisa que tecla due presionada
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        if checkLimitX(monkey, 'LEFT'):
            monkey.move_left()
    
    elif keys[K_RIGHT]:
        if checkLimitX(monkey, 'RIGHT'):
            monkey.move_right()
    
    screen.fill((0, 0, 0))  
    
    monkey.dibuja() #Dibuja el monkey
    for b in lista_bananas: #Dibuja y mueve las bananas
        b.dibuja()
        b.move()
        checkLimitY(b)            
        if collision(b, monkey):
            lista_bananas.remove(b)
      
    #Refresca la pantalla
    pygame.display.update()
    


        
    
    
    
    
    