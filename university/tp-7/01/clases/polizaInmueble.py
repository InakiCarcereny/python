from abc import ABC, abstractmethod

class Poliza_inmueble(ABC):
    def __init__(self, numero: int, incendio: float | int, explosion: float | int, robo: float | int):
        if not isinstance(numero, int):
            raise TypeError("Numero tiene que ser un entero")
        if numero <= 0:
            raise ValueError("Numero no puede ser menor o igual a 0")
        
        if not isinstance(incendio, float, int): # type: ignore
            raise TypeError("Incendio tiene que ser un entero o decimal")
        if incendio < 0:
            raise ValueError("Incendio no puede ser 0")
        
        if not isinstance(explosion, float, int): # type: ignore
            raise TypeError("Explosion tiene que ser un entero o decimal")
        if explosion < 0:
            raise ValueError("Explosion no puede ser 0")

        if not isinstance(robo, float, int): # type: ignore
            raise TypeError("Robo tiene que ser un entero o decimal")
        if robo < 0:
            raise ValueError("Robo no puede ser 0")

        self._numero = numero
        self._incendio = incendio
        self._explosion = explosion
        self._robo = robo

    def establecer_numero(self, numero: int):
        if not isinstance(numero, int):
            raise TypeError("Numero tiene que ser un entero")
        if numero <= 0:
            raise ValueError("Numero no puede ser menor o igual a 0")
        
        self._numero = numero

    def establecer_incendio(self, incendio: float | int):
        if not isinstance(incendio, float, int): # type: ignore
            raise TypeError("Incendio tiene que ser un entero o decimal")
        if incendio < 0:
            raise ValueError("Incendio no puede ser 0")
        
        self._incendio = incendio

    def establecer_explosion(self, explosion: float | int):
        if not isinstance(explosion, float, int): # type: ignore
            raise TypeError("Explosion tiene que ser un entero o decimal")
        if explosion < 0:
            raise ValueError("Explosion no puede ser 0")

        self._explosion = explosion

    def establecer_robo(self, robo: float | int):
        if not isinstance(robo, float, int): # type: ignore
            raise TypeError("Robo tiene que ser un entero o decimal")
        if robo < 0:
            raise ValueError("Robo no puede ser 0")
        self._robo = robo

    def obtener_numero(self) -> int:
        return self._numero
    
    def obtener_incendio(self) -> float | int:
        return self._incendio
    
    def obtener_explosion(self) -> float | int:
        return self._explosion
    
    def obtener_robo(self) -> float | int:
        return self._robo

    @abstractmethod
    def costo_poliza(self) -> float | int:
        pass
    
    def __str__(self) -> str:
        return f"{self._numero} - INCENDIO: {self._incendio} - EXPLOSION: {self._explosion} - ROBO: {self._robo}"