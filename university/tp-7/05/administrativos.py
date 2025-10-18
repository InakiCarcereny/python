from categoria import Categoria

class Administrativo(Categoria):
    def __init__(self, nombre: str, apellido: str, dni: int, legajo: int, posicion: str):
        super().__init__(nombre, apellido, dni)
        self.__legajo = legajo
        self.__posicion = posicion

    def establecer_legajo(self, legajo: int):
        self.__legajo = legajo

    def establecer_posicion(self, posicion: str):
        self.__posicion = posicion

    def obtener_legajo(self) -> int:
        return self.__legajo
    
    def obtener_posicion(self) -> str:
        return self.__posicion