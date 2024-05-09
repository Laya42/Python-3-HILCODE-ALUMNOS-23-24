# Escribe tu código aquí :-)
import random
def getColor(color):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colores = {"BLANCO": (255, 255, 255),
                "BEIGE": (243, 199, 80),
                "AMARILLO": (255, 255, 0),
                "AZUL": (100, 149, 237),
                "ROJO": (188, 39, 50),
                "GRIS_OSCURO": (80, 71, 78),
                "NARANJA": (203, 123, 0),
                "NARANJA_CLARO":  (255, 172, 36),
                "MARRON": (126, 55, 5),
                "SALMON":  (215, 97, 49),
                "AZUL_OSCURO": (0, 0, 153),
                "CIAN": (0, 204, 204),
                "GRIS_CLARO": (224, 224, 224),
                "NEGRO": (0,0,0),
                "GRIS": (183,183,183),
                "CREMA": (255,225,179),
                "RANDOM": (r,g,b)
                }

    if color not in colores:
        print("Color no encontrado.")
        return None

    return colores[color]
