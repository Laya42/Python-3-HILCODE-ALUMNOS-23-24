# Escribe tu código aquí :-)
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from colores import *

pygame.init()
ANCHO = 300
ALTO = 400
ANCHO_RAYA = 100
TAM = (ANCHO, ALTO)
NOMBRE = "Tic Tac Toe"

VENTANA = pygame.display.set_mode(TAM)
pygame.display.set_caption(NOMBRE)

VENTANA.fill((getColor("BLANCO")))

def dibujar_tabla():
    for i in range(1,4):
        # LINEAS HORIZONTALES
        pygame.draw.line(surface = VENTANA,
                        color = getColor("ROJO"),
                        width = 3,
                        start_pos = (0,i*ANCHO_RAYA),
                        end_pos = (ANCHO,i*ANCHO_RAYA))

        # LINEAS VERTICALES
        pygame.draw.line(surface = VENTANA,
                        color = getColor("ROJO"),
                        width = 3,
                        start_pos = (i*ANCHO_RAYA,0),
                        end_pos = (i*ANCHO_RAYA,ANCHO))

def dibujar_x(r1, r2):
    pygame.draw.line(surface = VENTANA,
                    color = getColor("ROJO"),
                    width = 3,
                    start_pos = r1[0],
                    end_pos = r1[1])

    pygame.draw.line(surface = VENTANA,
                    color = getColor("ROJO"),
                    width = 3,
                    start_pos = r2[0],
                    end_pos = r2[1])

def dibujar_o(centro):
    pygame.draw.circle(surface = VENTANA,
                    color = getColor("ROJO"),
                    width = 3,
                    radius = 50,
                    center = centro)

def posiciones_o(posicion):
    posiciones = [ [    [1,2,3],
                        [4,5,6],
                        [7,8,9]],

                    [   [50,150,250],
                        [50,150,250],
                        [50,150,250]],

                    [   [50,50,50],
                        [150,150,150],
                        [250,250,250]]         ]

    for i in range(len(posiciones[0])):
        for j in range(len(posiciones[0][i])):
            if posiciones[0][i][j] == posicion:
                I = i
                J = j
                break

    x = posiciones[1][I][J]
    y = posiciones[2][I][J]


    return (x, y)

def posiciones_x(posicion):
    posiciones = {  1: ([(0,0),(100,100)],[(0,100),(100,0)]),
                    2: ([(100,0),(200,100)], [(100,100),(200,0)]),
                    3: ([(200,0),(300,100)], [(200,100),(300,0)]),
                    4: ([(0,100),(100,200)], [(0,200),(100,100)]),
                    5: ([(100,100),(200,200)], [(100,200),(200,100)]),
                    6: ([(200,100),(300,200)], [(200,200),(300,100)]),
                    7: ([(0,200),(100,300)], [(0,300),(100,200)]),
                    8: ([(100,200),(200,300)],[(100,300),(200,200)]),
                    9: ([(200,200),(300,300)],[(200,300),(300,200)])    }

    r1 = posiciones[posicion][0]
    r2 = posiciones[posicion][1]
    return r1, r2

def click(punto):
        x = punto[0]
        y = punto[1]

        posicion = None
        if (x >= 0 and x < 100) and (y >= 0 and y < 100):
            posicion = 1
        elif (x >= 100 and x < 200) and (y >= 0 and y < 100):
            posicion = 2
        elif (x >= 200 and x < 300) and (y >= 0 and y < 100):
            posicion = 3

        elif (x >= 0 and x < 100) and (y >= 100 and y < 200):
            posicion = 4
        elif (x >= 100 and x < 200) and (y >= 100 and y < 200):
            posicion = 5
        elif (x >= 200 and x < 300) and (y >= 100 and y < 200):
            posicion = 6

        elif (x >= 0 and x < 100) and (y >= 200 and y < 300):
            posicion = 7
        elif (x >= 100 and x < 200) and (y >= 200 and y < 300):
            posicion = 8
        elif (x >= 200 and x < 300) and (y >= 200 and y < 300):
            posicion = 9

        return posicion

def victoria(posicion):
    ganador = " "
    if tabla[0][0] == tabla[0][1] and tabla[0][1] == tabla[0][2]:
        ganador = tabla[0][0]
    elif tabla[1][0] == tabla[1][1] and tabla[1][1] == tabla[1][2]:
        ganador = tabla[1][0]
    elif tabla[2][0] == tabla[2][1] and tabla[2][1] == tabla[2][2]:
        ganador = tabla[2][0]
    elif tabla[0][0] == tabla[1][0] and tabla[1][0] == tabla[2][0]:
        ganador = tabla[0][0]
    elif tabla[0][1] == tabla[1][1] and tabla[1][1] == tabla[2][1]:
        ganador = tabla[0][1]
    elif tabla[0][2] == tabla[1][2] and tabla[1][2] == tabla[2][2]:
        ganador = tabla[0][2]
    elif tabla[0][0] == tabla[1][1] and tabla[1][1] == tabla[2][2]:
        ganador = tabla[0][0]
    elif tabla[0][2] == tabla[1][1] and tabla[1][1] == tabla[2][0]:
        ganador = tabla[0][2]
    else:
        i = 0
        j = 0
        interrumpir = False
        while i < len(tabla) and not interrumpir:
            j = 0
            while j < len(tabla[i]) and not interrumpir:
                if type(tabla[i][j]) == int:
                    interrumpir = True
                elif i == 2 and j == 2:
                    interrumpir = True
                    ganador = "Empate"
                j+=1
            i+=1

    return ganador

