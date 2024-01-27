import planetas_utils
import pygame
import math
import random

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

mercurio = planetas_utils.constructorPlanetas(nombre = "Mercurio", tam = 5, radio = 60, color = (243, 199, 80))
venus = planetas_utils.constructorPlanetas(nombre = "Venus", tam = 8, radio = 90, color = (255, 255, 255))
tierra = planetas_utils.constructorPlanetas(nombre = "Tierra", tam = 12, radio = 145, color = (100, 149, 237))
marte = planetas_utils.constructorPlanetas(nombre = "Marte", tam = 8, radio = 220, color = (188, 39, 50))
jupiter = planetas_utils.constructorPlanetas(nombre = "Jupiter", tam = 28, radio = 400, color = (203, 123, 0))
saturno = planetas_utils.constructorPlanetas(nombre = "Saturno", tam = 24, radio = 500, color = (255, 172, 36))
urano = planetas_utils.constructorPlanetas(nombre = "Urano", tam = 23, radio = 600, color = (0, 204, 204))
neptuno = planetas_utils.constructorPlanetas(nombre = "Neptuno", tam = 20, radio = 700, color = (0, 0, 153))
sol = planetas_utils.constructorPlanetas(nombre="Sol", tam=50, x=CENTRO[0], y=CENTRO[1], radio=0, color=(255,251,2))

luna = planetas_utils.constructorPlanetas(nombre="Luna", tam=6, radio=25, color=(180,180,177))

planetas = [sol, mercurio, venus, tierra, marte, jupiter, saturno, urano, neptuno, luna]

for i in range(5000):
    planetas.append(planetas_utils.constructorPlanetas(nombre="Asteroide", tam=1, color=(255,255,255), radio = random.randint(235,365), angulo=random.randint(0,359)))

for i in range(400):
    planetas.append(planetas_utils.constructorPlanetas(nombre="Anillo", tam=1, color=(255,255,255), radio = random.randint(29,34), angulo=random.randint(0,359)))



tiempo = 0
ejecuta = True

for planeta in planetas:
    planeta = planetas_utils.setX(planeta, CENTRO[0] + planetas_utils.getRadio(planeta))
    planeta = planetas_utils.setY(planeta, CENTRO[1])

while ejecuta == True:
    VENTANA.fill((0,0,0))

    for planeta in planetas:
        pygame.draw.circle(VENTANA,
                            planetas_utils.getColor(planeta),
                            (planetas_utils.getX(planeta),
                            planetas_utils.getY(planeta)),
                            planetas_utils.getTam(planeta))

        if planetas_utils.getNombre(planeta) == "Luna":
            centro_x = planetas_utils.getX(tierra)
            centro_y = planetas_utils.getY(tierra)
        elif planetas_utils.getNombre(planeta)=="Anillo":
            centro_x = planetas_utils.getX(saturno)
            centro_y = planetas_utils.getY(saturno)
        else:
            centro_x = planetas_utils.getX(sol)
            centro_y = planetas_utils.getY(sol)

        '''
        centro_x = planetas_utils.getX(tierra) if planetas_utils.getNombre(planeta) == "Luna" else planetas_utils.getX(sol)
        centro_y = planetas_utils.getY(tierra) if planetas_utils.getNombre(planeta) == "Luna" else planetas_utils.getY(sol)
        '''

        x, y = movimiento(  radio = planetas_utils.getRadio(planeta),
                            centro_x = centro_x,
                            centro_y = centro_y,
                            angulo = planetas_utils.getAngulo(planeta))

        planeta = planetas_utils.setX(planeta, x)
        planeta = planetas_utils.setY(planeta, y)

        nuevo_angulo = planetas_utils.getVelocidad(planeta) + planetas_utils.getAngulo(planeta)
        planeta = planetas_utils.setAngulo(planeta, nuevo_angulo)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecuta = False

    pygame.display.update()
    tiempo += 1 # tiempo = tiempo + 1
pygame.quit()



