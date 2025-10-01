from auto import Auto

class Piloto:
    def __init__(self, nombre: str, apellido: str, numero_inscripcion: int, experiencia: float, auto: Auto):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__numero_inscripcion = numero_inscripcion
        self.__experiencia = experiencia
        self.__auto = auto
