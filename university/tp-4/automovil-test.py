import random

from automovil import Automovil

class Test:
  @staticmethod
  def ejecutar():
    try:
      automovil = Automovil("ferrari", "488 pista", 2023, 220.0, 100.0)
      cantidad_iteraciones = int(input("Ingrese la cantidad de iteraciones que desea realizar: "))
      for _ in range(cantidad_iteraciones):
        numero_iteracion = random.randint(0, 3)

        if numero_iteracion == 0:
          print(f"velocidad: {automovil.obtener_velocidad_actual()}")
          print("acelerar")
          automovil.acelerar(20)
          print(f"velocidad: {automovil.obtener_velocidad_actual()}")
        elif numero_iteracion == 1:
          print(f"velocidad: {automovil.obtener_velocidad_actual()}")
          print("desacelerar")
          automovil.desacelerar(15)
          print(f"velocidad: {automovil.obtener_velocidad_actual()}")
        elif numero_iteracion == 2:
          print(f"velocidad: {automovil.obtener_velocidad_actual()}")
          print("frenar")
          automovil.frenar_completo()
          print(f"velocidad: {automovil.obtener_velocidad_actual()}")
        else:
          velocidad = automovil.calcular_minutos_para_llegar(50)
          if (velocidad > 0):
            print(f"El tiempo para llega es de {velocidad} minutos")
          else:
            print("No se puede calcular porque el auto esta frenado")
    except ValueError as e:
      print(f"{e}")
    except TypeError as e:
      print(f"{e}")

if __name__ == "__main__":
  Test.ejecutar()