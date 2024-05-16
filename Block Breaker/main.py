import pygame
import sys
import random
import Bloque
import Plataforma
import Pelota
import colores

pygame.init()

ANCHO, ALTO = 800, 600
TAM = (ANCHO, ALTO)
NOMBRE = "Block Breaker"
VENTANA = pygame.display.set_mode(TAM)
pygame.display.set_caption(NOMBRE)

VENTANA.fill((colores.getColor("NEGRO")))

plataforma = Plataforma.constructor(color = colores.getColor("AZUL"),
                                    ancho = 100,
                                    alto = 20,
                                    x = 350,
                                    y = 550,
                                    velocidad = 7)

pelota = Pelota.constructor(color = colores.getColor("RANDOM"),
                            radio = 20,
                            x = 400,
                            y = 300,
                            velocidad = 15)

pygame.draw.rect(VENTANA,
                 Plataforma.getColor(plataforma),
                 (Plataforma.getX(plataforma),
                 Plataforma.getY(plataforma),
                 Plataforma.getAncho(plataforma),
                 Plataforma.getAlto(plataforma)))

pygame.draw.circle(VENTANA,
                   Pelota.getColor(pelota),
                   (Pelota.getX(pelota),
                   Pelota.getY(pelota)),
                   Pelota.getRadio(pelota))

pygame.display.update()






