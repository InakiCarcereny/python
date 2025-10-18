from propietario import Propietario

class Inmueble_clase():
    def __init__(self, codigo: int, domicilio: str, metros_cuadrados: int, estado: int):
        if not isinstance(codigo, int):
            raise TypeError("Codigo tiene que ser un entero")
        if codigo < 0:
            raise ValueError("Codigo tiene que ser un numero positivo")
        
        if not isinstance(domicilio, str):
            raise TypeError("Domicilio tiene que ser un string")
        if domicilio == "" or domicilio.isspace():
            raise ValueError("Domicilio no puede estar vacio")
        
        if not isinstance(metros_cuadrados, int):
            raise TypeError("Metros cuadrados tiene que ser un entero")
        if metros_cuadrados <= 0:
            raise ValueError("Metros cudrados tiene que ser un numero valido")
        
        if not isinstance(estado, int):
            raise TypeError("Estado tiene que ser un entero")
        if estado <= 0:
            raise ValueError("Estado tiene que ser un numero valido")

        self._codigo = codigo
        self._domicilio = domicilio
        self._metros_cuadrados = metros_cuadrados
        self._estado = estado
        self._propietario = None

    def establecer_codigo(self, codigo: int):
        if not isinstance(codigo, int):
            raise TypeError("Codigo tiene que ser un entero")
        if codigo < 0:
            raise ValueError("Codigo tiene que ser un numero positivo")

        self._codigo = codigo

    def establecer_domicilio(self, domicilio: str):
        if not isinstance(domicilio, str):
            raise TypeError("Domicilio tiene que ser un string")
        if domicilio == "" or domicilio.isspace():
            raise ValueError("Domicilio no puede estar vacio")

        self._domicilio = domicilio

    def establecer_metros_cuadrados(self, metros_cuadrados: int):
        if not isinstance(metros_cuadrados, int):
            raise TypeError("Metros cuadrados tiene que ser un entero")
        if metros_cuadrados <= 0:
            raise ValueError("Metros cudrados tiene que ser un numero valido")

        self._metros_cuadrados = metros_cuadrados

    def establecer_estado(self, estado: int):
        if not isinstance(estado, int):
            raise TypeError("Estado tiene que ser un entero")
        if estado <= 0:
            raise ValueError("Estado tiene que ser un numero valido")

        self._estado = estado

    def establecer_propietario(self, propietario: 'Propietario'):
        if not isinstance(propietario, Propietario):
            raise TypeError("Propietario tiene que ser una instancia de Propietario")

        self._propietario = propietario

    def obtener_codigo(self) -> int:
        return self._codigo
    
    def obtener_domicilio(self) -> str:
        return self._domicilio
    
    def obtener_metros_cuadrados(self) -> int:
        return self._metros_cuadrados
    
    def obtener_estado(self) -> int:
        return self._estado

    def obtener_propietario(self) -> Propietario | None:
        return self._propietario

    def costo_alquiler(self, base: int) -> float | int:
        if not isinstance(base, int):
            raise TypeError("Base tiene que ser un entero")
        if base <= 0:
            raise ValueError("Base tiene que ser un numero valido")

        return base + (100 * self._metros_cuadrados)
    
    def precio_venta(self, m2: int) -> float | int:
        if not isinstance(m2, int):
            raise TypeError("Metros cuadrados tiene que ser un entero")
        if m2 <= 0:
            raise ValueError("Metros cuadrados tiene que ser un numero valido")

        return self._metros_cuadrados * m2

    def __str__(self) -> str:
        return (
            f"Codigo: {self._codigo}\n"
            f"Domicilio: {self._domicilio}\n"
            f"Propietario: {self._propietario}\n"
            f"Metros cuadrados: {self._metros_cuadrados}\n"
            f"Estado: {self._estado}\n"
        )