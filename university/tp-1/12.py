numero = 1
numero_actual = 1
esta_ordenada = True

while numero > 0:
    ingreso = input("Ingrese un numero entero positivo: ")
    numero = int(ingreso)
    if numero_actual > numero and numero != 0:
        esta_ordenada = False
    numero_actual = numero

if (esta_ordenada):
    print("La secuencia esta ordenada")
else:
    print("La secuencia NO esta ordenada")

