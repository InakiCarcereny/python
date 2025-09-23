lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("Triangulo equilatero")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Triangulo isoceles")
else:
    print("Triangulo escaleno")