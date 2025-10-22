from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, dni: int, nombre: str, apellido: str, anio_ingreso: int):
        if not isinstance(dni, int):
            raise TypeError("Dni tiene que ser un entero")
        if dni <= 0:
            raise ValueError("Dni tiene que ser un numero valido")
        
        if not isinstance(nombre, str):
            raise ValueError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre tiene que tener un valor")
        
        if not isinstance(apellido, str):
            raise ValueError("Apellido tiene que ser un string")
        if apellido == "" or apellido.isspace():
            raise ValueError("Apellido tiene que tener un valor")
        
        if not isinstance(anio_ingreso, int):
            raise TypeError("Anio ingreso tiene que ser un entero")
        if anio_ingreso <= 0:
            raise ValueError("Anio ingreso tiene que ser un anio valido")
        
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._anio_ingreso = anio_ingreso

    def obtener_dni(self) -> int:
        return self._dni
    
    def obtener_nombre(self) -> str:
        return self._nombre
    
    def obtener_apellido(self) -> str:
        return self._apellido
    
    def obtener_anio_ingreso(self) -> int:
        return self._anio_ingreso
    
    def nombre_completo(self) -> str:
        return f"{self._nombre} {self._apellido}"
    
    def antiguedad_en_anios(self, anio_actual: int) -> int:
        if not isinstance(anio_actual, int):
            raise TypeError("Anio actual tiene que ser un entero")
        if anio_actual <= 0:
            raise ValueError("Anio actual tiene que ser un anio valido")
        
        return anio_actual - self._anio_ingreso
    
    @abstractmethod
    def obtener_salario(self) -> float | int:
        pass
    
    def __str__(self) -> str:
        return (
            f"Dni: {self._dni} \n"
            f"Nombre: {self._nombre} \n"
            f"Apellido: {self._apellido} \n"
            f"Anio ingreso: {self._anio_ingreso}"
        )