alto = int(input("Ingrese el alto del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))

while alto > 40 or ancho > 40:
    alto = int(input("Ingrese el alto del rectangulo: "))
    ancho = int(input("Ingrese el ancho del rectangulo: "))

for i in range(alto):
    for j in range(ancho):
        print("*", end='')
    print()