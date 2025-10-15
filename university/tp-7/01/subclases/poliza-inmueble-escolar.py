from clases.polizaInmueble import Poliza_inmueble

class Poliza_inmueble_escolar(Poliza_inmueble):
    def __init__(self, numero: int, incendio: float | int, explosion: float | int, robo: float | int, cant_personas: int, monto_equipamiento: float | int, monto_mobiliario: float | int, monto_persona: float | int):
        super().__init__(numero, incendio, explosion, robo)
        if not isinstance(cant_personas, int):
            raise TypeError("Cantidad personas tiene que ser un entero o decimal")
        if cant_personas < 0:
            raise ValueError("Cantidad personas no puede ser 0")

        if not isinstance(monto_equipamiento, float, int): # type: ignore
            raise TypeError("Monto equipamiento tiene que ser un entero o decimal")
        if monto_equipamiento < 0:
            raise ValueError("Monto equipamiento no puede ser 0")

        if not isinstance(monto_mobiliario, float, int): # type: ignore
            raise TypeError("Monto mobiliario tiene que ser un entero o decimal")
        if monto_mobiliario < 0:
            raise ValueError("Monto mobiliario no puede ser 0")

        if not isinstance(monto_persona, float, int): # type: ignore
            raise TypeError("Monto persona tiene que ser un entero o decimal")
        if monto_persona < 0:
            raise ValueError("Monto persona no puede ser 0")

        self.__cant_personas = cant_personas
        self.__monto_equipamiento = monto_equipamiento
        self.__monto_mobiliario = monto_mobiliario
        self.__monto_persona = monto_persona

    def establecer_cant_personas(self, cant_personas: float | int):
        self.__cant_personas = cant_personas

    def establecer_monto_equipamiento(self, monto_equipamiento: float | int):
        self.__monto_equipamiento = monto_equipamiento

    def establecer_monto_mobiliario(self, monto_mobiliario: float | int):
        self.__monto_mobiliario = monto_mobiliario

    def establecer_monto_persona(self, monto_persona: float | int):
        self.__monto_persona = monto_persona

    def obtener_cant_personas(self) -> int:
        return self.__cant_personas

    def obtener_monto_equipamiento(self) -> float | int:
        return self.__monto_equipamiento
    
    def obtener_monto_mobiliario(self) -> float | int:
        return self.__monto_mobiliario
    
    def obtener_monto_persona(self) -> float | int:
        return self.__monto_persona

    def costo_poliza(self) -> float | int:
        return 0.00

    def __str__(self) -> str:
        return f"{super().__str__()}, Cantidad personas: {self.__cant_personas}, Monto equipamiento: {self.__monto_equipamiento}, Monto mobiliario: {self.__monto_mobiliario}, Monto persona: {self.__monto_persona}"
