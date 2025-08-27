ruta = r"D:\Users\Iñaki\Desktop\Dev\python\university\tp-2\files\distancias.txt"

distancias = []

suma = 0

with open(ruta, "r") as archivo:
  for linea in archivo:
      convertida = int(linea.strip())
      suma = suma + convertida
      distancias.append(convertida)

promedio = suma / len(distancias)

for i in distancias:
    if i > promedio:
        print(f"{i} es mayor al promedio")

print(f"El promedio es: {promedio}")