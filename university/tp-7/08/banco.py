from cliente import Cliente
from cuenta import Cuenta

class Banco:
    def __init__(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")

        self.__nombre = nombre
        self.__clientes: list[Cliente] = []

    def insertar(self, cliente: 'Cliente'):
        if not isinstance(cliente, Cliente):
            raise TypeError("Cliente tiene que ser una instancia de Cliente")
        
        if not cliente in self.__clientes:
            self.__clientes.append(cliente)
        else:
            raise ValueError("Ese cliente ya se encuentra en la lista de clientes")
        
    def eliminar(self, cliente: 'Cliente'):
        if not isinstance(cliente, Cliente):
            raise TypeError("Cliente tiene que ser una instancia de Cliente")
        
        if cliente in self.__clientes:
            self.__clientes.remove(cliente)
        else:
            raise ValueError("Ese cliente no existe en la lista de clientes")
        
    def existe_cliente(self, nombre: str) -> bool:
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")
        
        for cliente in self.__clientes:
            if cliente.obtener_nombre() == nombre:
                return True
            
        return False
            
    def cliente_mas_saldo(self) -> Cliente:
        self.__clientes.sort(key= lambda p: p.obtener_cuenta().obtener_saldo())

        return self.__clientes[len(self.__clientes) - 1]
    
    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_clientes(self) -> list[Cliente]:
        return self.__clientes