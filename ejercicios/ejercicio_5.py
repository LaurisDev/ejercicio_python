def conversion(grados):
    celsius = (grados - 32)*5/9
    return celsius


grados_fahrenheit = int(input("Ingrese sus grados en Fahrenheit que quiere convertir: "))
celsius = conversion(grados_fahrenheit)
print("Sus grados convertidos a celsius es de: ",celsius)