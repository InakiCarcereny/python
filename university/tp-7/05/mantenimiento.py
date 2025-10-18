from categoria import Categoria

class Mantenimiento(Categoria):
    def __init__(self, nombre: str, apellido: str, dni: int, legajo: int, area_asignado: str):
        super().__init__(nombre, apellido, dni)
        self.__legajo = legajo
        self.__area_asignado = area_asignado
        
    def establecer_legajo(self, legajo: int):
        self.__legajo = legajo

    def establecer_area_asignado(self, area_asignado: str):
        self.__area_asignado = area_asignado

    def obtener_legajo(self) -> int:
        return self.__legajo
    
    def obtener_area_asignado(self) -> str:
        return self.__area_asignado
    