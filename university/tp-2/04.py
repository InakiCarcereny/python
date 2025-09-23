digitos = []

def validar(mensaje: str) -> str:
    while True:
        ingreso = input(mensaje)
        if ingreso.isdigit():
            return ingreso
        print("Tiene que ingresar un numero")

numero_string = validar("Ingresa un numero: ")

for i in numero_string:
    numero_numero = int(i)
    digitos.append(numero_numero)

digito_mayor = digitos[0]

for i in range(len(digitos)):
    if digitos[i] > digito_mayor:
        digito_mayor = digitos[i]

indice = digitos.index(digito_mayor)

print(f"El digito mayor fue: {digito_mayor}, y se encuentra en la posicion: {indice}")