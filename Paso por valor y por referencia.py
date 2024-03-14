# Escribe tu código aquí :-)
def f(lista):
    lista[0] = 9

def g(lista):
    lista2 = list()
    for i in lista:
        lista2.append(i)

    lista2[0] = 9


l = [1,2,3,4]
print(l)
f(l)
print(l)

l = [1,2,3,4]
print(l)
f(l)
print(l)


lista = l

lista.append(90)
print(lista)
print(l)

