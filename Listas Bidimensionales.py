# Escribe tu código aquí :-)
lista = [1,2,3,4,5]

for elem in lista:
    print(elem)

print("\nLISTA BIDIMENSIONAL") # Conocido también como Matriz o Tabla
lista_bidim = [ [1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13],
                [14,15]]

for lista in lista_bidim:
    print("\nElementos de",lista)
    for elem in lista:
        print(elem)

print("ELEMENTO:", lista_bidim[2][2])

print("\nLISTA TRIDIMENSIONAL") # Cubo

lista_tridim = [   [[1,2,3],
                    [4,5,6],
                    [7,8,9]],

                [   [10,11,12],
                    [13,14,15],
                    [16,17,18]],

                [   [19,20,21],
                    [22,23,24],
                    [25,26,27]]     ]

print(lista_tridim[0][0][2])
print(lista_tridim[1][1][0])
