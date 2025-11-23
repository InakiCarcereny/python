class Socio:
    @classmethod
    def from_diccionario(cls, data: dict) -> 'Socio':
        if not isinstance(data, dict):
            raise TypeError("Data tiene que ser un diccionario")
        if not 'DNI' in data or not 'nombre' in data or not 'apellido' in data or not 'mail' in data or not 'fecha_nacimiento' in data:
            raise ValueError("Data tiene que contener las claves DNI, nombre, apellido, mail, fecha_nacimiento")
        
        return cls(
            DNI = data['DNI'],
            nombre = data['nombre'],
            apellido = data['apellido'],
            mail = data['mail'],
            fecha_nacimiento = data['fecha_nacimiento']
        )
    
    def __init__(self, DNI: int, nombre: str, apellido: str, mail: str, fecha_nacimiento: int):
        if not isinstance(DNI, int):
            raise TypeError("DNI tiene que ser un numero entero")
        if DNI < 0:
            raise ValueError("DNI tiene que ser un numero positivo")
        
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser una cadena de texto")
        if nombre == '' or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")
        
        if not isinstance(apellido, str):
            raise TypeError("Apellido tiene que ser una cadena de texto")
        if apellido == '' or apellido.isspace():
            raise ValueError("Apellido no puede estar vacio")
        
        if not isinstance(mail, str):
            raise TypeError("Mail tiene que ser una cadena de texto")
        if mail == '' or mail.isspace():
            raise ValueError("Mail no puede estar vacio")
        
        if not isinstance(fecha_nacimiento, int):
            raise TypeError("Fecha nacimiento tiene que ser un numero entero")
        if fecha_nacimiento < 0 or fecha_nacimiento > 2025:
            raise ValueError("Fecha nacimiento tiene que ser un numero valido")
        
        self.__DNI = DNI
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_DNI(self) -> int:
        return self.__DNI
    
    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_apellido(self) -> str:
        return self.__apellido
    
    def obtener_mail(self) -> str:
        return self.__mail
    
    def obtener_fecha_nacimiento(self) -> int:
        return self.__fecha_nacimiento
    
    def establecer_DNI(self, DNI: int):
        if not isinstance(DNI, int):
            raise TypeError("DNI tiene que ser un numero entero")
        if DNI < 0:
            raise ValueError("DNI tiene que ser un numero positivo")

        self.__DNI = DNI

    def establecer_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser una cadena de texto")
        if nombre == '' or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")
        
        self.__nombre = nombre

    def establecer_apellido(self, apellido: str):
        if not isinstance(apellido, str):
            raise TypeError("Apellido tiene que ser una cadena de texto")
        if apellido == '' or apellido.isspace():
            raise ValueError("Apellido no puede estar vacio")
        
        self.__apellido = apellido

    def establecer_mail(self, mail: str):
        if not isinstance(mail, str):
            raise TypeError("Mail tiene que ser una cadena de texto")
        if mail == '' or mail.isspace():
            raise ValueError("Mail no puede estar vacio")
        
        self.__mail = mail

    def establecer_fecha_nacimiento(self, fecha_nacimiento: int):
        if not isinstance(fecha_nacimiento, int):
            raise TypeError("Fecha nacimiento tiene que ser un numero entero")
        if fecha_nacimiento < 0 or fecha_nacimiento > 2025:
            raise ValueError("Fecha nacimiento tiene que ser un numero valido")
        
        self.__fecha_nacimiento = fecha_nacimiento

    def es_igual(self, otro: 'Socio') -> bool:
        return self == otro
    
    def to_diccionario(self) -> dict:
        return {
            'DNI': self.__DNI,
            'nombre': self.__nombre,
            'apellido': self.__apellido,
            'mail': self.__mail,
            'fecha_nacimiento': self.__fecha_nacimiento
        }
    
    def __str__(self) -> str:
        return (
            f"DNI: {self.__DNI} \n"
            f"nombre: {self.__nombre} \n"
            f"apellido: {self.__apellido} \n"
            f"mail: {self.__mail} \n"
            f"fecha_nacimiento: {self.__fecha_nacimiento} \n"
        )
    
