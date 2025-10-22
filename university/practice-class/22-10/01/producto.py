from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, id: int, precio: float | int):
        if not isinstance(id, int):
            raise TypeError("ID tiene que ser un numero entero")
        if id <= 0:
            raise ValueError("ID tiene que ser un numero valido")
        
        if not isinstance(precio, (float, int)):
            raise TypeError("Precio tiene que ser un numero entero o un numero con decimal")
        if precio <= 0:
            raise ValueError("Precio tiene que ser un numero valido")
        
        self._id = id
        self._precio = precio

    def obtener_id(self) -> int:
        return self._id
    
    def obtener_precio(self) -> float | int:
        return self._precio
    
    @abstractmethod
    def se_puede_vender(self, cantidad: int) -> bool:
        pass
    
    @abstractmethod
    def vender(self, cantidad: int):
        pass
    