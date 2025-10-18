from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, patente: str, color: str, anio_fabricacion: int, precio: float, kilometraje: int, ancho_manubrio: float, cilindrada: int):
        super().__init__(marca, modelo, patente, color, anio_fabricacion, precio, kilometraje)
        self.__ancho_manubrio = ancho_manubrio
        self.__cilindrada = cilindrada

    def establecer_ancho_manubrio(self, ancho_manubrio: float):
        self.__ancho_manubrio = ancho_manubrio

    def establecer_cilindrada(self, cilindrada: int):
        self.__cilindrada = cilindrada

    def obtener_ancho_manubrio(self) -> float:
        return self.__ancho_manubrio
    
    def obtener_cilindrada(self) -> int:
        return self.__cilindrada