def crear_tabla():
    tabla = list()
    num = 1

    for i in range(3):
        fila = list()

        for i in range(3):
            fila.append(num)
            num+=1
        tabla.append(fila)
    return tabla

def cambiar_posiciones(tabla, posicion):
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if tabla[i][j] == posicion:
                tabla[i][j] = jugada[0]
                dibujos(posicion)
                break

    # Optimizado
    """
    i = 0
    encontrado = False
    while i < len(tabla) and not encontrado:
        j = 0
        while j < len(tabla[i]):
            if tabla[i][j] == posicion:
                tabla[i][j] = jugada[0]
                dibujos(posicion)
                encontrado = True
            elif type(tabla[i][j]) == int and tabla[i][j] > posicion:
                encontrado = True
            j+=1
        i+=1
    """

def dibujos(posicion):
    if jugada[0] == "X":
        r1, r2 = posiciones_x(posicion)
        dibujar_x(r1, r2)
        jugada[0] = "O"
    else:
        centro = posiciones_o(posicion)
        dibujar_o(centro)
        jugada[0] = "X"

def victoria(posicion):
    ganador = " "
    if tabla[0][0] == tabla[0][1] and tabla[0][1] == tabla[0][2]:
        ganador = tabla[0][0]
    elif tabla[1][0] == tabla[1][1] and tabla[1][1] == tabla[1][2]:
        ganador = tabla[1][0]
    elif tabla[2][0] == tabla[2][1] and tabla[2][1] == tabla[2][2]:
        ganador = tabla[2][0]
    elif tabla[0][0] == tabla[1][0] and tabla[1][0] == tabla[2][0]:
        ganador = tabla[0][0]
    elif tabla[0][1] == tabla[1][1] and tabla[1][1] == tabla[2][1]:
        ganador = tabla[0][1]
    elif tabla[0][2] == tabla[1][2] and tabla[1][2] == tabla[2][2]:
        ganador = tabla[0][2]
    elif tabla[0][0] == tabla[1][1] and tabla[1][1] == tabla[2][2]:
        ganador = tabla[0][0]
    elif tabla[0][2] == tabla[1][1] and tabla[1][1] == tabla[2][0]:
        ganador = tabla[0][2]
    else:
        i = 0
        j = 0
        interrumpir = False
        while i < len(tabla) and not interrumpir:
            j = 0
            while j < len(tabla[i]) and not interrumpir:
                if type(tabla[i][j]) == int:
                    interrumpir = True
                elif i == 2 and j == 2:
                    interrumpir = True
                    ganador = "Empate"
                j+=1
            i+=1

    return ganador

# Función para mostrar el mensaje del ganador
def mostrar_mensaje_ganador(mensaje):
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(mensaje, True, getColor("ROJO"))
    rectangulo_texto = texto.get_rect(center=(ANCHO // 2, ALTO - 50))
    VENTANA.blit(texto, rectangulo_texto)

# Función para mostrar el botón "Jugar de Nuevo"
def mostrar_boton_jugar_nuevo():
    ancho_boton = 130
    alto_boton = 30
    x_centro = (ANCHO // 2) - ancho_boton//2
    y_centro = ALTO - 35

    pygame.draw.rect(VENTANA, getColor("SALMON"), (x_centro , y_centro, ancho_boton, alto_boton))
    fuente = pygame.font.Font(None, 24)
    texto = fuente.render('Jugar de Nuevo', True, getColor("BLANCO"))
    rectangulo_texto = texto.get_rect(center=(ANCHO // 2, ALTO - 20))
    VENTANA.blit(texto, rectangulo_texto)

    return ancho_boton, alto_boton, x_centro, y_centro

def area_boton(ancho_boton, alto_boton, x_centro, y_centro):
    min_x = x_centro - (ancho_boton//2)
    max_x = x_centro + (ancho_boton//2)
    min_y = y_centro - (alto_boton//2)
    max_y = y_centro + (alto_boton//2)

    return min_x, max_x, min_y, max_y

def reiniciar(min_x, max_x, min_y, max_y, punto, tabla):
    x = punto[0]
    y = punto[1]
    print(x, y)
    print(min_x, max_x, min_y, max_y)
    if (x >= min_x and x <= max_x) and (y >= min_y and y <= max_y):
        print("a")
        tabla = crear_tabla()
        VENTANA.fill((getColor("BLANCO")))
        dibujar_tabla()
    return tabla



jugada = ["X"]
ejecuta = True
tabla = crear_tabla()

ganador = victoria(tabla)
while ejecuta:
    dibujar_tabla()
    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecuta = False

    while not(ganador in ("X","O","Empate")) and ejecuta:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecuta = False
            elif evento.type == MOUSEBUTTONDOWN:
                posicion = click(evento.pos)
                cambiar_posiciones(tabla, posicion)
                ganador = victoria(tabla)
        pygame.display.update()

    ancho_boton, alto_boton, x_centro, y_centro = mostrar_boton_jugar_nuevo()
    mensaje = f"El ganador ha sido {ganador}" if ganador != "Empate" else "Empate"
    mostrar_mensaje_ganador(mensaje)

    for evento in pygame.event.get():
        if evento.type == MOUSEBUTTONDOWN:

            min_x, max_x, min_y, max_y = area_boton(ancho_boton, alto_boton, x_centro, y_centro)
            tabla = reiniciar(min_x, max_x, min_y, max_y, evento.pos, tabla)
            ganador = victoria(tabla)
    pygame.display.update()

pygame.quit()



