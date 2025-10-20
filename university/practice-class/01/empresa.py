from empleado import Empleado
from empleadoAComision import EmpleadoAComision

class Empresa:
    def __init__(self, nombre: str):
        if not isinstance(nombre, str):
            raise ValueError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre tiene que tener un valor")
        
        self.__nombre = nombre
        self.__empleados: list[Empleado] = []

    def agregar_empleado(self, emp: 'Empleado'):
        if not isinstance(emp, Empleado):
            raise TypeError("Empleado tiene que ser una instancia de Empleado")
        
        if emp not in self.__empleados:
            self.__empleados.append(emp)
        else:
            raise ValueError("Ese empleado ya se encuentra en la lista de empleados")
        
    def mostrar_empleados(self):
        for emp in self.__empleados:
            print(emp)

    def empleado_con_mas_clientes(self) -> Empleado | None:
        empleado_mas_clientes = None
        max_clientes = -1

        for emp in self.__empleados:
            if isinstance(emp, EmpleadoAComision):
                if emp.obtener_cant_clientes_captados() > max_clientes:
                    empleado_mas_clientes = emp
                    max_clientes = emp.obtener_cant_clientes_captados()
        
        return empleado_mas_clientes
    
    def es_igual(self, empresa: 'Empresa') -> bool:
        return self == empresa
        
    
    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_empleados(self) -> list[Empleado]:
        return self.__empleados