def encontrar_numero_mas_grande(lista):
    mas_grande = lista[0]
    for elemento in lista:
        if elemento > mas_grande:
            mas_grande = elemento
    return mas_grande


def encontrar_numero_mas_pequeño(lista):
    mas_pequeño = lista[0]
    for elemento in lista:
        if elemento < mas_pequeño:
            mas_pequeño = elemento
    return mas_pequeño


lista_numeros = [12, 55, 20, 15, 27, 3, 30]
numero_mas_grande = encontrar_numero_mas_grande(lista_numeros)
numero_mas_pequeño = encontrar_numero_mas_pequeño(lista_numeros)

print("El número más grande en la lista es:", numero_mas_grande)
print("El número más pequeño en la lista es:", numero_mas_pequeño)