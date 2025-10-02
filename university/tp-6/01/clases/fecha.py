class Fecha:
    def __init__(self, dia: int, mes: int, anio: int):
        if not isinstance(dia, int):
            raise TypeError("Dia tiene que ser un numero")
        if dia < 0 or dia > 31:
            raise ValueError("Dia tiene que ser mayor a 0 y menor a 32")

        if not isinstance(mes, int):
            raise TypeError("Mes tiene que ser un numero")
        if mes < 0 or mes > 12:
            raise ValueError("Mes tiene que ser mayor a 0 y menor a 13")

        if not isinstance(anio, int):
            raise TypeError("Anio tiene que ser un numero")

        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    def establecer_dia(self, dia: int):
        if not isinstance(dia, int):
            raise TypeError("Dia tiene que ser un numero")
        if dia < 0 or dia > 31:
            raise ValueError("Dia tiene que ser mayor a 0 y menor a 32")

        self.__dia = dia

    def establecer_mes(self, mes: int):
        if not isinstance(mes, int):
            raise TypeError("Mes tiene que ser un numero")
        if mes < 0 or mes > 12:
            raise ValueError("Mes tiene que ser mayor a 0 y menor a 13")

        self.__mes = mes

    def establecer_anio(self, anio: int):
        if not isinstance(anio, int):
            raise TypeError("Anio tiene que ser un numero")

        self.__anio = anio

    def obtener_dia(self):
        return self.__dia

    def obtener_mes(self):
        return self.__mes

    def obtener_anio(self):
        return self.__anio

    def es_anterior(self, otra_fecha: 'Fecha') -> bool:
        if not isinstance(otra_fecha.__dia, int):
            raise TypeError("Dia tiene que ser un numero")
        if otra_fecha.__dia < 0 or otra_fecha.__dia > 31:
            raise ValueError("Dia tiene que ser mayor a 0 y menor a 32")

        if not isinstance(otra_fecha.__mes, int):
            raise TypeError("Mes tiene que ser un numero")
        if otra_fecha.__mes < 0 or otra_fecha.__mes > 12:
            raise ValueError("Mes tiene que ser mayor a 0 y menor a 13")

        if not isinstance(otra_fecha.__anio, int):
            raise TypeError("Anio tiene que ser un numero")


        return (self.__anio, self.__mes, self.__dia) < (otra_fecha.__anio, otra_fecha.__mes, otra_fecha.__dia)
 
    def suma_dias(self, cant_dias: int) -> 'Fecha':
        if not isinstance(cant_dias, int):
            raise TypeError("Cantidad de dias tiene que ser un numero")
        if cant_dias <= 0:
            raise ValueError("Cantidad de dias tiene que ser un numero positivo")

        dia = self.__dia
        mes = self.__mes
        anio = self.__anio

        for _ in range(cant_dias):
            dia += 1
            if dia > self.__dias_del_mes(mes):
                dia = 1
                mes += 1
                if mes > 12:
                    mes = 1
                    anio += 1

        return Fecha(dia, mes, anio)

    def dia_siguiente(self) -> 'Fecha':
        dia = self.__dia + 1
        mes = self.__mes
        anio = self.__anio
        if dia > self.__dias_del_mes(mes):
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1

        return Fecha(dia, mes, anio)

    def es_igual_que(self, otra_fecha: 'Fecha') -> bool:
        if not isinstance(otra_fecha.__dia, int):
            raise TypeError("Dia tiene que ser un numero")
        if otra_fecha.__dia < 0 or otra_fecha.__dia > 31:
            raise ValueError("Dia tiene que ser mayor a 0 y menor a 32")

        if not isinstance(otra_fecha.__mes, int):
            raise TypeError("Mes tiene que ser un numero")
        if otra_fecha.__mes < 0 or otra_fecha.__mes > 12:
            raise ValueError("Mes tiene que ser mayor a 0 y menor a 13")

        if not isinstance(otra_fecha.__anio, int):
            raise TypeError("Anio tiene que ser un numero")


        if self.__dia == otra_fecha.__dia and self.__mes == otra_fecha.__mes and self.__anio == otra_fecha.__anio:
            return True
        else:
            return False

    def __es_bisiesto(self, anio: int) -> bool:
        return (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0)

    def __dias_del_mes(self, mes: int) -> int:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            return 31

        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            return 30

        if self.__es_bisiesto(self.__anio):
            return 29
        else:
            return 28


