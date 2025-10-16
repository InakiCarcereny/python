from inmueble import Inmueble

class Departamento(Inmueble):
    def __init__(self, codigo: int, domicilio: str, metros_cuadrados: int, estado: int, gastos_comunes: float | int, cochera: bool):
        super().__init__(codigo, domicilio, metros_cuadrados, estado)
        if not isinstance(gastos_comunes, (float, int)):
            raise TypeError("Gastos comunes tiene que ser un entero o decimal")
        if gastos_comunes <= 0:
            raise ValueError("Gastos comunes tiene que ser un numero valido")
        
        if not isinstance(cochera, bool):
            raise TypeError("Cochera tiene que ser un booleano")
        
        self.__gastos_comunes = gastos_comunes
        self.__cochera = cochera

    def establecer_gastos_comunes(self, gastos_comunes: float | int):
        if not isinstance(gastos_comunes, (float, int)):
            raise TypeError("Gastos comunes tiene que ser un entero o decimal")
        if gastos_comunes <= 0:
            raise ValueError("Gastos comunes tiene que ser un numero valido")

        self.__gastos_comunes = gastos_comunes

    def establecer_cochera(self, cochera: bool):
        if not isinstance(cochera, bool):
            raise TypeError("Cochera tiene que ser un booleano")

        self.__cochera = cochera

    def obtener_gastos_comunes(self) -> float | int:
        return self.__gastos_comunes
    
    def obtener_cochera(self) -> bool:
        return self.__cochera

    def costo_alquiler(self, base: int) -> float | int:
        if not isinstance(base, int):
            raise TypeError("Base tiene que ser un entero")
        if base <= 0:
            raise ValueError("Base tiene que ser un numero valido")

        if self.__cochera:
            return base + (100 * self._metros_cuadrados) + 2000
        else:
            return base + (100 * self._metros_cuadrados)

    def precio_venta(self, m2: int) -> float | int:
        if not isinstance(m2, int):
            raise TypeError("Metros cuadrados tiene que ser un entero")
        if m2 <= 0:
            raise ValueError("Metros cuadrados tiene que ser un numero valido")

        return self._metros_cuadrados * m2