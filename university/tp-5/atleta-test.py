from atleta import Atleta

class Test:
  @staticmethod
  def ejecutar():
    try:
      atleta1 = Atleta("Inaki")
      atleta2 = Atleta("Luca")

      print(f"La energia actual de {atleta1.obtener_nombre()} es: {atleta1.obtener_energia()}")
      print(f"La energia actual de {atleta2.obtener_nombre()} es: {atleta2.obtener_energia()}")

      print(f"La destreza actual de {atleta1.obtener_nombre()} es: {atleta1.obtener_destreza()}")

      print(f"La cantidad de entrenamientos de {atleta1.obtener_nombre()} es: {atleta1.obtener_cantidad_entrenamientos()}")

      for _ in range(5):
        atleta1.entrenar()
        print(f"La energia actual de {atleta1.obtener_nombre()} es: {atleta1.obtener_energia()}")
        print(f"La cantidad de entrenamientos de {atleta1.obtener_nombre()} es: {atleta1.obtener_cantidad_entrenamientos()}")
      
      if atleta1.puede_aumentar_destreza():
        print(f"El atleta {atleta1.obtener_nombre()} aumento su destreza en 1")
        print(f"La destreza actual de {atleta1.obtener_nombre()} es: {atleta1.obtener_destreza()}")
      else:
        print(f"El atleta {atleta1.obtener_nombre()} NO aumento su destreza en 1")

      atleta1.descansar()
      print(f"La energia actual de {atleta1.obtener_nombre()} es: {atleta1.obtener_energia()}")

      if atleta1.mayor_destreza_que(atleta2):
        print(f"El atleta {atleta1.obtener_nombre()} tiene mayor destreza que {atleta2.obtener_nombre()}")
      else:
        print(f"El atleta {atleta1.obtener_nombre()} NO tiene mayor destreza que {atleta2.obtener_nombre()}")

      if atleta1.misma_destreza_que(atleta2):
        print(f"El atleta {atleta1.obtener_nombre()} tiene la misma destreza que {atleta2.obtener_nombre()}")
      else:
        print(f"El atleta {atleta1.obtener_nombre()} NO tiene la misma destreza que {atleta2.obtener_nombre()}")

      nuevo_nombre = input("Ingrese el nuevo nombre: ")
      atleta2.establecer_nombre(nuevo_nombre)

      print(f"El nuevo nombre del atleta2 es: {atleta2.obtener_nombre()}")

    except ValueError as e:
      print(f"{e}")
    except TypeError as e:
      print(f"{e}")

if __name__ == "__main__":
  Test.ejecutar()


