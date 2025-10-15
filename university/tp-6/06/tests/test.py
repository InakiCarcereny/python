from clases.participante import Participante
from clases.disciplinas import Disciplinas

class Test:
  @staticmethod
  def ejecutar():
    try:
      p1 = Participante("Inaki", 20, "Argentina")
      p2 = Participante("Luca", 20, "Argentina")

      print(p1.obtener_nombre())
      print(p1.obtener_edad())
      print(p1.obtener_nacionalidad())

      d1 = Disciplinas("Lanzamiento jabalina", "Los participantes tiene que tirar una jabalina lo mas lejos que puedan")
      d2 = Disciplinas("Salto en longitud", "Los participantes tendran que saltar lo mas lejos que pueda")

      p1.agregar_disciplina(d1)
      p2.agregar_disciplina(d2)
      p1.agregar_disciplina(d2)
      p2.agregar_disciplina(d1)

      p1.obtener_disciplinas()
      p2.obtener_disciplinas()

      d1.agregar_participante(p1)
      d2.agregar_participante(p2)
    except ValueError as e:
      print(e)
    except TypeError as e:
      print(e)

if __name__ == '__main__':
  Test.ejecutar()