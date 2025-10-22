class Cliente:
    def __init__(self, nombre: str, apellido: str, dni: int, mail: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre NO puede estar vacio")
        
        if not isinstance(apellido, str):
            raise TypeError("Apellido tiene que ser un string")
        if apellido == "" or apellido.isspace():
            raise ValueError("Apellido NO puede estar vacio")
        
        if not isinstance(dni, int):
            raise TypeError("Dni tiene que ser un numero entero")
        
        if not isinstance(mail, str):
            raise TypeError("Mail tiene que ser un string")
        if mail == "" or mail.isspace():
            raise ValueError("Mail NO puede estar vacio")
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__mail = mail

    def establecer_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre NO puede estar vacio")
        
        self.__nombre = nombre

    def establecer_apellido(self, apellido: str):
        if not isinstance(apellido, str):
            raise TypeError("Apellido tiene que ser un string")
        if apellido == "" or apellido.isspace():
            raise ValueError("Apellido NO puede estar vacio")
        
        self.__apellido = apellido

    def establecer_dni(self, dni: int):
        if not isinstance(dni, int):
            raise TypeError("Dni tiene que ser un numero entero")
        
        self.__dni = dni

    def establecer_mail(self, mail: str):
        if not isinstance(mail, str):
            raise TypeError("Mail tiene que ser un string")
        if mail == "" or mail.isspace():
            raise ValueError("Mail NO puede estar vacio")
        
        self.__mail = mail

    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_apellido(self) -> str:
        return self.__apellido
    
    def obtener_dni(self) -> int:
        return self.__dni
    
    def obtener_mail(self) -> str:
        return self.__mail
    
    def __str__(self) -> str:
        return (
            f"Nombre: {self.__nombre} \n"
            f"Apellido: {self.__apellido} \n"
            f"DNI: {self.__dni} \n"
            f"Mail: {self.__mail} \n"
        )