import numpy as np


def generar_matriz(filas, columnas):
    matriz = np.zeros((filas, columnas))
    for i in range(filas):
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor para la posición ({i}, {j}): "))
            matriz[i][j] = valor
    return matriz


filas = int(input("ingresa la cantidad de filas que deseas: "))
columnas = int(input("ingresa la cantidad de columnas que deseas: "))

matriz_generada = generar_matriz(filas, columnas)
print(matriz_generada)
