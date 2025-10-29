import json
from contacto import Contacto

class Test:
    @staticmethod
    def ejecutar():
        datos = [
            Contacto("Juan", "Pérez", "123456789", "juan@example.com", "Calle Falsa 123"),
            Contacto("María", "Gómez", "987654321", "maria@example.com", "Av. Siempre Viva 742"),
            Contacto("Pedro", "López", "555555555", "pedro@example.com", "Ruta 8 km 15")
        ]

        contactos = []

        for contacto in datos:
            contactos.append(contacto.a_json())

        with open("contactos.json", "w", encoding = "utf-8") as archivo:
            json.dump(contactos, archivo, ensure_ascii = False, indent = 2)

        print("Archivo contactos.json creado correctamente.")

        contactos_desde_json: list[Contacto] = []

        with open("contactos.json", "r", encoding = "utf-8") as archivo:
            datos_json = json.load(archivo)

        for item in datos_json:
            try:
                c = Contacto.desde_json(item)
                contactos_desde_json.append(c)
            except (ValueError, TypeError) as e:
                print(f"Error al crear el contacto: {e}")

        for contacto in contactos_desde_json:
            print(contacto)

        apellido_a_buscar = input("Ingrese una inicial de apellido a buscar: ")

        contactos_encontrados: list[Contacto] = []

        for contacto in contactos_desde_json:
            if contacto.obtener_apellido().lower().startswith(apellido_a_buscar):
                contactos_encontrados.append(contacto)

        if len(contactos_encontrados) > 0:
            for c in contactos_encontrados:
                print(c)
        else:
            print("NO se encontraron contactos con esa inicial")

if __name__ == "__main__":
    Test.ejecutar()