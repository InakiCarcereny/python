from modelos.entidades.polizaInmueble import PolizaInmueble

class PolizaInmuebleEscolar(PolizaInmueble):
    @classmethod
    def from_diccionario(cls, data: dict) -> 'PolizaInmuebleEscolar':
        if not isinstance(data, dict):
            raise TypeError("Data tiene que ser un diccionario")
        
        requerido = [
            "numero", "incendio", "explosion", "robo",
            "cant_personas", "monto_equipamiento",
            "monto_mobiliario", "monto_persona"
        ]

        for campo in requerido:
            if campo not in data:
                raise ValueError(f"Falta el campo requerido: {campo}")
        
        return cls(
            numero = data["numero"],
            incendio = data["incendio"],
            explosion = data["explosion"],
            robo = data["robo"],
            cant_personas = data["cant_personas"],
            monto_equipamiento = data["monto_equipamiento"],
            monto_mobiliario = data["monto_mobiliario"],
            monto_persona = data["monto_persona"]
        )
    
    def __init__(self, numero: int, incendio: int | float, explosion: int | float, robo: int | float, cant_personas: int, monto_equipamiento: int | float, monto_mobiliario: int | float, monto_persona: int | float):
        super().__init__(numero, incendio, explosion, robo)

        if not isinstance(cant_personas, int):
            raise TypeError("Cantidad personas tiene que ser un numero entero")
        if cant_personas < 0:
            raise ValueError("Cantidad personas tiene que ser positivo")
        
        if not isinstance(monto_equipamiento, (int, float)):
            raise TypeError("Monto equipamiento tiene que ser un numero entero o con decimales")
        if monto_equipamiento < 0:
            raise ValueError("Monto equipamiento tiene que ser positivo")
        
        if not isinstance(monto_mobiliario, (int, float)):
            raise TypeError("Monto mobiliario tiene que ser un numero entero o con decimales")
        if monto_mobiliario < 0:
            raise ValueError("Monto mobiliario tiene que ser positivo")
        
        if not isinstance(monto_persona, (int, float)):
            raise TypeError("Monto persona tiene que ser un numero entero o con decimales")
        if monto_persona < 0:
            raise ValueError("Monto persona tiene que ser positivo")
        
        self.__cant_personas = cant_personas
        self.__monto_equipamiento = monto_equipamiento
        self.__monto_mobiliario = monto_mobiliario
        self.__monto_persona = monto_persona

    def obtener_cant_personas(self) -> int:
        return self.__cant_personas
    
    def obtener_monto_equipamiento(self) -> int | float:
        return self.__monto_equipamiento
    
    def obtener_monto_mobiliario(self) -> int | float:
        return self.__monto_mobiliario
    
    def obtener_monto_persona(self) -> int | float:
        return self.__monto_persona
    
    def establecer_cant_personas(self, cant_personas: int):
        self.__cant_personas = cant_personas

    def establecer_monto_equipamiento(self, monto_equipamiento: int | float):
        self.__monto_equipamiento = monto_equipamiento

    def establecer_monto_mobiliario(self, monto_mobiliario: int | float):
        self.__monto_mobiliario = monto_mobiliario

    def establecer_monto_persona(self, monto_persona: int | float):
        self.__monto_persona = monto_persona

    def valor_mensual_poliza(self) -> int | float:
        base = (self._incendio * 0.01) + (self._explosion * 0.01) + (self._robo * 0.02)
        extra = (self.__monto_equipamiento * 0.01) + (self.__monto_mobiliario * 0.01)
        personas = self.__cant_personas * self.__monto_persona * 0.01

        return base + extra + personas
    
    def to_diccionario(self) -> dict:
        return {
            'numero': self._numero,
            'incendio': self._incendio,
            'explosion': self._explosion,
            'robo': self._robo,
            'cant_personas': self.__cant_personas,
            'monto_equipamiento': self.__monto_equipamiento,
            'monto_mobiliario': self.__monto_mobiliario,
            'monto_persona': self.__monto_persona
        }
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"cantidad personas: {self.__cant_personas} \n"
            f"monto equipamiento: {self.__monto_equipamiento} \n"
            f"monto mobiliario: {self.__monto_mobiliario} \n"
            f"monto persona: {self.__monto_persona} \n"
        )