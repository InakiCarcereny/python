FILE_PATH = r"D:\Users\Iñaki\Desktop\Dev\python\university\tp-2\files\productos.txt"

productos = []

with open(FILE_PATH, "r") as archivo:
    for linea in archivo:
        lista = linea.strip().split(";")
        productos.append({
            "codigo": int(lista[0]), 
            "nombre": lista[1], 
            "precio": int(lista[2])
            })

producto_a_buscar = input("Ingrese el nombre del producto que quiere buscar: ").lower()

encontrado = False
precio_producto_encontrado = 0

for producto in productos:
    if producto["nombre"] == producto_a_buscar:
        precio_producto_encontrado = producto["precio"]
        encontrado = True

if encontrado:
    print(f"El precio de {producto_a_buscar} es: {precio_producto_encontrado}")
else:
    print(f"NO se encontro el producto: {producto_a_buscar}")