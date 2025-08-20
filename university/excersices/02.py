total_ventas = 0
venta_mas_alta = 0
venta = 1
venta_actual = 0
total = 0

while venta != 0 and venta > 0:
    venta = int(input("Ingrese la venta: "))
    if venta_actual < venta:
        venta_mas_alta = venta
    venta_actual = venta
    total = total + venta
    total_ventas = total_ventas + 1

promedio = total / total_ventas

print(f"La cantidad total fue: {total_ventas}")
print(f"La venta mas alta fue: {venta_mas_alta}")
print(f"El promedio fue: {promedio}")
print(f"El total fue: {total}")
