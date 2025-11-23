class PolizaInmueble:
    @classmethod
    def from_diccionario(cls, data: dict) -> 'PolizaInmueble':
        if not isinstance(data, dict):
            raise TypeError("Data tiene que ser un diccionario")
        if 'numero' not in data or 'incendio' not in data or 'explosion' not in data or 'robo' not in data:
            raise ValueError("Las claves numero, incendio, explosion, robo tienen que estar en el diccionario")
        
        return cls(
            numero = data['numero'],
            incendio = data['incendio'],
            explosion = data['explosion'],
            robo = data['robo']
        )
    
    def __init__(self, numero: int, incendio: int | float, explosion: int | float, robo: int | float):
        if not isinstance(numero, int):
            raise TypeError("Numero tiene que ser un numero entero")
        if numero < 0:
            raise ValueError("Numero tiene que ser un numero positivo")
        
        if not isinstance(incendio, (int, float)):
            raise TypeError("Incendio tiene que ser un numero entero o con decimales")
        if incendio < 0:
            raise ValueError("Incendio tiene que ser un numero positivo")
        
        if not isinstance(explosion, (int, float)):
            raise TypeError("Explosion tiene que ser un numero entero o con decimales")
        if explosion < 0:
            raise ValueError("Explosion tiene que ser un numero positivo")
        
        if not isinstance(robo, (int, float)):
            raise TypeError("Robo tiene que ser un numero entero o con decimales")
        if robo < 0:
            raise ValueError("Robo tiene que ser un numero positivo")
        
        self._numero = numero
        self._incendio = incendio
        self._explosion = explosion
        self._robo = robo

    def obtener_numero(self) -> int:
        return self._numero
    
    def obtener_incendio(self) -> int | float:
        return self._incendio
    
    def obtener_explosion(self) -> int | float:
        return self._explosion
    
    def obtener_robo(self) -> int | float:
        return self._robo
    
    def establecer_numero(self, numero: int):
        if not isinstance(numero, int):
            raise TypeError("Numero tiene que ser un numero entero")
        if numero < 0:
            raise ValueError("Numero tiene que ser un numero positivo")
        
        self._numero = numero

    def establecer_incendio(self, incendio: int | float):
        if not isinstance(incendio, (int, float)):
            raise TypeError("Incendio tiene que ser un numero entero o con decimales")
        if incendio < 0:
            raise ValueError("Incendio tiene que ser un numero positivo")
        
        self._incendio = incendio

    def establecer_explosion(self, explosion: int | float):
        if not isinstance(explosion, (int, float)):
            raise TypeError("Explosion tiene que ser un numero entero o con decimales")
        if explosion < 0:
            raise ValueError("Explosion tiene que ser un numero positivo")
        
        self._explosion = explosion

    def establecer_robo(self, robo: int | float):
        if not isinstance(robo, (int, float)):
            raise TypeError("Robo tiene que ser un numero entero o con decimales")
        if robo < 0:
            raise ValueError("Robo tiene que ser un numero positivo")
        
        self._robo = robo

    def valor_mensual_poliza(self) -> int | float:
        return (self._incendio * 0.02) + (self._explosion * 0.01) + (self._robo * 0.03)
    
    def to_diccionario(self) -> dict:
        return {
            'numero': self._numero,
            'incendio': self._incendio,
            'explosion': self._explosion,
            'robo': self._robo
        }
    
    def __str__(self) -> str:
        return (
            f"numero: {self._numero} \n"
            f"incendio: {self._incendio} \n"
            f"explosion: {self._explosion} \n"
            f"robo: {self._robo}"
        )