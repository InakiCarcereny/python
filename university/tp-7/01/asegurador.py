from polizaInmueble import Poliza_inmueble

class Aseguradora:
    def __init__(self):
        self.__polizas: list[Poliza_inmueble] = []

    def insertar(self, poliza: 'Poliza_inmueble'):
        if not isinstance(poliza, Poliza_inmueble):
            raise TypeError("Poliza tiene que ser una instancia de Poliza")

        if poliza not in self.__polizas:
          self.__polizas.append(poliza)
          self.__polizas.sort(key= lambda p: p._numero)
        else:
            raise ValueError("La poliza ya se encuentra dentro de las polizas")

    def eliminar(self, poliza: 'Poliza_inmueble'):
        if not isinstance(poliza, Poliza_inmueble):
            raise TypeError("Poliza tiene que ser una instancia de Poliza")

        if poliza in self.__polizas:
            self.__polizas.remove(poliza)
        else:
            raise ValueError("La poliza no exite dentro de las polizas")

    def obtener_polizas(self) -> list[Poliza_inmueble]:
        return self.__polizas

    def existe_poliza(self, poliza: 'Poliza_inmueble') -> bool:
        if not isinstance(poliza, Poliza_inmueble):
            raise TypeError("Poliza tiene que ser una instancia de Poliza")

        if poliza in self.__polizas:
            return True
        else:
            return False

    def hay_polizas(self) -> bool:
        if len(self.__polizas) > 0:
            return True
        else:
            return False

    def costo_total(self) -> float | int:
        costo: float | int = 0

        for pol in self.__polizas:
            costo += pol.costo_poliza()
        
        return costo

    def es_igual(self, aseguradora: 'Aseguradora') -> bool:
        if not isinstance(aseguradora, Aseguradora):
            raise TypeError("Aseguradora tiene que ser una instancia de Aseguradora")

        return self == aseguradora
