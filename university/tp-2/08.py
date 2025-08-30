FILE_PATH = r"D:\Users\Iñaki\Desktop\Dev\python\university\tp-2\files\stock.txt"
OUTPUT_PATH = r"D:\Users\Iñaki\Desktop\Dev\python\university\tp-2\files\compras.txt"

productos = []

with open(FILE_PATH, "r") as archivo:
    for linea in archivo:
        lista = linea.strip().split(";")
        productos.append({
            "codigo de producto": int(lista[0]),
            "stock minimo": int(lista[1]),
            "stock real": int(lista[2])
        })

with open(OUTPUT_PATH, "w") as salida:
    for producto in productos:
        if producto["stock real"] < producto["stock minimo"]:
            salida.write(f"{producto["codigo de producto"]};{producto["stock minimo"]};{producto["stock real"]} \n")
            print(producto)