from libro import Libro
import json

class Test:
    @staticmethod
    def ejecutar():
        datos_desde_json: list[Libro] = []

        with open("libros.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
                
        for item in datos:
            try:
                l = Libro.desde_json(item)
                datos_desde_json.append(l)
            except (TypeError, ValueError) as e:
                print(f"Error al crear libro: {e}")

        # PUNTO A
        # for libro in datos_desde_json:
        #     print(libro)

        # PUNTO B
        anio_a_buscar = int(input("Ingrese un anio de publicacion a buscar: "))

        for libro in datos_desde_json:
            if libro.obtener_anio_publicacion() == anio_a_buscar:
                print(libro)


if __name__ == "__main__":
    Test.ejecutar()