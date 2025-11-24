class Ciudad:
    __ULTIMO_ID: int = 0

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
    def from_diccionario(cls, data: dict) -> 'Ciudad':
        if not isinstance(data, dict):
            raise TypeError("Data tiene que ser un diccionario")
        
        claves = [
            'nombre',
            'provincia',
            'puntos_turisticos'
        ]

        for c in claves:
            if c not in data:
                raise ValueError(f"Falta la clave: {c}")

        return cls(
            id = data.get('id', None),
            nombre = data['nombre'],
            provincia = data['provincia'],
            puntos_turisticos = data['puntos_turisticos']
        )
    
    def __init__(self, id: int | None, nombre: str, provincia: str, puntos_turisticos: str):
        if id is None:
            id = Ciudad.obtener_nuevo_ID()

        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser una cadena de texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")
        
        if not isinstance(provincia, str):
            raise TypeError("Provincia tiene que ser una cadena de texto")
        if provincia == "" or provincia.isspace():
            raise ValueError("Provincia no puede estar vacio")
        
        if not isinstance(puntos_turisticos, str):
            raise TypeError("Puntos turisticos tiene que ser una cadena de texto")
        if puntos_turisticos == "" or puntos_turisticos.isspace():
            raise ValueError("Puntos turisticos no puede estar vacio")
        
        self.__id = id
        self.__nombre = nombre
        self.__provincia = provincia
        self.__puntos_turisticos = puntos_turisticos

    def obtener_id(self) -> int:
        return self.__id
    
    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_provincia(self) -> str:
        return self.__provincia
    
    def obtener_puntos_turisticos(self) -> str:
        return self.__puntos_turisticos
    
    def establecer_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser una cadena de texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")
        
        self.__nombre = nombre

    def establecer_provincia(self, provincia: str):
        if not isinstance(provincia, str):
            raise TypeError("Provincia tiene que ser una cadena de texto")
        if provincia == "" or provincia.isspace():
            raise ValueError("Provincia no puede estar vacio")
        
        self.__provincia = provincia

    def establecer_puntos_turisticos(self, puntos_turisticos: str):
        if not isinstance(puntos_turisticos, str):
            raise TypeError("Puntos turisticos tiene que ser una cadena de texto")
        if puntos_turisticos == "" or puntos_turisticos.isspace():
            raise ValueError("Puntos turisticos no puede estar vacio")
        
        self.__puntos_turisticos = puntos_turisticos

    def es_igual(self, ciudad: 'Ciudad') -> bool:
        return self == ciudad
    
    def to_diccionario(self) -> dict:
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'provincia': self.__provincia,
            'puntos_turisticos': self.__puntos_turisticos
        }
    
    def __str__(self) -> str:
        return (
            f"id: {self.__id} \n"
            f"nombre: {self.__nombre} \n"
            f"provincia: {self.__provincia} \n"
            f"puntos_turisticos: {self.__puntos_turisticos}"
        )
