import pygame
import sys
import random
import Bloque
import Plataforma
import Pelota
import colores
import mapas_utils
import math


def movimiento_plataforma(boton):
    if boton[pygame.K_LEFT]:
        nueva_x = Plataforma.getX(plataforma) - Plataforma.getVelocidad(plataforma)
        if nueva_x >= 0:  # Verificar límites
            Plataforma.setX(plataforma, nueva_x)
    if boton[pygame.K_RIGHT]:
        nueva_x = Plataforma.getX(plataforma) + Plataforma.getVelocidad(plataforma)
        if nueva_x + Plataforma.getAncho(plataforma) <= ANCHO:  # Verificar límites
            Plataforma.setX(plataforma, nueva_x)

def movimiento_pelota(pelota):
    x = Pelota.getX(pelota) + math.cos(angulo*math.pi/180)*Pelota.getVelocidad(pelota)
    y = Pelota.getY(pelota) + math.sin((angulo)*math.pi/180)*Pelota.getVelocidad(pelota)
    return x, y

def colisiones(pelota_objeto, pelota, bloques_objetos, pos, ancho_bloque, alto_bloque):
    for i in range(len(pos)):
        for  j in range(len(pos[i])):
            horizontal = [pos[i][j][0], pos[i][j][0]+ancho_bloque] # [x inicio, x fin]
            vertical = [pos[i][j][1], pos[i][j][1]+alto_bloque] # [y inicio, y fin]

            for x in range(horizontal[0], horizontal[1]):
                for y in range(vertical[0], vertical[1]):
                    if pelota_objeto.collidepoint(x,y):
                        Pelota.setVelocidad(pelota, -1)

pygame.init()
ANCHO, ALTO = 800, 600

TAM = (ANCHO, ALTO)
NOMBRE = "Block Breaker"
VENTANA = pygame.display.set_mode(TAM)
pygame.display.set_caption(NOMBRE)

# creación de plataforma
plataforma = Plataforma.constructor(color = colores.getColor("BEIGE"),
                                    ancho = 100,
                                    alto = 20,
                                    x = 350,
                                    y = 550,
                                    velocidad = 1)

# creación de pelota
pelota = Pelota.constructor(color = colores.getColor("CIAN"),
                            radio = 10,
                            x = 400,
                            y = 300,
                            velocidad = 3)


# creando los bloques
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

angulo = random.randint(0,360)
print(angulo)

ejecuta = True
while ejecuta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False


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


    # dibuja cada bloque
    bloques_objetos = list()
    bordes_objetos = list()
    for bloque in bloques:
        bloque_objeto = pygame.draw.rect(surface = VENTANA,
                        color = Bloque.getColor(bloque),
                        rect = (Bloque.getX(bloque),
                        Bloque.getY(bloque),
                        Bloque.getAncho(bloque),
                        Bloque.getAlto(bloque)))

        bloques_objetos.append(bloque_objeto)

        borde_objeto = pygame.draw.rect(surface = VENTANA,
                     color = colores.getColor("NEGRO"),
                     width = 1,
                     rect = (Bloque.getX(bloque),
                     Bloque.getY(bloque),
                     Bloque.getAncho(bloque),
                     Bloque.getAlto(bloque)))

        bordes_objetos.append(borde_objeto)

    # mover la plataforma
    boton = pygame.key.get_pressed()
    movimiento_plataforma(boton)

    # mueve la pelota
    x, y = movimiento_pelota(pelota)
    Pelota.setX(pelota, x)
    Pelota.setY(pelota, y)

    # colisiones con bloques
    colisiones(pelota_objeto, pelota, bloques_objetos, pos, ancho_bloque, alto_bloque)

    # colisiones con paredes
    # abajo
    for x in range(0,ANCHO):
        if pelota_objeto.collidepoint(x, ALTO-1):
            Pelota.setVelocidad(pelota, 0)

    # izquierda
    for y in range(0,ALTO):
        if pelota_objeto.collidepoint(1, y):
            Pelota.setVelocidad(pelota, 0)

    # derecha
    for y in range(0,ALTO):
        if pelota_objeto.collidepoint(ANCHO-1, y):
            Pelota.setVelocidad(pelota, 0)

    # arriba
    for x in range(0,ANCHO):
        if pelota_objeto.collidepoint(x, 1):
            Pelota.setVelocidad(pelota, 0)

    pygame.display.update()

pygame.quit()
