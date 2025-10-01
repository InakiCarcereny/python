import math

class Especie:
    def __init__(self, nombre: str, machos: int = 0, hembras: int = 0, ritmo: float | int = 0):
        if not isinstance(hembras, int):
            raise TypeError("Cantidad de hembras tiene que ser un numero")
        if hembras < 0:
            raise ValueError("Cantidad de hembras tiene que ser un numero positivo")

        if not isinstance(machos, int):
            raise TypeError("Cantidad de machos tiene que ser un numero")
        if machos < 0:
            raise ValueError("Cantidad de machos tiene que ser un numero positivo")

        if not isinstance(ritmo, float | int):
            raise TypeError("Ritmo tiene que ser un numero")

        self.__nombre = nombre
        self.__machos = machos
        self.__hembras = hembras
        self.__ritmo = ritmo

    """COMANDOS"""
    def establecer_hembras(self, cant_hembras: int):
        if not isinstance(cant_hembras, int):
            raise TypeError("Cantidad de hembras tiene que ser un numero")
        if cant_hembras < 0:
            raise ValueError("Cantidad de hembras tiene que ser un numero positivo")

        self.__hembras = cant_hembras

    def establecer_machos(self, cant_machos: int):
        if not isinstance(cant_machos, int):
            raise TypeError("Cantidad de machos tiene que ser un numero")
        if cant_machos < 0:
            raise ValueError("Cantidad de machos tiene que ser un numero positivo")

        self.__machos = cant_machos

    def establecer_ritmo(self, ritmo: float | int):
        if not isinstance(ritmo, float | int):
            raise TypeError("Ritmo tiene que ser un numero")

        self.__ritmo = ritmo

    def actualizar_hembras(self, cant_hembras: int):
        if not isinstance(cant_hembras, int):
            raise TypeError("Cantidad de hembras tiene que ser un numero")

        calcular_can_hembras = self.__hembras + cant_hembras

        if calcular_can_hembras < 0:
            self.__hembras = 0
        else:
            self.__hembras = calcular_can_hembras

    def actualizar_machos(self, cant_machos: int):
        if not isinstance(cant_machos, int):
            raise TypeError("Cantidad de machos tiene que ser un numero")

        calcular_can_machos = self.__machos + cant_machos

        if calcular_can_machos < 0:
            self.__machos = 0
        else:
            self.__machos = calcular_can_machos

    def actualizar_ritmo(self, ritmo: float | int):
        self.__ritmo = ritmo

    """CONSULTAS"""
    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_machos(self) -> int:
        return self.__machos

    def obtener_hembras(self) -> int:
        return self.__hembras

    def obtener_ritmo(self) -> float | int:
        return self.__ritmo

    def poblacion_actual(self) -> int:
        return self.__hembras + self.__machos

    def poblacion_estimada(self, anios: int) -> int:
        if not isinstance(anios, int):
            raise TypeError("Anios tiene que ser un numero")
        if anios <= 0:
            raise ValueError("Anios tiene que ser un numero positivo")

        return int(self.poblacion_actual() * (1 + self.__ritmo) ** anios)

    def anios_para_poblacion(self, poblacion: int) -> int:
        if not isinstance(poblacion, int):
            raise TypeError("Poblacion tiene que ser un numero")
        if poblacion <= 0:
            raise ValueError("Poblacion tiene que ser un numero positivo")

        actual = self.poblacion_actual()

        if poblacion <= actual:
         return 0

        return math.ceil(math.log(poblacion / actual) / math.log(1 + self.__ritmo))

    def riesgo(self) -> str:
        if self.__ritmo > 0:
            return "Verde"
        elif self.__ritmo == 0:
            return "Amarillo"
        else:
            return "Rojo"

    def mas_hembras(self) -> bool:
        if self.__hembras > self.__machos:
            return True
        else:
            return False

    def mayor_ritmo(self, otra_especie: 'Especie') -> 'Especie':
        if not isinstance(otra_especie, Especie):
            raise TypeError("Otra especie tiene que ser una instancia de Especie")

        if self.__ritmo > otra_especie.__ritmo:
            return self
        else:
            return otra_especie

    def clonar(self) -> 'Especie':
        return Especie(self.__nombre, self.__machos, self.__hembras, self.__ritmo)

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}, Cantidad de machos: {self.__machos}, Cantidad de hembras: {self.__hembras}, Ritmo: {self.__ritmo}"

