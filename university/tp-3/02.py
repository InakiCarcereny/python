nombres = ["inaki", "luca", "gonzalo", "fernando"]

def nombres_mayor_a_x(longitud: int) -> list:
    return [nombre for nombre in nombres if len(nombre) >= longitud]

print(nombres_mayor_a_x(5))
print(nombres_mayor_a_x(6))