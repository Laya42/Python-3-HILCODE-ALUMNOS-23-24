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
ANCHO, ALTO = 800, 600

TAM = (ANCHO, ALTO)
NOMBRE = "Block Breaker"
VENTANA = pygame.display.set_mode(TAM)
pygame.display.set_caption(NOMBRE)

VENTANA.fill((colores.getColor("NEGRO")))

plataforma = Plataforma.constructor(color = colores.getColor("BEIGE"),
                                    ancho = 100,
                                    alto = 20,
                                    x = 350,
                                    y = 550,
                                    velocidad = 1)

pelota = Pelota.constructor(color = colores.getColor("CIAN"),
                            radio = 15,
                            x = 400,
                            y = 300,
                            velocidad = 0.025)

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

ancho_bloque = 50
alto_bloque = 25
num_filas = 10

pos = mapas_utils.generar_pos(ancho_bloque = ancho_bloque,
                  ancho_pantalla = ANCHO,
                  alto_bloque = alto_bloque,
                  num_filas = num_filas)

mapa1 = mapas_utils.generar_map(ancho_bloque = ancho_bloque,
                  ancho_pantalla = ANCHO,
                  alto_bloque = alto_bloque,
                  num_filas = num_filas)


bloques = list()
for i in range(len(mapa1)):
    for j in range(len(mapa1[i])):
        if mapa1[i][j]:
            bloque = Bloque.constructor(color = colores.getColor("ROJO"),
                                         ancho = ancho_bloque,
                                         alto = alto_bloque,
                                         x = pos[i][j][0],
                                         y = pos[i][j][1],
                                         estado = 3)
            bloques.append(bloque)

for bloque in bloques:
    pygame.draw.rect(surface = VENTANA,
                 color = Bloque.getColor(bloque),
                 rect = (Bloque.getX(bloque),
                 Bloque.getY(bloque),
                 Bloque.getAncho(bloque),
                 Bloque.getAlto(bloque)))

    pygame.draw.rect(surface = VENTANA,
                 color = colores.getColor("NEGRO"),
                 width = 1,
                 rect = (Bloque.getX(bloque),
                 Bloque.getY(bloque),
                 Bloque.getAncho(bloque),
                 Bloque.getAlto(bloque)))

print(pos)
pygame.display.update()

angulo = random.randint(0,360)
print(angulo)

def movimiento_plataforma(boton):
    if boton[pygame.K_LEFT]:
        nueva_x = Plataforma.getX(plataforma) - Plataforma.getVelocidad(plataforma)
        if nueva_x >= 0:  # Verificar límites
            Plataforma.setX(plataforma, nueva_x)
    if boton[pygame.K_RIGHT]:
        nueva_x = Plataforma.getX(plataforma) + Plataforma.getVelocidad(plataforma)
        if nueva_x + Plataforma.getAncho(plataforma) <= ANCHO:  # Verificar límites
            Plataforma.setX(plataforma, nueva_x)

ejecuta = True
while ejecuta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    VENTANA.fill(colores.getColor("NEGRO"))

    # dibuja la plataforma
    plataforma_objeto = pygame.draw.rect(VENTANA,
                        Plataforma.getColor(plataforma),
                        (Plataforma.getX(plataforma),
                        Plataforma.getY(plataforma),
                        Plataforma.getAncho(plataforma),
                        Plataforma.getAlto(plataforma)))


    # dibuja la pelota
    pelota_objeto = pygame.draw.circle(VENTANA,
                        Pelota.getColor(pelota),
                        (Pelota.getX(pelota),
                        Pelota.getY(pelota)),
                        Pelota.getRadio(pelota))

    if pelota_objeto.collidepoint(ANCHO//2, ALTO//2):
        VENTANA.fill(colores.getColor("RANDOM"))

    # dibuja cada bloque
    for bloque in bloques:
        # cuerpo del bloque
        pygame.draw.rect(VENTANA, Bloque.getColor(bloque),
                         (Bloque.getX(bloque), Bloque.getY(bloque),
                          Bloque.getAncho(bloque), Bloque.getAlto(bloque)))

        # borde del bloque
        pygame.draw.rect(VENTANA, colores.getColor("NEGRO"), width=1,
                         rect=(Bloque.getX(bloque), Bloque.getY(bloque),
                               Bloque.getAncho(bloque), Bloque.getAlto(bloque)))


    # mover la plataforma
    boton = pygame.key.get_pressed()
    movimiento_plataforma(boton)

    # mueve la pelota
    Pelota.setX(pelota, Pelota.getX(pelota) + math.cos(angulo*math.pi/180)*Pelota.getVelocidad(pelota))
    Pelota.setY(pelota, Pelota.getY(pelota) + math.sin((angulo)*math.pi/180)*Pelota.getVelocidad(pelota))

    pygame.display.update()


