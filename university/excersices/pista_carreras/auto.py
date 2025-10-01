class Auto:
    __VELOCIDAD = 0
    __VELOCIDAD_MIN = 0

    def __init__(self, marca: str, peso: float, velocidad_max: int, potencia_motor: int):
        self.__marca = marca
        self.__peso = peso
        self.__velocidad_max = velocidad_max
        self.__velocidad = Auto.__VELOCIDAD
        self.__velocidad_min = Auto.__VELOCIDAD_MIN
        self.__potencia_motor = potencia_motor

    """COMANDOS"""
    def establecer_marca(self, marca: str):
        self.__marca = marca

    def establecer_peso(self, peso: float):
        self.__peso = peso

    def establecer_velocidad_max(self, velocidad_max: int):
        self.__velocidad_max = velocidad_max

    def establecer_potencia_motor(self, potencia_motor: int):
        self.__potencia_motor = potencia_motor

    """CONSULTAS"""

    def obtener_marca(self) -> str:
        return self.__marca

    def obtener_peso(self) -> float:
        return self.__peso

    def obtener_velocidad_max(self) -> int:
        return self.__velocidad_max

    def obtener_potencia_motor(self) -> int:
        return self.__potencia_motor
