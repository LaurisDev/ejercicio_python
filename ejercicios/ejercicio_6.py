def lista_suma(lista_numero):
    suma = 0
    for numero in lista_numeros:
        suma = suma + numero
    return suma


lista_numeros = [1, 2, 3, 4]
suma_numeros = lista_suma(lista_numeros)
print("La suma de sus numeros son de:",suma_numeros)