from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: str, patente: str, color: str, anio_fabricacion: int, precio: float, kilometraje: int, puertas: int, aire: bool):
        super().__init__(marca, modelo, patente, color, anio_fabricacion, precio, kilometraje)
        self.__puertas = puertas
        self.__aire = aire

    def establecer_puertas(self, puertas: int):
        self.__puertas = puertas

    def establecer_aire(self, aire: bool):
        self.__aire = aire

    def obtener_puertas(self) -> int:
        return self.__puertas
    
    def obtener_aire(self) -> bool:
        return self.__aire
