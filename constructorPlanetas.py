import random
def constructorPlanetas(nombre, tam, radio, color, v_angular = None, x = 0, y = 0, angulo = 0):

    v_angular = setVelocidad(nombre = nombre)

    objeto = {"nombre": nombre,
            "tam": tam,
            "radio": radio,
            "color": color,
            "v_angular": v_angular,
            "x": x,
            "y": y,
            "angulo": angulo,
            "tipo": "planeta"}
    return objeto

def setVelocidad(objeto=None, nueva_velocidad=None, nombre=None):
    velocidad = None
    astros = {"Sol": 0,
            "Mercurio": 0.02,
            "Venus": 0.016,
            "Tierra": 0.01,
            "Luna": 0.02,
            "Marte": 0.0052,
            "Jupiter": 0.0008,
            "Saturno": 0.0003,
            "Urano": 0.0001,
            "Neptuno": 0.00006}

    if nombre != None and nombre in astros and objeto == None:
        velocidad = astros[nombre]
        return velocidad
    elif nombre not in astros and objeto == None:
        velocidad = 0.3/random.randint(1,100)
        return velocidad

    elif "tipo" in objeto and "nombre" in objeto and objeto["tipo"] == "planeta":
        objeto["v_angular"] = nueva_velocidad
    else:
        print("Objeto invalido para esta función")
    return objeto

def getVelocidad(objeto):
    if "v_angular" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        return objeto["v_angular"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen velocidad angular.")
    else:
        print("El objeto pasado no tiene velocidad angular.")
    return None

def setNombre(objeto, nuevo_nombre):
    if type(nuevo_nombre) != str:
        print("Valor invalido: El nombre tiene que ser de tipo string")
    elif "nombre" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["nombre"] = nuevo_nombre
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene nombre.")
    else:
        print("El objeto pasado no tiene nombre.")
    return objeto


mercurio = constructorPlanetas(nombre = "Mercurio", tam = 5, radio = 60, color = (243, 199, 80))
venus = constructorPlanetas(nombre = "Venus", tam = 9, radio = 90, color = (0, 0, 0))
tierra = constructorPlanetas(nombre = "Tierra", tam = 12, radio = 145, color = (100, 149, 237))
marte = constructorPlanetas(nombre = "Marte", tam = 8, radio = 200, color = (188, 39, 50))
jupiter = constructorPlanetas(nombre = "Jupiter", tam = 30, radio = 400, color = (203, 123, 0))
saturno = constructorPlanetas(nombre = "Saturno", tam = 25, radio = 500, color = (255, 172, 36))
urano = constructorPlanetas(nombre = "Urano", tam = 23, radio = 600, color = (0, 204, 204))
neptuno = constructorPlanetas(nombre = "Neptuno", tam = 20, radio = 700, color = (0, 0, 153))

print(mercurio)
print("Velocidad de mercurio:", getVelocidad(mercurio))

