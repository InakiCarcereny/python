from combustible import Combustible

class Vehiculo:
    def __init__(self, marca: str, modelo: str, patente: str, color: str, anio_fabricacion: int, precio: float, kilometraje: int):
        self._marca = marca
        self._modelo = modelo
        self._patente = patente
        self._color = color
        self._anio_fabricacion = anio_fabricacion
        self._precio = precio
        self._kilometraje = kilometraje
        self._combustible: type[Combustible] = Combustible

    def establecer_marca(self, marca: str):
        self._marca = marca
    
    def establecer_modelo(self, modelo: str):
        self._modelo = modelo

    def establecer_patente(self, patente: str):
        self._patente = patente

    def establecer_color(self, color: str):
        self._color = color

    def establcer_anio_fabricacion(self, anio_fabricacion: int):
        self._anio_fabricacion = anio_fabricacion

    def establecer_precio(self, precio: float):
        self._precio = precio

    def establecer_kilometraje(self, kilometraje: int):
        self._kilometraje = kilometraje

    def obtener_marca(self) -> str:
        return self._marca
    
    def obtener_modelo(self) -> str:
        return self._modelo
    
    def obtener_patente(self) -> str:
        return self._patente
    
    def obtener_color(self) -> str:
        return self._color
    
    def obtener_anio_fabricacion(self) -> int:
        return self._anio_fabricacion
    
    def obtener_precio(self) -> float:
        return self._precio
    
    def obtener_kilometraje(self) -> int:
        return self._kilometraje