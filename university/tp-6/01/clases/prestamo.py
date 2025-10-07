from libro import Libro
from fecha import Fecha
from socio import Socio

class Prestamo:
    def __init__(self, libro: Libro, socio: Socio, fecha_prestamo: Fecha, cant_dias: int):
        if not isinstance(libro, Libro):
            raise TypeError("libro debe ser una instancia de Libro")
        if not isinstance(socio, Socio):
            raise TypeError("socio debe ser una instancia de Socio")
        if not isinstance(fecha_prestamo, Fecha):
            raise TypeError("fecha_prestamo debe ser una instancia de Fecha")
        if not isinstance(cant_dias, int) or cant_dias <= 0:
            raise ValueError("cant_dias debe ser un número entero positivo")

        self.__libro = libro
        self.__socio = socio
        self.__fecha_prestamo = fecha_prestamo
        self.__cant_dias = cant_dias
        self.__fecha_devolucion = None

    """COMANDOS"""

    def establecer_fecha_devolucion(self, fecha_dev: Fecha):
        if not isinstance(fecha_dev, Fecha):
            raise TypeError("fecha_dev debe ser una instancia de Fecha")

        self.__fecha_devolucion = fecha_dev

        fecha_limite = self.__fecha_prestamo.suma_dias(self.__cant_dias)

        if fecha_limite.es_anterior(fecha_dev):
            fecha_penalizacion = self.penalizacion()
            self.__socio.establecer_fecha_penalizacion(fecha_penalizacion)

    """CONSULTAS"""

    def obtener_libro(self) -> Libro:
        return self.__libro

    def obtener_fecha_prestamo(self) -> Fecha:
        return self.__fecha_prestamo

    def obtener_fecha_devolucion(self) -> Fecha | None:
        return self.__fecha_devolucion

    def esta_atrasado(self, fecha_actual: Fecha) -> bool:
        if not isinstance(fecha_actual, Fecha):
            raise TypeError("fecha_actual debe ser una instancia de Fecha")

        fecha_limite = self.__fecha_prestamo.suma_dias(self.__cant_dias)
        return self.__fecha_devolucion is None and fecha_limite.es_anterior(fecha_actual)

    def penalizacion(self) -> Fecha:
        if self.__fecha_devolucion is None:
            raise ValueError("El libro aún no fue devuelto")

        fecha_limite = self.__fecha_prestamo.suma_dias(self.__cant_dias)
        dias_atraso = self.__dias_diferencia(fecha_limite, self.__fecha_devolucion)

        if dias_atraso < 7:
            dias_penalizacion = 3
        elif dias_atraso < 21:
            dias_penalizacion = 5
        else:
            dias_penalizacion = 10

        if self.__libro.obtener_categoria() == "A":
            dias_penalizacion *= 2

        return self.__fecha_devolucion.suma_dias(dias_penalizacion)

    def __dias_diferencia(self, f1: Fecha, f2: Fecha) -> int:
        dias = 0
        fecha_temp = f1
        while fecha_temp.es_anterior(f2):
            fecha_temp = fecha_temp.dia_siguiente()
            dias += 1
        return dias

    def __str__(self):
        return (f"Préstamo de '{self.__libro.obtener_nombre()}' a {self.__socio.obtener_nombre()} "
                f"el {self.__fecha_prestamo.obtener_dia()}/{self.__fecha_prestamo.obtener_mes()}/{self.__fecha_prestamo.obtener_anio()} "
                f"por {self.__cant_dias} días")

