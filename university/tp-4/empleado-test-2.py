from empleado import Empleado

class Test:
  @staticmethod
  def ejecutar():
    try:
      empleado = Empleado(2)
      empleado.establecer_horas_trabajadas(5)
      empleado.establecer_valor_hora(3.5)
      print(f"legajo: {empleado.obtener_legajo()}, sueldo: {empleado.obtener_sueldo()}")
    except TypeError as e:
      print(f"{e}")
    except ValueError as e:
      print(f"{e}")

if __name__ == "__main__":
    Test.ejecutar()