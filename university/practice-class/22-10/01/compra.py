from datetime import date
from cliente import Cliente
from items import Item

class Compra:
    def __init__(self, fecha: date, forma_pago: str, estado: str, cliente: 'Cliente'):
        if not isinstance(fecha, date):
            raise TypeError("Fecha tiene que ser una instancia de date")
        
        if not isinstance(forma_pago, str):
            raise TypeError("Forma pago tiene que ser un string")
        if forma_pago == "" or forma_pago.isspace():
            raise ValueError("Forma pago NO puede estar vacio")
        
        if not isinstance(estado, str):
            raise TypeError("Estado pago tiene que ser un string")
        if estado == "" or estado.isspace():
            raise ValueError("Estado pago NO puede estar vacio")
        
        if not isinstance(cliente, Cliente):
            raise TypeError("Cliente tiene que ser una instancia de Cliente")
        
        self.__fecha = fecha
        self.__lista_items: list[Item] = []
        self.__forma_pago = forma_pago
        self.__estado = estado
        self.__cliente = cliente

    def obtener_fecha(self) -> date:
        return self.__fecha
    
    def obtener_forma_pago(self) -> str:
        return self.__forma_pago
    
    def obtener_lista_items(self) -> list[Item]:
        return self.__lista_items
    
    def obtener_estado(self) -> str:
        return self.__estado
    
    def obtener_cliente(self) -> Cliente:
        return self.__cliente
    
    def agregar_item(self, item: 'Item'):
        if not isinstance(item, Item):
            raise TypeError("El parámetro item debe ser una instancia de la clase Item.")
        if self.__estado != "En proceso":
            raise ValueError("No se pueden agregar items a una compra que no está en proceso.")
        
        producto = item.obtener_producto()
        cantidad = item.obtener_cantidad()

        if not producto.se_puede_vender(cantidad):
            raise ValueError("No hay suficiente stock para el producto solicitado.")
        self.__lista_items.append(item)

    def calcularTotal(self) -> float:
        total = 0.0

        for item in self.__lista_items:
            producto = item.obtener_producto()
            cantidad = item.obtener_cantidad()
            total += producto.obtener_precio() * cantidad

        return total

    def entregar(self):
        for item in self.__lista_items:
            producto = item.obtener_producto()
            cantidad = item.obtener_cantidad()
            producto.vender(cantidad)

        self.__estado = "Entregado"
         