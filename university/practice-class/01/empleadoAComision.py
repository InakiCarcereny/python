from empleado import Empleado

class EmpleadoAComision(Empleado):
    def __init__(self, dni: int, nombre: str, apellido: str, anio_ingreso: int, salario_minimo: float | int, cant_clientes_captados: int, monto_por_cliente: float | int):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        if not isinstance(salario_minimo, (float, int)):
            raise TypeError("Salario minimo tiene que ser un numero entero o un numero decimal")
        if salario_minimo < 0:
            raise ValueError("Salario minimo tiene que ser un numero positivo")
        
        if not isinstance(cant_clientes_captados, int):
            raise ValueError("Cantidad de clientes captados tiene que ser un numero entero")
        if cant_clientes_captados < 0:
            raise ValueError("Salario minimo tiene que ser un numero positivo")
        
        if not isinstance(monto_por_cliente, (float, int)):
            raise TypeError("Monto por cliente tiene que ser un entero o un numero decimal")
        if monto_por_cliente < 0:
            raise ValueError("Monto por cliente tiene que ser un numero positivo")
        
        self.__salario_minimo = salario_minimo
        self.__cant_clientes_captados = cant_clientes_captados
        self.__monto_por_cliente = monto_por_cliente
        
    def obtener_salario(self) -> float | int:
        salario = self.__cant_clientes_captados * self.__monto_por_cliente

        if salario > self.__salario_minimo:
            return salario
        
        return self.__salario_minimo
    
    def obtener_cant_clientes_captados(self) -> int:
        return self.__cant_clientes_captados
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()} \n"
            f"Salario minimo: {self.__salario_minimo} \n"
            f"Cantidad clientes captados: {self.__cant_clientes_captados} \n"
            f"Monto por cliente: {self.__monto_por_cliente}"
        )
            