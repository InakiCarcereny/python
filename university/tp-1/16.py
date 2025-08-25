texto = input("Ingrese una oracion: ")

palabra = ''
palabra_mas_larga = ''
longitud_palabra_actual = 0

for i in texto:
    if i != ' ':              
        palabra = palabra + i
    else:                     
        if len(palabra) > longitud_palabra_actual:
            palabra_mas_larga = palabra
            longitud_palabra_actual = len(palabra)
        palabra = ''          

if len(palabra) > longitud_palabra_actual:
    palabra_mas_larga = palabra
    longitud_palabra_actual = len(palabra)

print(f"La palabra mas larga es: '{palabra_mas_larga}' y tiene {longitud_palabra_actual} caracteres")
