import pygame
import math

ANCHO = 1080
ALTO = 720
TAM = (ANCHO, ALTO)
CENTRO = (ANCHO/2, ALTO/2)
NOMBRE = "Sistema Solar"

VENTANA = pygame.display.set_mode(TAM)
pygame.display.set_caption(NOMBRE)

def movimiento(radio, centro_x, centro_y, angulo):
    x = centro_x + int(math.cos(angulo)*radio)
    y = centro_y + int(math.sin(angulo)*radio)
    return x, y

x_mercurio = CENTRO[0]+120
y_mercurio = CENTRO[1]
radio_mercurio = 120
angulo_mercurio = 0
velocidad_angular_mercurio = 0.02

x_venus = CENTRO[0]+160
y_venus = CENTRO[1]
radio_venus = 160
angulo_venus = 0
velocidad_angular_venus = 0.016

x_tierra = CENTRO[0]+220
y_tierra = CENTRO[1]
radio_tierra = 220
angulo_tierra = 0
velocidad_angular_tierra = 0.01

x_luna = x_tierra+30
y_luna = y_tierra
radio_luna = 50
angulo_luna = 0
velocidad_angular_luna = 0.015

tiempo = 0
ejecuta = True
pygame.draw.circle(VENTANA, (0,173,182), (x_tierra, y_tierra), 30)
while ejecuta == True:
    # pygame.draw.circle(ventana, color, donde, radio del circulo)
    VENTANA.fill((0,0,0))
    pygame.draw.circle(VENTANA, (255,251,2), CENTRO, 100)

    x_mercurio , y_mercurio  = movimiento(radio_mercurio , CENTRO[0], CENTRO[1], angulo_mercurio )
    pygame.draw.circle(VENTANA, (152,104,8), (x_mercurio , y_mercurio ), 10)

    x_venus, y_venus = movimiento(radio_venus, CENTRO[0], CENTRO[1], angulo_venus)
    pygame.draw.circle(VENTANA, (255, 172, 36), (x_venus, y_venus), 20)

    x_tierra, y_tierra = movimiento(radio_tierra, CENTRO[0], CENTRO[1], angulo_tierra)
    pygame.draw.circle(VENTANA, (0,173,182), (x_tierra, y_tierra), 30)

    x_luna , y_luna  = movimiento(radio_luna , x_tierra, y_tierra, angulo_luna)
    pygame.draw.circle(VENTANA, (180,180,177), (x_luna , y_luna), 10)

    pygame.display.update()

    angulo_tierra = velocidad_angular_tierra * tiempo
    angulo_venus = velocidad_angular_venus * tiempo
    angulo_mercurio  = velocidad_angular_mercurio  * tiempo
    angulo_luna  = velocidad_angular_luna  * tiempo

    tiempo += 1 # tiempo = tiempo + 1

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecuta = False
    pygame.display.update()

pygame.quit()

