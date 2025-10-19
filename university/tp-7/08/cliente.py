from cuenta import Cuenta

class Cliente():
    def __init__(self, nombre: str, apellido: str, edad: int):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")
        
        if not isinstance(apellido, str):
            raise TypeError("Apellido tiene que ser un texto")
        if apellido == "" or apellido.isspace():
            raise ValueError("Apellido no puede estar vacio")
        
        if not isinstance(edad, int):
            raise TypeError("Edad tiene que ser un entero")
        if edad < 0:
            raise ValueError("Edad tiene que ser un numero positivo")
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__cuenta: Cuenta | None = None

    def establecer_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")

        self.__nombre = nombre

    def establecer_apellido(self, apellido: str):
        if not isinstance(apellido, str):
            raise TypeError("Apellido tiene que ser un texto")
        if apellido == "" or apellido.isspace():
            raise ValueError("Apellido no puede estar vacio")

        self.__apellido = apellido

    def establecer_edad(self, edad: int):
        if not isinstance(edad, int):
            raise TypeError("Edad tiene que ser un entero")
        if edad < 0:
            raise ValueError("Edad tiene que ser un numero positivo")

        self.__edad = edad

    def establecer_cuenta(self, cuenta: 'Cuenta'):
        if not isinstance(cuenta, Cuenta):
            raise TypeError("Cuenta tiene que ser una instancia de Cuenta")

        self.__cuenta = cuenta

    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_apellido(self) -> str:
        return self.__apellido
    
    def obtener_edad(self) -> int:
        return self.__edad
    
    def obtener_cuenta(self) -> Cuenta | None:
        return self.__cuenta
    
    def __str__(self) -> str:
        return (
            f"Nombre: {self.__nombre} \n"
            f"Apellido: {self.__apellido} \n"
            f"Edad: {self.__edad} \n"
            f"Cuenta: {self.__cuenta}"
        )