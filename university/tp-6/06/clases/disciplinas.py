from participante import Participante

class Disciplinas:
    def __init__(self, nombre: str, descripcion: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre tiene que tener un valor")

        if not isinstance(descripcion, str):
            raise TypeError("Descripcion tiene que ser un string")
        if descripcion == "" or descripcion.isspace():
            raise ValueError("Descripcion tiene que tener un valor")

        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__participantes: list[Participante] = []

    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_descripcion(self) -> str:
        return self.__descripcion

    def obtener_participantes(self):
        for part in self.__participantes:
            print(part)
    
    def establecer_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre tiene que tener un valor")

        self.__nombre = nombre

    def establecer_descripcion(self, descripcion: str):
        if not isinstance(descripcion, str):
            raise TypeError("Descripcion tiene que ser un string")
        if descripcion == "" or descripcion.isspace():
            raise ValueError("Descripcion tiene que tener un valor")

        self.__descripcion = descripcion

    def agregar_participante(self, participante: Participante):
        if not isinstance(participante, Participante):
            raise TypeError("Participante debe ser una instancia de Participante")

        if participante not in self.__participantes:
            self.__participantes.append(participante)
        else:
            raise ValueError("Participante ya se encuentra")