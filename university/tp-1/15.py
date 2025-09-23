texto = input("Ingrese un texto: ")

contador_puntuacion = 0
palabras_separadas = 0

for i in texto:
    if i == ',' or i == '.':
        contador_puntuacion = contador_puntuacion + 1
    if i == ' ':
        palabras_separadas = palabras_separadas + 1

total_caracteres = len(texto)
total_letras = len(texto) - contador_puntuacion

print(f"El numero total de caracteres es: {total_caracteres}")
print(f"La cantidad total de letras es: {total_letras}")
print(f"La cantidad total de palabras separadas por coma es: {palabras_separadas + 1}")

