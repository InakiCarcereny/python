from inmueble import Inmueble

class Inmobiliaria:
    def __init__(self):
        self.__propiedades: list[Inmueble] = []

    def insertar(self, inmueble: 'Inmueble'):
        if isinstance(inmueble, list):
            for inmueble in self.__propiedades:
                if isinstance(inmueble, 'Inmueble'):
                    if inmueble not in self.__propiedades:
                        self.__propiedades.append(inmueble)
                    else:
                      raise ValueError("Alguna de esas propiedades ya se encuentra en la lista de propiedades")
        elif isinstance(inmueble, 'Inmueble'):
            if inmueble not in self.__propiedades:
                self.__propiedades.append(inmueble)
            else:
                raise ValueError("Esa propiedad ya se encuentra en la lista de propiedades")
        else:
            raise TypeError("Inmueble NO es una instancia de lista ni de Inmueble")
        
    def eliminar(self, inmueble: 'Inmueble'):
        if not isinstance(inmueble, Inmueble):
            raise TypeError("Inmueble tiene que ser una instancia de Inmueble")
        
        if inmueble in self.__propiedades:
            self.__propiedades.remove(inmueble)
        else:
            raise ValueError("Ese inmueble NO se encuentra en la lista de inmuebles")
        
    def obtener_inmuebles(self) -> list[Inmueble]:
        return self.__propiedades
    
    def esta_inmueble_codigo(self, codigo: int) -> bool:
        if not isinstance(codigo, int):
            raise TypeError("Codigo tiene que ser un numero entero")
        if codigo <= 0:
            raise ValueError("Codigo tiene que ser un numero valido")

        for propiedad in self.__propiedades:
            if propiedad.obtener_codigo() == codigo:
                return True

        return False

    def esta_inmueble(self, inmueble: 'Inmueble') -> bool:
        if not isinstance(inmueble, Inmueble):
            raise TypeError("Inmueble tiene que ser una instancia de Inmueble")
        
        if inmueble in self.__propiedades:
            return True
        else:
            return False

    def es_igual(self, inmueble: 'Inmueble') -> bool:
        if not isinstance(inmueble, Inmueble):
            raise TypeError("Inmueble tiene que ser una instancia de Inmueble")

        return self == inmueble

    def hay_inmuebles(self) -> bool:
        if len(self.__propiedades) > 0:
            return True
        else:
            return False

    def contar_propiedades_mas_metros(self, metros: int) -> int:
        if not isinstance(metros, int):
            raise TypeError("Metros tiene que ser un entero")

        contador = 0
        
        for propiedad in self.__propiedades:
            if propiedad.obtener_metros_cuadrados() < metros:
                contador += 1

        return contador

    def mayor_precio_venta(self) -> Inmueble:
        self.__propiedades.sort(key= lambda p: p.precio_venta(0))
        
        return self.__propiedades[len(self.__propiedades) - 1]
        