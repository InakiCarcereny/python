from fecha import Fecha

class Socio:
    def __init__(self, nombre: str, fecha_nacimiento: Fecha):
        self.__nombre = nombre
        self.__fecha_nacimiento = fecha_nacimiento
        self.__fecha_penalizacion: Fecha | None = None

    """COMANDOS"""

    def establecer_nombre(self, nombre: str):
        self.__nombre = nombre

    def establecer_fecha_nacimiento(self, fecha_nacimiento: Fecha):
        self.__fecha_nacimiento = fecha_nacimiento

    def establecer_fecha_penalizacion(self, fecha_penalizacion: Fecha):
        self.__fecha_penalizacion = fecha_penalizacion

    """CONSULTAS"""

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_fecha_nacimiento(self) -> Fecha:
        return Fecha(self.__fecha_nacimiento.__dia, 0, 0)

    def obtener_fecha_penalizacion(self) -> Fecha:
        return Fecha(0, 0, 0)

    def esta_habilitado(self, fecha: Fecha) -> bool:
        return True

    def __str__(self):
        return f"Nombre: {self.__nombre}, Fecha nacimiento: {self.__fecha_nacimiento}, Fecha penalizacion: {self.__fecha_penalizacion}"
