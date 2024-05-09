# CLASE BLOQUE

def constructor(color, ancho, alto, x, y, estado):
    bloque = {"tipo": "bloque"}
    setColor(bloque, color)
    setAlto(bloque, alto)
    setAncho(bloque, ancho)
    setX(bloque, x)
    setY(bloque, y)
    setEstado(bloque, estado)
    return bloque

def checkTipo(objeto):
    if "tipo" in objeto and objeto["tipo"] == "bloque":
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

def getAncho(objeto):
    if checkTipo(objeto):
        return objeto["ancho"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen ancho.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setAncho(objeto, nuevoAncho):
    if checkTipo(objeto) and type(nuevoAncho) == int and nuevoAncho >= 0:
        objeto["ancho"] = nuevoAncho
    elif not(type(nuevoAncho) == int and nuevoAncho >= 0):
        print("El ancho debe ser un valor entero positivo")
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen ancho.")
    else:
        print("El objeto pasado no tiene tipo.")

def getAlto(objeto):
    if checkTipo(objeto):
        return objeto["alto"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen alto.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setAlto(objeto, nuevoAlto):
    if checkTipo(objeto) and type(nuevoAlto) == int and nuevoAlto >= 0:
        objeto["alto"] = nuevoAlto
    elif not(type(nuevoAlto) == int and nuevoAlto >= 0):
        print("El alto debe ser un valor entero positivo")
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen alto.")
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
    if checkTipo(objeto) and type(nuevoX) == int and nuevoX >= 0:
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
    if checkTipo(objeto) and type(nuevoY) == int and nuevoY >= 0:
        objeto["y"] = nuevoY
    elif not(type(nuevoY) == int and nuevoY >= 0):
        print("El valor de Y debe ser un entero positivo.")
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen Y.")
    else:
        print("El objeto pasado no tiene tipo.")

def getEstado(objeto):
    if checkTipo(objeto):
        return objeto["estado"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen estado.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setEstado(objeto, nuevoEstado):
    if checkTipo(objeto):
        objeto["estado"] = nuevoEstado
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen estado.")
    else:
        print("El objeto pasado no tiene tipo.")
