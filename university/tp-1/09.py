a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
x = int(input("Ingrese el tercer numero: "))

for i in range(a, b + 1):
    if i % x == 0:
        print(i)