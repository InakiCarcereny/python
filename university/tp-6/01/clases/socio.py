from fecha import Fecha

class Socio:
    def __init__(self, nombre: str, fecha_nacimiento: Fecha):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser una cadeta de texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")

        if not isinstance(fecha_nacimiento, Fecha):
            raise TypeError("Fecha de nacimiento tiene que ser una instancia de Fecha")

        self.__nombre = nombre
        self.__fecha_nacimiento = fecha_nacimiento
        self.__fecha_penalizacion = None

    """COMANDOS"""

    def establecer_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser una cadeta de texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")

        self.__nombre = nombre

    def establecer_fecha_nacimiento(self, fecha_nacimiento: Fecha):
        if not isinstance(fecha_nacimiento, Fecha):
            raise TypeError("Fecha de nacimiento tiene que ser una instancia de Fecha")

        self.__fecha_nacimiento = fecha_nacimiento

    def establecer_fecha_penalizacion(self, fecha_penalizacion: Fecha):
        if not isinstance(fecha_penalizacion, Fecha):
            raise TypeError("Fecha de penzalizacion tiene que ser una instancia de Fecha")

        self.__fecha_penalizacion = fecha_penalizacion

    """CONSULTAS"""

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_fecha_nacimiento(self) -> Fecha:
        return self.__fecha_nacimiento

    def obtener_fecha_penalizacion(self) -> Fecha:
        if self.__fecha_penalizacion is None:
            raise ValueError("El socio no tiene fecha de penalizacion")
        else:
            return self.__fecha_penalizacion

    def esta_habilitado(self, fecha: Fecha) -> bool:
        if not isinstance(fecha, Fecha):
            raise TypeError("Fecha tiene que ser una instancia de Fecha")

        return (
            self.__fecha_penalizacion is None
            or self.__fecha_penalizacion.es_anterior(fecha)
            or self.__fecha_penalizacion.es_igual_que(fecha)
        )

    def __str__(self):
        return f"Nombre: {self.__nombre}, Fecha nacimiento: {self.__fecha_nacimiento}, Fecha penalizacion: {self.__fecha_penalizacion}"

