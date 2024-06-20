# CLASE PELOTA

def constructor(color, radio, x, y, velocidad):
    pelota = {"tipo": "pelota"}
    setColor(pelota, color)
    setRadio(pelota, radio)
    setX(pelota, x)
    setY(pelota, y)
    setVelocidad(pelota, velocidad)
    return pelota

def checkTipo(objeto):
    if "tipo" in objeto and objeto["tipo"] == "pelota":
        return True
    return False

def getColor(objeto):
    if checkTipo(objeto):
        return objeto["color"]
    elif "tipo" in objeto:
        print(f"Objetos de tipo {objeto['tipo']} no tienen color.")
    else:
        print("El objeto pasado como parámetro no posee tipo.")
    return None

def setColor(objeto, nuevo_color):
    if type(nuevo_color) != tuple or len(nuevo_color) != 3:
        print("Valor invalido: Los colores van en una tupla de longitud 3.")
        return

    for i in range(3):
        if type(nuevo_color[i]) != int or nuevo_color[i] < 0 or nuevo_color[i] > 255:
            print("Valor invalido: El código de color RGB son numeros enteros >= 0 y <= 255.")
            return

    if checkTipo(objeto):
        objeto["color"] = nuevo_color
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen color.")
    else:
        print("El objeto pasado no tiene tipo.")

def getRadio(objeto):
    if checkTipo(objeto):
        return objeto["radio"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen radio.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setRadio(objeto, nuevoRadio):
    if checkTipo(objeto) and type(nuevoRadio) == int and nuevoRadio >= 0:
        objeto["radio"] = nuevoRadio
    elif not(type(nuevoRadio) == int and nuevoRadio >= 0):
        print("El radio debe ser un valor entero positivo")
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen radio.")
    else:
        print("El objeto pasado no tiene tipo.")

def getX(objeto):
    if checkTipo(objeto):
        return objeto["x"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen X.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setX(objeto, nuevoX):
    if checkTipo(objeto) and type(nuevoX) in (float, int) and nuevoX >= 0:
        objeto["x"] = nuevoX
    elif not(type(nuevoX) == int and nuevoX >= 0):
        print("El valor de X debe ser un entero positivo.")
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen X.")
    else:
        print("El objeto pasado no tiene tipo.")

def getY(objeto):
    if checkTipo(objeto):
        return objeto["y"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen Y.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setY(objeto, nuevoY):
    if checkTipo(objeto) and type(nuevoY) in (float, int) and nuevoY >= 0:
        objeto["y"] = nuevoY
    elif not(type(nuevoY) == int and nuevoY >= 0):
        print("El valor de Y debe ser un entero positivo.")
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen Y.")
    else:
        print("El objeto pasado no tiene tipo.")

def getVelocidad(objeto):
    if checkTipo(objeto):
        return objeto["velocidad"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen velocidad.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setVelocidad(objeto, nuevaVelocidad):
    if checkTipo(objeto) and type(nuevaVelocidad) in (float, int):
        objeto["velocidad"] = nuevaVelocidad
    elif not(type(nuevaVelocidad) in (float, int)):
        print("La velocidad debe ser un valor numérico")
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen velocidad.")
    else:
        print("El objeto pasado no tiene tipo.")
