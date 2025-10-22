from juego import Juego

class JuegoDigital(Juego):
    def __init__(self, id: int, precio: float | int, nombre: str, genero: str, anio: int, descripcion: str, multijugador: bool, plataforma: str, tamanio: float | int, distribuidora: str):
        super().__init__(id, precio, nombre, genero, anio, descripcion, multijugador)
        if not isinstance(plataforma, str):
            raise TypeError("Plataforma tiene que ser un string")
        if plataforma == "" or plataforma.isspace():
            raise ValueError("Plataforma NO puede estar vacio")
        
        if not isinstance(tamanio, (float | int)):
            raise TypeError("Tamanio tiene que ser un numero entero o un numero con decimal")
        if tamanio <= 0:
            raise ValueError("Tamanio tiene que ser un numero valido")
        
        if not isinstance(distribuidora, str):
            raise TypeError("Distribuidora tiene que ser un string")
        if distribuidora == "" or distribuidora.isspace():
            raise ValueError("Distribuidora NO puede estar vacio")
        
        self.__plataforma = plataforma
        self.__tamanio = tamanio
        self.__distribuidora = distribuidora

    def se_puede_vender(self, cantidad: int) -> bool:
        if not isinstance(cantidad, int):
            raise TypeError("Cantidad tiene que ser un numero entero")
        if cantidad <= 0:
            raise ValueError("Cantidad tiene que ser un numero valido")
        
        if self.__stock >= cantidad:
            return True
        
        return False
    
    def vender(self, cantidad: int):
        if not isinstance(cantidad, int):
            raise TypeError("Cantidad tiene que ser un numero entero")
        if cantidad <= 0:
            raise ValueError("Cantidad tiene que ser un numero valido")
        
        if self.se_puede_vender(cantidad):
            self.__stock -= cantidad
        else:
            raise ValueError("La cantidad solicitada es mayor al stock disponible")
        
    def obtener_plataforma(self) -> str:
        return self.__plataforma
    
    def obtener_tamanio(self) -> float | int:
        return self.__tamanio
    
    def obtener_distribuidora(self) -> str:
        return self.__distribuidora