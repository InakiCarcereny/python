personas = {
    "Ana": 25,
    "Luis": 17,
    "María": 30,
    "Jorge": 15,
    "Lucía": 22
}

edad_minima = int(input("Ingrese la edad mínima: "))

mayores = [nombre for nombre, edad in personas.items() if edad > edad_minima]

print(mayores)
