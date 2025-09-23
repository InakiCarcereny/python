numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El {numero1} es el mas grande")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El {numero2} es el mas grande")
else:
    print(f"El {numero3} es el mas grande")