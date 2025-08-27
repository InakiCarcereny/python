def validar(texto: str) -> int:
    while True:
        try:
          ingreso = input(texto)
          numero = int(ingreso)
          if numero > 0:
             return numero
          else:
             print("El numero debe ser mayor a 0")
        except ValueError:
           print("Ingrese un numero entero positivo")

numero = validar("Ingrese una cantidad de alumnos: ")

alumnos = []

for i in range(numero):
    alumno = {}
    alumno["nombre"] = input(f"Ingrese el nombre del alumno {i + 1}: ")
    alumno["nota"] = int(input(f"Ingrese la nota del alumno {i + 1}: "))
    alumnos.append(alumno)

for i in alumnos:
    print("Nombre:", i["nombre"])
    print("Nota:", i["nota"])
    if i["nota"] >= 40:
      print("Resultado: Aprobado")
    else:
      print("Resultado: Desaprobado")
    print("---")
   
