import pygame
import sys
import random
import Bloque
import Plataforma
import Pelota
import colores
import mapas_utils
import math


pygame.init()
ANCHO, ALTO = 100, 100

TAM = (ANCHO, ALTO)
NOMBRE = "Block Breaker"
VENTANA = pygame.display.set_mode(TAM)
pygame.display.set_caption(NOMBRE)

VENTANA.fill((colores.getColor("NEGRO")))


pygame.draw.rect(VENTANA,(255,255,255),(50,50,20,20))

pygame.display.update()
