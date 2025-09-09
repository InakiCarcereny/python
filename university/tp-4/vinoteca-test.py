from vinoteca import Vinoteca

class Test:
  @staticmethod
  def ejecutar():
    try:
      vinoteca = Vinoteca()
      print(f"jugos: {vinoteca.obtener_cantidad_jugos()}")
      print(f"blancos: {vinoteca.obtener_cantidad_blancos()}")
      print(f"vinos jovenes: {vinoteca.obtener_cantidad_tinto_jovenes()}")
      print(f"vinos aniejados: {vinoteca.obtener_cantidad_tinto_aniejados()}")

      vinoteca.vender_jugos(250)

      print(f"jugos restantes: {vinoteca.obtener_cantidad_jugos()}")

      vinoteca.reponer_jugos()

      vinoteca.vender_jugos(4900)

      print(f"jugos restantes: {vinoteca.obtener_cantidad_jugos()}")
    except ValueError as e:
      print(f"{e}")
    except TypeError as e:
      print(f"{e}")

if __name__ == "__main__":
  Test.ejecutar()