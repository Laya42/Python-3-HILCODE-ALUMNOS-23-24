def generar_pos(ancho_bloque, ancho_pantalla, alto_bloque, num_filas):
    pos = list()
    x = 0
    y = 0
    for j in range(num_filas):
        fila = list()
        for i in range(ancho_pantalla//ancho_bloque):
            fila.append((x, y))
            x += ancho_bloque
        y+=alto_bloque
        x=0
        pos.append(fila)
    return pos

def generar_map(ancho_bloque, ancho_pantalla, alto_bloque, num_filas):
    mapa = list()
    for j in range(num_filas):
        fila = list()
        for i in range(ancho_pantalla//ancho_bloque):
            fila.append(True)
        mapa.append(fila)
    return mapa


