from inmueble import Inmueble

class Quinta(Inmueble):
    def __init__(self, codigo: int, domicilio: str, metros_cuadrados: int, estado: int, metros_parque: int):
        super().__init__(codigo, domicilio, metros_cuadrados, estado)
        if not isinstance(metros_parque, int):
            raise TypeError("Metros parque tiene que ser un entero")
        if metros_parque <= 0:
            raise ValueError("Metros parque tiene que ser un numero valido")

        self.__metros_parque = metros_parque

    def establecer_metros_parque(self, metros_parque: int):
        if not isinstance(metros_parque, int):
            raise TypeError("Metros parque tiene que ser un entero o decimal")
        if metros_parque <= 0:
            raise ValueError("Metros parque tiene que ser un numero valido")

        self.__metros_parque = metros_parque

    def obtener_metros_parque(self) -> int:
        return self.__metros_parque

    def costo_alquiler(self, base: int) -> float | int:
        if not isinstance(base, int):
            raise TypeError("Base tiene que ser un entero")
        if base <= 0:
            raise ValueError("Base tiene que ser un numero valido")

        contador = 0
        sobrante = 0

        while self.__metros_parque > 0:
            if self.__metros_parque >= 15:
                self.__metros_parque -= 15
                contador += 1
            else:
                sobrante = self.__metros_parque
                self.__metros_parque = 0
        
        return base + (100 * self.__metros_parque) + (500 * contador) + (100 * sobrante)

    def precio_venta(self, m2: int) -> float | int:
        if not isinstance(m2, int):
            raise TypeError("Metros cuadrados tiene que ser un entero")
        if m2 <= 0:
            raise ValueError("Metros cuadrados tiene que ser un numero valido")

        return (self.__metros_parque * m2) / 2 