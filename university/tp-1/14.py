texto = input("Ingrese un texto: ")

contador = 0

for i in texto:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        contador = contador + 1

print(f"La cantidad total de vocales es: {contador}")