from empleado import Empleado

class EmpleadoSalarioFijo(Empleado):
    __PORC_2_A_5: float | int = 0.05
    __PORC_MAS_DE_5: float | int = 0.1
    __ANIO_LIMITE_INFERIOR: int = 2
    __ANIO_LIMITE_SUPERIOR: int = 5

    def __init__(self, dni: int, nombre: str, apellido: str, anio_ingreso: int, sueldo_basico: float | int):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        if not isinstance(sueldo_basico, (float, int)):
            raise TypeError("Sueldo basico tiene que ser un numero entero o un numero decimal")
        if sueldo_basico < 0:
            raise ValueError("Sueldo basico tiene que ser un numero positivo")
        
        self.__sueldo_basico = sueldo_basico

    def obtener_salario(self) -> float | int:
        anio = 2025

        if anio - self._anio_ingreso < EmpleadoSalarioFijo.__ANIO_LIMITE_INFERIOR:
            return self.__sueldo_basico
        elif EmpleadoSalarioFijo.__ANIO_LIMITE_SUPERIOR > anio - self._anio_ingreso > EmpleadoSalarioFijo.__ANIO_LIMITE_INFERIOR:
            return self.__sueldo_basico + self.__sueldo_basico * EmpleadoSalarioFijo.__PORC_2_A_5
        else:
            return self.__sueldo_basico * EmpleadoSalarioFijo.__PORC_MAS_DE_5
        
    def obtener_porcentaje_adicional(self) -> float | int:
        anio = 2025
        
        if anio - self._anio_ingreso < EmpleadoSalarioFijo.__ANIO_LIMITE_INFERIOR:
            return 0
        elif anio - self._anio_ingreso <= EmpleadoSalarioFijo.__ANIO_LIMITE_SUPERIOR:
            return EmpleadoSalarioFijo.__PORC_2_A_5 
        else:
            return EmpleadoSalarioFijo.__PORC_MAS_DE_5
        
    def __str__(self)->str:
        return f"{super().__str__()}\n- Salario básico: {self.__sueldo_basico}\n- Salario a cobrar: {self.obtener_salario()}"