from empleado import Empleado

class Test:
  @staticmethod
  def ejecutar():
    try:
      empleado1 = Empleado(1, 10, 4.5)
      print(f"legajo: {empleado1.obtener_legajo()}")
      print(f"cantidad horas trabajadas: {empleado1.obtener_horas_trabajadas()}")
      print(f"valor de la hora: {empleado1.obtener_valor_hora()}")
      print(f"El legajo es {empleado1.obtener_legajo()} y su sueldo es ${empleado1.obtener_sueldo()}")
    except ValueError as e:
      print(f"{e}")
    except TypeError as e:
      print(f"{e}")

if __name__ == "__main__":
    Test.ejecutar()