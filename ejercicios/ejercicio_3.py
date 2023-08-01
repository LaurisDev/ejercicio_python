import random

def lista_aleatorios(cantidad):
      lista = [0] * cantidad
      for i in range(cantidad):
          lista[i] = random.randint(0, 1000)
      return lista

print("Ingrese cuantos numeros aleatorios desea obtener: ")
cantidad_num=int(input())

aleatorios=lista_aleatorios(cantidad_num)
print(aleatorios)