# main.py
import Bloque
import Plataforma
import Pelota

def main():
    # Crear objetos de cada clase y probar todos los métodos

    # Bloque
    bloque = Bloque.constructor((255, 0, 0), 50, 50, 100, 100, "activo")
    print("Bloque:")
    print("Color del bloque:", Bloque.getColor(bloque))
    print("Ancho del bloque:", Bloque.getAncho(bloque))
    print("Alto del bloque:", Bloque.getAlto(bloque))
    print("Posición X del bloque:", Bloque.getX(bloque))
    print("Posición Y del bloque:", Bloque.getY(bloque))
    print("Estado del bloque:", Bloque.getEstado(bloque))
    print()

    # Plataforma
    plataforma = Plataforma.constructor((0, 255, 0), 100, 20, 200, 200, 5)
    print("Plataforma:")
    print("Color de la plataforma:", Plataforma.getColor(plataforma))
    print("Ancho de la plataforma:", Plataforma.getAncho(plataforma))
    print("Alto de la plataforma:", Plataforma.getAlto(plataforma))
    print("Posición X de la plataforma:", Plataforma.getX(plataforma))
    print("Posición Y de la plataforma:", Plataforma.getY(plataforma))
    print("Velocidad de la plataforma:", Plataforma.getVelocidad(plataforma))
    print()

    # Pelota
    pelota = Pelota.constructor((0, 0, 255), 10, 300, 300, 10)
    print("Pelota:")
    print("Color de la pelota:", Pelota.getColor(pelota))
    print("Radio de la pelota:", Pelota.getRadio(pelota))
    print("Posición X de la pelota:", Pelota.getX(pelota))
    print("Posición Y de la pelota:", Pelota.getY(pelota))
    print("Velocidad de la pelota:", Pelota.getVelocidad(pelota))

if __name__ == "__main__":
    main()
