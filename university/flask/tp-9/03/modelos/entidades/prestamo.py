class Prestamo:
    __ULTIMO_ID = 0

    @classmethod
    def obtener_nuevo_ID(cls) -> int:
        cls.__ULTIMO_ID += 1
        
        return cls.__ULTIMO_ID
    
    @classmethod
    def establecer_ultimo_ID(cls, ultimo_id: int):
        if not isinstance(ultimo_id, int):
            raise TypeError("Ultimo id tiene que ser un numero entero")
        if ultimo_id < 0:
            raise ValueError("Ultimo id tiene que ser positivo")
        
        cls.__ULTIMO_ID = ultimo_id

    @classmethod
    def from_diccionario(cls, data: dict) -> 'Prestamo':
        if not isinstance(data, dict):
            raise TypeError("Data tiene que ser un diccionario")
        if 'socio_dni' not in data or 'libro_isbn' not in data or 'fecha_retiro' not in data or 'cant_dias' not in data:
            raise ValueError("El diccionario debe contener las claves socio_dni, libro_isbn, fecha_retiro, cant_dias")
        
        return cls(
            id = data.get('id', None),
            socio_dni = data['socio_dni'],
            libro_isbn = data['libro_isbn'],
            fecha_retiro = data['fecha_retiro'],
            cant_dias = data['cant_dias'],
            fecha_devolucion = data.get('fecha_devolucion', None)
        )
    
    def __init__(self, id: int | None, socio_dni: int, libro_isbn: int, fecha_retiro: int, cant_dias: int, fecha_devolucion: int | None):
        if id is None:
            id = Prestamo.obtener_nuevo_ID()

        if not isinstance(socio_dni, int):
            raise TypeError("Socio dni tiene que ser un numero entero")
        if socio_dni < 0:
            raise ValueError("Socio dni tiene que ser un numero positivo")
        
        if not isinstance(libro_isbn, int):
            raise TypeError("Libro isbn tiene que ser un numero entero")
        if libro_isbn < 0:
            raise ValueError("Libro isbn tiene que ser un numero positivo")
        
        if not isinstance(fecha_retiro, int):
            raise TypeError("Fecha retiro tiene que ser un numero entero")
        if fecha_retiro < 0:
            raise ValueError("Fecha retiro tiene que ser un numero positivo")
        
        if not isinstance(cant_dias, int):
            raise TypeError("Cantidad dias tiene que ser un numero entero")
        if cant_dias < 0:
            raise ValueError("Cantidad dias tiene que ser un numero positivo")
        
        if fecha_devolucion is not None:
            if not isinstance(fecha_devolucion, int):
                raise TypeError("Fecha devolucion tiene que ser un numero entero")
            if fecha_devolucion < 0:
                raise ValueError("Fecha devolucion tiene que ser positivo")
        
        self.__id = id
        self.__socio_dni = socio_dni
        self.__libro_isbn = libro_isbn
        self.__fecha_retiro = fecha_retiro
        self.__cant_dias = cant_dias
        self.__fecha_devolucion = fecha_devolucion

    def obtener_ID(self) -> int:
        return self.__id
    
    def obtener_socio_dni(self) -> int:
        return self.__socio_dni
    
    def obtener_libro_isbn(self) -> int:
        return self.__libro_isbn
    
    def obtener_fecha_retiro(self) -> int:
        return self.__fecha_retiro
    
    def obtener_cant_dias(self) -> int:
        return self.__cant_dias
    
    def obtener_fecha_devolucion(self) -> int | None:
        return self.__fecha_devolucion
    
    def establecer_ID(self, id: int):
        if not isinstance(id, int):
            raise TypeError("Id tiene que ser un numero entero")
        if id < 0:
            raise ValueError("Id tiene que ser positivo")

        self.__id = id

    def establecer_socio_dni(self, socio_dni: int):
        if not isinstance(socio_dni, int):
            raise TypeError("Socio dni tiene que ser un numero entero")
        if socio_dni < 0:
            raise ValueError("Socio dni tiene que ser un numero positivo")

        self.__socio_dni = socio_dni

    def establecer_libro_isbn(self, libro_isbn: int):
        if not isinstance(libro_isbn, int):
            raise TypeError("Libro isbn tiene que ser un numero entero")
        if libro_isbn < 0:
            raise ValueError("Libro isbn tiene que ser un numero positivo")

        self.__libro_isbn = libro_isbn

    def establecer_fecha_retiro(self, fecha_retiro: int):
        if not isinstance(fecha_retiro, int):
            raise TypeError("Fecha retiro tiene que ser un numero entero")
        if fecha_retiro < 0:
            raise ValueError("Fecha retiro tiene que ser un numero positivo")
        
        self.__fecha_retiro = fecha_retiro

    def establecer_cant_dias(self, cant_dias: int):
        if not isinstance(cant_dias, int):
            raise TypeError("Cantidad dias tiene que ser un numero entero")
        if cant_dias < 0:
            raise ValueError("Cantidad dias tiene que ser un numero positivo")
        
        self.__cant_dias = cant_dias

    def establecer_fecha_devolucion(self, fecha_devolucion: int):
        if not isinstance(fecha_devolucion, int):
            raise TypeError("Fecha devolucion tiene que ser un numero entero")
        if fecha_devolucion < 0:
            raise ValueError("Fecha devolucion tiene que ser un numero positivo")
        
        self.__fecha_devolucion = fecha_devolucion

    def es_igual(self, prestamo: 'Prestamo') -> bool:
        return self == prestamo
    
    def to_diccionario(self) -> dict:
        return {
            'id': self.__id,
            'socio_dni': self.__socio_dni,
            'libro_isbn': self.__libro_isbn,
            'fecha_retiro': self.__fecha_retiro,
            'cant_dias': self.__cant_dias,
            'fecha_devolucion': self.__fecha_devolucion
        }
        
    def __str__(self) -> str:
        return (
            f"id: {self.__id} \n"
            f"socio_dni: {self.__socio_dni} \n"
            f"libro_isbn: {self.__libro_isbn} \n"
            f"fecha_retiro: {self.__fecha_retiro} \n"
            f"cant_dias: {self.__cant_dias} \n"
            f"fecha_devolucion: {self.__fecha_devolucion} \n"
        )
        