tope = int(input("Cuantos valores quiere ingresar: "))

contador = 0
suma = 0

while contador < tope:
    valor = int(input(f"Ingrese el valor {contador + 1}: "))
    suma = suma + valor
    contador = contador + 1

promedio = suma / tope

print(f"La suma total es: {suma}")
print(f"El promedio total es: {promedio:.2f}")