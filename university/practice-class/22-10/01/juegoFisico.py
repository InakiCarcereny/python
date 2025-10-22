from juego import Juego

class JuegoFisico(Juego):
    def __init__(self, id: int, precio: float | int, nombre: str, genero: str, anio: int, descripcion: str, multijugador: bool, stock: int):
        super().__init__(id, precio, nombre, genero, anio, descripcion, multijugador)
        if not isinstance(stock, int):
            raise TypeError("Stock tiene que ser un numero entero")
        if stock <= 0:
            raise ValueError("Stock tiene que ser un numero valido")
        
        self.__stock = stock

    def agregar_stock(self, cantidad: int):
        if not isinstance(cantidad, int):
            raise TypeError("Cantidad tiene que ser un numero entero")
        if cantidad <= 0:
            raise ValueError("Cantidad tiene que ser un numero valido")
        
        self.__stock += cantidad

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
        
    def obtener_stock(self) -> int:
        return self.__stock