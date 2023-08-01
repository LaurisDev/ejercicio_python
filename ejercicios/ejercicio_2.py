import math

def calcular_area(radio):
   area = math.pi * (radio ** 2)
   return area


radio_circulo = float(input("Ingrese el radio de su circulo: "))
area_del_circulo = calcular_area(radio_circulo)
print("El área del círculo es: ", area_del_circulo)