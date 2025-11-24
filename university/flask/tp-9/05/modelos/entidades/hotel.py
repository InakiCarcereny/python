from modelos.entidades.pension import Pension
from modelos.entidades.ciudad import Ciudad

class Hotel:
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
    def from_diccionario(cls, data: dict) -> 'Hotel':
        if not isinstance(data, dict):
            raise TypeError("Data tiene que ser un diccionario")
        
        claves = [
            'nombre',
            'estrellas',
            'descripcion',
            'pension',
            'ciudad'
        ]

        for c in claves:
            if c not in data:
                raise ValueError(f"Falta la clave: {c}")

        return cls(
            id = data.get('id', None),
            nombre = data['nombre'],
            estrellas = data['estrellas'],
            descripcion = data['descripcion'],
            pension = data['pension'],
            ciudad = Ciudad.from_diccionario(data['ciudad'])
        )
    
    def __init__(self, id: int | None, nombre: str, estrellas: int, descripcion: str, pension: Pension, ciudad: Ciudad):
        if id is None:
            id = Hotel.obtener_nuevo_ID()

        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser una cadena de texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")
        
        if not isinstance(estrellas, int):
            raise TypeError("Estrellas tiene que ser un numero entero")
        if estrellas < 0:
            raise ValueError("Estrellas tiene que ser positivo")
        
        if not isinstance(descripcion, str):
            raise TypeError("Descripcion tiene que ser una cadena de texto")
        if descripcion == "" or descripcion.isspace():
            raise ValueError("Descripcion no puede estar vacio")

        if isinstance(pension, str):
            try:
                pension = Pension(pension)
            except ValueError:
                raise ValueError("Pension inválida")
        
        if not isinstance(ciudad, Ciudad):
            raise TypeError("Ciudad tiene que ser una instancia de Ciudad")
        
        self.__id = id
        self.__nombre = nombre
        self.__estrellas = estrellas
        self.__descripcion = descripcion
        self.__pension = pension
        self.__ciudad = ciudad

    def obtener_id(self) -> int:
        return self.__id
    
    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_estrellas(self) -> int:
        return self.__estrellas
    
    def obtener_descripcion(self) -> str:
        return self.__descripcion
    
    def obtener_pension(self) -> Pension:
        return self.__pension
    
    def obtener_ciudad(self) -> Ciudad:
        return self.__ciudad
    
    def establecer_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser una cadena de texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")

        self.__nombre = nombre

    def establecer_estrellas(self, estrellas: int):
        if not isinstance(estrellas, int):
            raise TypeError("Estrellas tiene que ser un numero entero")
        if estrellas < 0:
            raise ValueError("Estrellas tiene que ser positivo")
        
        self.__estrellas = estrellas

    def establecer_descripcion(self, descripcion: str):
        if not isinstance(descripcion, str):
            raise TypeError("Descripcion tiene que ser una cadena de texto")
        if descripcion == "" or descripcion.isspace():
            raise ValueError("Descripcion no puede estar vacio")
        
        self.__descripcion = descripcion

    def establecer_pension(self, pension: Pension):
        if not isinstance(pension, Pension):
            raise TypeError("Pension tiene que ser una instancia de Pension")
        
        self.__pension = pension

    def establecer_ciudad(self, ciudad: Ciudad):
        if not isinstance(ciudad, Ciudad):
            raise TypeError("Ciudad tiene que ser una instancia de Ciudad")
        
        self.__ciudad = ciudad

    def es_igual(self, hotel: 'Hotel') -> bool:
        return self.__nombre == hotel.obtener_nombre() and self.__estrellas == hotel.obtener_estrellas() and self.__descripcion == hotel.obtener_descripcion() and self.__pension == hotel.obtener_pension() and self.__ciudad.es_igual(hotel.obtener_ciudad())
    
    def to_diccionario(self) -> dict:
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'estrellas': self.__estrellas,
            'descripcion': self.__descripcion,
            'pension': self.__pension.value,
            'ciudad': self.__ciudad.to_diccionario()
        }
    
    def __str__(self) -> str:
        return (
            f"id: {self.__id} \n"
            f"nombre: {self.__nombre} \n"
            f"estrellas: {self.__estrellas} \n"
            f"descripcion: {self.__descripcion} \n"
            f"pension: {self.__pension} \n"
            f"ciudad: {self.__ciudad}"
        )