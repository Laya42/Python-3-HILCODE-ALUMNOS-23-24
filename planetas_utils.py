import random

PROPORCION = 1

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
            "Neptuno": 0.00006,
            "Luna": 0.015}

    for clave in astros.keys():
        astros[clave]*=PROPORCION

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

def getNombre(objeto):
    if "nombre" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        return objeto["nombre"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen nombre.")
    else:
        print("El objeto pasado no tiene nombre.")
    return None

def setRadio(objeto, nuevo_radio):
    if type(nuevo_radio) != int or nuevo_radio <= 0:
        print("Valor invalido: El radio tiene que ser un valor entero positivo.")
    elif "nombre" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["radio"] = nuevo_radio
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene radio.")
    else:
        print("El objeto pasado no tiene radio.")
    return objeto

def getRadio(objeto):
    if "radio" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        return objeto["radio"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen radio.")
    else:
        print("El objeto pasado no tiene radio.")
    return None

def setTam(objeto, nuevo_tam):
    if type(nuevo_tam) != int or nuevo_tam <= 0:
        print("Valor invalido: El tamaño tiene que ser un valor entero positivo.")
    elif "tam" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["tam"] = nuevo_tam
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene tamaño.")
    else:
        print("El objeto pasado no tiene tamaño.")
    return objeto

def getTam(objeto):
    if "tam" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        return objeto["tam"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen tamaño.")
    else:
        print("El objeto pasado no tiene tamaño.")
    return None

def setAngulo(objeto, nuevo_angulo):
    if type(nuevo_angulo) != int and type(nuevo_angulo) != float:
        print("Valor invalido: El angulo tiene que ser un valor numérico.")
    elif "angulo" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["angulo"] = nuevo_angulo
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene angulo.")
    else:
        print("El objeto pasado no tiene angulo.")
    return objeto

def getAngulo(objeto):
    if "angulo" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        return objeto["angulo"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen angulo.")
    else:
        print("El objeto pasado no tiene angulo.")
    return None

def setX(objeto, nuevo_X):
    if type(nuevo_X) != int and type(nuevo_X) != float:
        print("Valor invalido: X tiene que ser un valor numérico.")
    elif "x" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["x"] = nuevo_X
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene x.")
    else:
        print("El objeto pasado no tiene x.")
    return objeto

def getX(objeto):
    if "x" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        return objeto["x"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen x.")
    else:
        print("El objeto pasado no tiene x.")
    return None

def setY(objeto, nuevo_Y):
    if type(nuevo_Y) != int and type(nuevo_Y) != float:
        print("Valor invalido: Y tiene que ser un valor numérico.")
    elif "y" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["y"] = nuevo_Y
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene y.")
    else:
        print("El objeto pasado no tiene y.")
    return objeto

def getY(objeto):
    if "y" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        return objeto["y"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen y.")
    else:
        print("El objeto pasado no tiene y.")
    return None

def setColor(objeto, nuevo_color):
    if type(nuevo_color) != tuple or len(nuevo_color) != 3:
        print("Valor invalido: Los colores van en una tupla de longitud 3.")
        return objeto

    for i in range(3):
        if type(nuevo_color[i]) != int or nuevo_color[i] < 0 or nuevo_color[i] > 255:
            print("Valor invalido: El código de color RGB son numeros enteros >= 0 y <= 255.")
            return objeto

    if "color" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["color"] = nuevo_color
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene color.")
    else:
        print("El objeto pasado no tiene color.")
    return objeto

def getColor(objeto):
    if "color" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        return objeto["color"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen color.")
    else:
        print("El objeto pasado no tiene color.")
    return None
'''
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
mercurio = setVelocidad(objeto=mercurio, nueva_velocidad=30)
print("Velocidad de mercurio:", getVelocidad(mercurio))
'''
