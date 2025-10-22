from producto import Producto

class Item:
    def __init__(self, producto: 'Producto', cantidad: int):
        if not isinstance(producto, Producto):
            raise TypeError("Producto tiene que ser una instancia de Producto")
        
        if not isinstance(cantidad, int):
            raise TypeError("Cantidad tiene que ser un numero entero")
        if cantidad < 0:
            raise ValueError("Cantidad tiene que ser un numero positivo")
        
        self.__producto = producto
        self.__cantidad = cantidad

    def establecer_producto(self, producto: 'Producto'):
        if not isinstance(producto, Producto):
            raise TypeError("Producto tiene que ser una instancia de Producto")
        
        self.__producto = producto

    def establecer_cantidad(self, cantidad: int):
        if not isinstance(cantidad, int):
            raise TypeError("Cantidad tiene que ser un numero entero")
        if cantidad < 0:
            raise ValueError("Cantidad tiene que ser un numero positivo")
        
        self.__cantidad = cantidad

    def obtener_producto(self) -> Producto:
        return self.__producto
    
    def obtener_cantidad(self) -> int:
        return self.__cantidad