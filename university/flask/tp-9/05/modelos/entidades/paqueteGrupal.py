from datetime import date
from modelos.entidades.ciudad import Ciudad
from modelos.entidades.hotel import Hotel
from modelos.entidades.tipoViaje import TipoViaje
from modelos.entidades.transporte import Transporte

class PaqueteGrupal:
    __ULTIMO_ID = 0

    @classmethod
    def obtener_nuevo_ID(cls) -> int:
        cls.__ULTIMO_ID += 1

        return cls.__ULTIMO_ID
    
    @classmethod
    def establecer_ultimo_ID(cls, id: int):
        if not isinstance(id, int):
            raise TypeError("Id tiene que ser un numero entero")
        if id < 0:
            raise ValueError("Id tiene que ser positivo")

        cls.__ULTIMO_ID = id

    @classmethod
    def from_diccionario(cls, data: dict) -> 'PaqueteGrupal':
        if not isinstance(data, dict):
            raise TypeError("Data tiene que ser un diccionario")
        
        claves = [
            'fecha_salida',
            'fecha_vuelta',
            'descripcion',
            'tipo',
            'transporte',
            'precio',
            'ciudad',
            'hotel',
            'cupo_maximo',
            'cupo_actual'
        ]

        for c in claves:
            if c not in data:
                raise ValueError(f"Falta la clave: {c}")
            
        return cls(
            id = data.get('id', None),
            fecha_salida = data['fecha_salida'],
            fecha_vuelta = data['fecha_vuelta'],
            descripcion = data['descripcion'],
            tipo = data['tipo'],
            transporte = data['transporte'],
            precio = data['precio'],
            ciudad = Ciudad.from_diccionario(data['ciudad']),
            hotel = Hotel.from_diccionario(data['hotel']),
            cupo_maximo = data['cupo_maximo'],
            cupo_actual = data['cupo_actual']
        )
    
    def __init__(self, id: int | None, fecha_salida: date, fecha_vuelta: date, descripcion: str, tipo: TipoViaje, transporte: Transporte, precio: int | float, ciudad: Ciudad, hotel: Hotel, cupo_maximo: int, cupo_actual: int):
        if id is None:
            id = PaqueteGrupal.obtener_nuevo_ID()

        if not isinstance(fecha_salida, date):
            raise TypeError("Fecha salida tiene que ser de tipo date")
        
        if not isinstance(fecha_vuelta, date):
            raise TypeError("Fecha vuelta tiene que ser de tipo date")
        
        if not isinstance(descripcion, str):
            raise TypeError("Descripcion tiene que ser una cadena de texto")
        if descripcion == "" or descripcion.isspace():
            raise ValueError("Descripcion no puede estar vacio")
        
        if isinstance(tipo, TipoViaje):
            try:
                tipo = TipoViaje(tipo)
            except ValueError:
                raise ValueError("Tipo viaje inválido")
        
        if isinstance(transporte, Transporte):
            try:
                transporte = Transporte(transporte)
            except ValueError:
                raise ValueError("Transporte inválido")
        
        if not isinstance(precio, (int, float)):
            raise TypeError("Precio tiene que ser un numero entero o con decimales")
        if precio < 0:
            raise ValueError("Precio tiene que ser positivo")
        
        if not isinstance(ciudad, Ciudad):
            raise TypeError("Ciudad tiene que ser una instancia de Ciudad")
        
        if not isinstance(hotel, Hotel):
            raise TypeError("Hotel tiene que ser una instancia de Hotel")
        
        if not isinstance(cupo_maximo, int):
            raise TypeError("Cupo maximo tiene que ser un numero entero")
        if cupo_maximo < 0:
            raise ValueError("Cupo maximo tiene que ser positivo")
        
        if not isinstance(cupo_actual, int):
            raise TypeError("Cupo actual tiene que ser un numero entero")
        if cupo_actual < 0:
            raise ValueError("Cupo actual tiene que ser positivo")
        
        self.__id = id
        self.__fecha_salida = fecha_salida
        self.__fecha_vuelta = fecha_vuelta
        self.__descripcion = descripcion
        self.__tipo = tipo
        self.__transporte = transporte
        self.__precio = precio
        self.__ciudad = ciudad
        self.__hotel = hotel
        self.__cupo_maximo = cupo_maximo
        self.__cupo_actual = cupo_actual

    def obtener_id(self) -> int:
        return self.__id
    
    def obtener_fecha_salida(self) -> date:
        return self.__fecha_salida
    
    def obtener_fecha_vuelta(self) -> date:
        return self.__fecha_vuelta
    
    def obtener_descripcion(self) -> str:
        return self.__descripcion
    
    def obtener_tipo(self) -> TipoViaje:
        return self.__tipo
    
    def obtener_transporte(self) -> Transporte:
        return self.__transporte
    
    def obtener_precio(self) -> int | float:
        return self.__precio
    
    def obtener_ciudad(self) -> Ciudad:
        return self.__ciudad
    
    def obtener_hotel(self) -> Hotel:
        return self.__hotel
    
    def obtener_cupo_maximo(self) -> int:
        return self.__cupo_maximo
    
    def obtener_cupo_actual(self) -> int:
        return self.__cupo_actual
    
    def establecer_fecha_salida(self, fecha_salida: date):
        if not isinstance(fecha_salida, date):
            raise TypeError("Fecha salida tiene que ser de tipo date")
        
        self.__fecha_salida = fecha_salida

    def establecer_fecha_vuelta(self, fecha_vuelta: date):
        if not isinstance(fecha_vuelta, date):
            raise TypeError("Fecha vuelta tiene que ser de tipo date")
        
        self.__fecha_vuelta = fecha_vuelta

    def establecer_descripcion(self, descripcion: str):
        if not isinstance(descripcion, str):
            raise TypeError("Descripcion tiene que ser una cadena de texto")
        if descripcion == "" or descripcion.isspace():
            raise ValueError("Descripcion no puede estar vacio")
        
        self.__descripcion = descripcion

    def establecer_tipo(self, tipo: TipoViaje):
        if not isinstance(tipo, TipoViaje):
            raise TypeError("Tipo viaje tiene que ser una instancia de TipoViaje")
        
        self.__tipo = tipo

    def establecer_transporte(self, transporte: Transporte):
        if not isinstance(transporte, Transporte):
            raise TypeError("Transporte tiene que ser una instancia de Transporte")
        
        self.__transporte = transporte

    def establecer_precio(self, precio: int | float):
        if not isinstance(precio, (int, float)):
            raise TypeError("Precio tiene que ser un numero entero o con decimales")
        if precio < 0:
            raise ValueError("Precio tiene que ser positivo")
        
        self.__precio = precio

    def establecer_ciudad(self, ciudad: Ciudad):
        if not isinstance(ciudad, Ciudad):
            raise TypeError("Ciudad tiene que ser una instancia de Ciudad")
        
        self.__ciudad = ciudad

    def establecer_hotel(self, hotel: Hotel):
        if not isinstance(hotel, Hotel):
            raise TypeError("Hotel tiene que ser una instancia de Hotel")
        
        self.__hotel = hotel

    def establecer_cupo_maximo(self, cupo_maximo: int):
        if not isinstance(cupo_maximo, int):
            raise TypeError("Cupo maximo tiene que ser un numero entero")
        if cupo_maximo < 0:
            raise ValueError("Cupo maximo tiene que ser positivo")
        
        self.__cupo_actual = cupo_maximo

    def establecer_cupo_actual(self, cupo_actual: int):
        if not isinstance(cupo_actual, int):
            raise TypeError("Cupo actual tiene que ser un numero entero")
        if cupo_actual < 0:
            raise ValueError("Cupo actual tiene que ser positivo")
        
        self.__cupo_actual = cupo_actual

    def capacidad_disponible(self) -> int:
        return self.__cupo_maximo - self.__cupo_actual
    
    def inscribir_pasajeros(self, cantidad: int):
        if self.capacidad_disponible() >= cantidad:
            self.__cupo_actual += cantidad

    def es_igual(self, paquete_grupal: 'PaqueteGrupal') -> bool:
        if self.__fecha_salida == paquete_grupal.obtener_fecha_salida() and self.__fecha_vuelta == paquete_grupal.obtener_fecha_vuelta() and self.__descripcion == paquete_grupal.obtener_descripcion() and self.__tipo == paquete_grupal.obtener_tipo() and self.__transporte == paquete_grupal.obtener_transporte() and self.__precio == paquete_grupal.obtener_precio() and self.__ciudad.es_igual(paquete_grupal.obtener_ciudad()) and self.__hotel.es_igual(paquete_grupal.obtener_hotel()) and self.__cupo_maximo == paquete_grupal.obtener_cupo_maximo() and self.__cupo_actual == paquete_grupal.obtener_cupo_actual():
            return True
        
        return False
    
    def to_diccionario(self) -> dict:
        return {
            'id': self.__id,
            'fecha_salida': self.__fecha_salida,
            'fecha_vuelta': self.__fecha_vuelta,
            'descripcion': self.__descripcion,
            'tipo': self.__tipo.value,
            'transporte': self.__transporte.value,
            'precio': self.__precio,
            'ciudad': self.__ciudad.to_diccionario(),
            'hotel': self.__hotel.to_diccionario(),
            'cupo_maximo': self.__cupo_maximo,
            'cupo_actual': self.__cupo_actual
        }
    
    def __str__(self) -> str:
        return (
            f"id: {self.__id} \n"
            f"fecha_salida: {self.__fecha_salida} \n"
            f"fecha_vuelta: {self.__fecha_vuelta} \n"
            f"descripcion: {self.__descripcion} \n"
            f"tipo: {self.__tipo} \n"
            f"transporte: {self.__transporte} \n"
            f"precio: {self.__precio} \n"
            f"ciudad: {self.__ciudad} \n"
            f"hotel: {self.__hotel} \n"
            f"cupo_maximo: {self.__cupo_maximo} \n"
            f"cupo_actual: {self.__cupo_actual} \n" 
        )