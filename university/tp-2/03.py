notas = []

nota = input("Ingrese la cantidad de notas que quiere anotar: ")
transformar = int(nota)

nota_mas_alta = 0
indice = 0

for i in range(transformar):
    nota_ingresada = int(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota_ingresada)
    if (nota_ingresada > nota_mas_alta):
        nota_mas_alta = nota_ingresada
        indice = i

for j in notas:
    print(j)

print(f"La nota mas alta fue: {nota_mas_alta}, y se encuentra en el indice: {indice}")
