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
screen = pygame.display.set_mode(GameTools.SCREEN_SIZE)
pygame.display.set_caption("THE MONKEY GAME")

#Crea el monkey y las bananas
monkey = Player(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT - 20) #Creamos el Monkey al centro de la pantalla
#num_bananas = 20
#lista_bananas = [] 
#lista_bananas = createListaBananas(screen, num_bananas)   

lista_frutas = [] 

#Objeto para registro del tiempo
clock = pygame.time.Clock()

#Ciclo infinito para dibujar
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #necesario para cerrar la ventana al presionar X sino se usa se traba el juego
            running = False
            exit()
    
    #Revisa que tecla fue presionada
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        if checkLimitX(monkey, 'LEFT'):
            monkey.mover_left(PLAYER_SPEED)
    
    elif keys[K_RIGHT]:
        if checkLimitX(monkey, 'RIGHT'):
            monkey.mover_right(PLAYER_SPEED)
    
    screen.fill((0, 0, 0))  
    
    monkey.dibuja() #Dibuja el monkey
    
    un_coco = crearFruta(screen, WHITE) #Crea un coco
    una_banana = crearFruta(screen, BLUE) #Crea una banana
    lista_frutas.append(un_coco)
    lista_frutas.append(una_banana)
        
    for f in lista_frutas:     #Dibuja y mueve las bananas
        if checkLimitY(f):     #Revisa si la fruta ya alcanzo el piso de la pantalla       
            lista_frutas.remove(f)    
        else:
            #revisa si hubo colision, actualiza el contador y la bandera de paro
            (col, record) = colision(f, monkey) 
            if col:
                lista_frutas.remove(f)
                
        record += record   
        f.dibuja()
        f.mover()
            
    if monkey.isJump:
        monkey.Jump()
      
    #Refresca la pantalla
    pygame.display.update()
    


        
    
    
    
    
    