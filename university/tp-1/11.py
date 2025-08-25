contador = 0
suma = 0
numero = 0

while numero >= 0:
    ingreso = input("Ingrese un numero entero positivo: ")
    numero = int(ingreso)
    suma = suma + numero
    contador = contador + 1

promedio = suma / contador
print(f"El promedio es de: {promedio}")