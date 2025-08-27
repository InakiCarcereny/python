def reverso(texto: str) -> str:
    palabra_inversa = ''
    for i in reversed(texto):
        palabra_inversa = palabra_inversa + i
    print(palabra_inversa)

reverso(input("Ingrese una palabra: "))

def palindromo(texto: str) -> str:
    palabra1 = texto.lower()
    palabra2 = ''
    for i in reversed(texto):
        palabra2 = palabra2 + i
    if palabra1 == palabra2:
        print(f"La palabra {palabra1} es un palindromo")
    else:
        print(f"La palabra {palabra1} NO es un palindromo")

palindromo(input("Ingrese una palabra: "))