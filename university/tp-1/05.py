texto = input("Ingrese una cadena de texto: ")

cantidad_espacios = 0

for i in texto:
    if i == ' ':
        cantidad_espacios = cantidad_espacios + 1

print(f"La cantidad de espacios es: {cantidad_espacios}")