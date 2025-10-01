from especie import Especie

import random

class Test:
    @staticmethod
    def ejecutar():
        try:
            nombre_especie1 = input("Ingrese el nombre de la especie 1: ")
            ritmo_especie1 = float(input("Ingrese el ritomo de la especie 1: "))
            cantidad_machos_especie1 = random.randint(0, 50)
            cantidad_hembras_especie1 = random.randint(0, 50)
            especie1 = Especie(nombre_especie1, cantidad_machos_especie1, cantidad_hembras_especie1, ritmo_especie1)

            nombre_especie2 = input("Ingrese el nombre de la especie 2: ")
            ritmo_especie2 = float(input("Ingrese el ritmo de la especie 2: "))
            cantidad_machos_especie2 = random.randint(0, 50)
            cantidad_hembras_especie2 = random.randint(0, 50)
            especie2 = Especie(nombre_especie2, cantidad_machos_especie2, cantidad_hembras_especie2, ritmo_especie2)

            print(especie1)
            print(especie2)

            especie1.establecer_hembras(25)
            print(f"Cantidad de hembras de la especie 1: {especie1.obtener_hembras()}")

            especie1.establecer_machos(25)
            print(f"Cantidad de machos de la especie 1: {especie1.obtener_machos()}")

            especie1.establecer_ritmo(50)
            print(f"Ritmo de la especie 1: {especie1.obtener_ritmo()}")

            especie1.actualizar_hembras(10)
            print(f"Cantidad de hembras de la especie 1 despues de la actualizacion: {especie1.obtener_hembras()}")

            especie1.actualizar_machos(10)
            print(f"Cantidad de machos de la especie 1 despues de la actualizacion: {especie1.obtener_machos()}")

            especie1.actualizar_ritmo(25)
            print(f"Ritmo de la especie 1 despues de la actualizacion: {especie1.obtener_ritmo()}")

            print(f"Nombre de la especie 1: {especie1.obtener_nombre()}")
            print(f"Nombre de la especie 2: {especie2.obtener_nombre()}")

            print(f"La poblacion actual de la especie 1 es: {especie1.poblacion_actual()}")

            print(f"La poblacion estimada de la especie 1 en 5 anios es: {especie1.poblacion_estimada(5)}")

            print(f"La cantidad de anios para 100 de poblacion es: {especie1.anios_para_poblacion(100)}")

            print(f"El riesgo de extincion de la especie 1 es: {especie1.riesgo()}") 

            if especie1.mas_hembras():
                print("Hay mas hembras que machos")
            else:
                print("Hay mas machos que hembras")

            especie_mayor_ritmo = especie1.mayor_ritmo(especie2)

            print(f"La especie con mayor ritmo es: {especie_mayor_ritmo.obtener_nombre()}")

            especie3 = especie1.clonar()

            print("Mostrar la nueva especie 3 clonada de la 1")
            print(especie3)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)

if __name__ == "__main__":
    Test.ejecutar()
