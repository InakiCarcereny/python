class Propietario:
    def __init__(self, nombre: str, dni: int):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre tiene que tener un valor")
        
        if not isinstance(dni, int):
            raise TypeError("Dni tiene que ser un numero entero")
        if dni <= 0:
            raise ValueError("Dni tiene que ser un numero valido")

        self.__nombre = nombre
        self.__dni = dni

    def establecer_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre tiene que tener un valor")

        self.__nombre = nombre

    def establecer_dni(self, dni: int):
        if not isinstance(dni, int):
            raise TypeError("Dni tiene que ser un numero entero")
        if dni <= 0:
            raise ValueError("Dni tiene que ser un numero valido")

        self.__dni = dni

    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_dni(self) -> int:
        return self.__dni
    
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}, DNI: {self.__dni}"