from categoria import Categoria

class Programador(Categoria):
    def __init__(self, nombre: str, apellido: str, dni: int, legajo: int, proyecto_asignado: str):
        super().__init__(nombre, apellido, dni)
        self.__legajo = legajo
        self.__proyecto_asignado = proyecto_asignado

    def establecer_legajo(self, legajo: int):
        self.__legajo = legajo
  
    def establecer_proyecto_asignado(self, proyecto_asignado: str):
        self.__proyecto_asignado = proyecto_asignado

    def obtener_legajo(self) -> int:
        return self.__legajo

    def obtener_proyecto_asignado(self) -> str:
        return self.__proyecto_asignado