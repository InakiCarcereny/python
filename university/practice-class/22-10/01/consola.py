from producto import Producto

class Consola(Producto):
    def __init__(self, id: int, precio: float | int, marca: str, modelo: str, almacenamiento: float | int, cantidad_joysticks: int, stock: int):
        super().__init__(id, precio)
        if not isinstance(marca, str):
            raise TypeError("Marca tiene que ser un string")
        if marca == "" or marca.isspace():
            raise ValueError("Marca NO puede estar vacio")
        
        if not isinstance(modelo, str):
            raise TypeError("Modelo tiene que ser un string")
        if modelo == "" or modelo.isspace():
            raise ValueError("Modelo NO puede estar vacio")
        
        if not isinstance(almacenamiento, (float, int)):
            raise TypeError("Almacenamiento tiene que ser un numero entero o un numero con decimal")
        if almacenamiento <= 0:
            raise ValueError("Almacenamiento tiene que ser un numero valido")
        
        if not isinstance(cantidad_joysticks, int):
            raise TypeError("Almacenamiento tiene que ser un numero entero")
        if cantidad_joysticks <= 0:
            raise ValueError("Cantidad de joysticks tiene que ser un numero valido")
        
        if not isinstance(stock, int):
            raise TypeError("Stock tiene que ser un numero entero")
        if stock <= 0:
            raise ValueError("Stock tiene que ser un numero valido")
        
        self.__marca = marca
        self.__modelo = modelo
        self.__almacenamiento = almacenamiento
        self.__cantidad_joysticks = cantidad_joysticks
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
        
    def obtener_marca(self) -> str:
        return self.__marca
    
    def obtener_modelo(self) -> str:
        return self.__modelo
    
    def obtener_almacenamiento(self) -> float | int:
        return self.__almacenamiento
    
    def obtener_cantidad_joysticks(self) -> int:
        return self.__cantidad_joysticks
    
    def obtener_stock(self) -> int:
        return self.__stock
        
    def esIgual(self, otra_consola: 'Consola') -> bool:
        if not isinstance(otra_consola, Consola):
            raise TypeError("El parámetro debe ser una instancia de la clase Consola.")
        
        return (self._id == super().obtener_id() and
                self._precio == super().obtener_precio() and
                self.__marca == otra_consola.obtener_marca() and
                self.__modelo == otra_consola.obtener_modelo() and
                self.__almacenamiento == otra_consola.obtener_almacenamiento() and
                self.__cantidad_joysticks == otra_consola.obtener_cantidad_joysticks() and
                self.__stock == otra_consola.obtener_stock())