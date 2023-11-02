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

x_tierra = CENTRO[0]+220
y_tierra = CENTRO[1]
angulo_tierra = 0
velocidad_angular_tierra = 0.01

ejecuta = True
while ejecuta == True:
    # pygame.draw.circle(ventana, color, donde, radio del circulo)
    pygame.draw.circle(VENTANA, (255,251,2), CENTRO, 100)
    pygame.draw.circle(VENTANA, (152,104,8), (CENTRO[0]+120,CENTRO[1]), 10)
    pygame.draw.circle(VENTANA, (255,236,131), (CENTRO[0]+160,CENTRO[1]), 20)
    pygame.draw.circle(VENTANA, (0,173,182), (CENTRO[0]+220,CENTRO[1]-150), 30)






    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecuta = False
    pygame.display.update()

pygame.quit()

