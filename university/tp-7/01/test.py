from polizaInmueble import Poliza_inmueble
from polizaInmuebleEscolar import Poliza_inmueble_escolar
from asegurador import Aseguradora

class Test:
    @staticmethod
    def ejecutar():
        try:
            pi1 = Poliza_inmueble(1111, 100, 150.00, 200)
            pi2 = Poliza_inmueble(2222, 50, 100, 150)

            pie1 = Poliza_inmueble_escolar(3333, 25, 50, 75, 2, 2, 2, 2)
            pie2 = Poliza_inmueble_escolar(4444, 50, 100, 150, 2, 2, 2, 2)

            print(pi1)
            print("--------------------------------------")
            print(pi2)
            print("--------------------------------------")
            print(pie1)
            print("--------------------------------------")
            print(pie2)
            print("--------------------------------------")

            a1 = Aseguradora()
            a2 = Aseguradora()

            a1.insertar(pi1)
            a1.insertar(pie1)

            for poliza in a1.obtener_polizas():
                print(f"{poliza} en la aseguradora 1")
            print("--------------------------------------")

            a2.insertar(pi2)
            a2.insertar(pie2)

            for poliza in a2.obtener_polizas():
                print(f"{poliza} en la aseguradora 2")
            print("--------------------------------------")

            a1.eliminar(pie1)
            for poliza in a1.obtener_polizas():
                print(f"{poliza} en la aseguradora 1")
            print("--------------------------------------")

            if a1.existe_poliza(pie1):
                print("La poliza existe")
            else:
                print("La poliza NO existe")

            if a1.existe_poliza(pi1):
                print("La poliza existe")
            else:
                print("La poliza NO existe")

            if a1.hay_polizas():
                print("La aseguradora tiene polizas")
            else:
                print("La aseguradora NO tiene polizas")

            print(f"Costo total aseguradora 1: {a1.costo_total()}")
            print(f"Cosot total aseguradora 2: {a2.costo_total()}")

            if a1.es_igual(a2):
                print("Las aseguradoras son iguales")
            else:
                print("Las aseguradoras NO son iguales")

        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    Test.ejecutar()