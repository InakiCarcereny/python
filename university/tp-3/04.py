diccionario = {
    "arbol": "Planta de tronco leñoso que se ramifica a cierta altura del suelo.",
    "amigo": "Persona con la que se mantiene una relación de afecto y confianza.",
    "avión": "Aeronave capaz de desplazarse por el aire.",
    "barco": "Vehículo flotante que se utiliza para navegar por el agua.",
    "casa": "Edificio para habitar.",
    "camino": "Vía que se abre para transitar de un lugar a otro.",
    "sol": "Estrella luminosa en torno a la cual gira la Tierra.",
    "luz": "Radiación que hace visibles los objetos.",
}

inicial_buscada = input("Ingrese la inicial por la que quiere agregar palabras: ")

nueva_lista = [palabra for palabra in diccionario if palabra[0] == inicial_buscada]

print(nueva_lista)