from abc import ABC, abstractmethod

class Cuenta(ABC):
    def __init__(self, saldo: float | int, cantidad_extracciones: int, cantidad_deposito: int, tasa_anual: float | int, comision_mensual: float | int):
        if not isinstance(saldo, (float, int)):
            raise TypeError("Saldo tiene que ser un entero o un numero con decima")
        if saldo < 0:
            raise ValueError("Saldo tiene que ser un numero positivo")
        
        if not isinstance(cantidad_extracciones, int):
            raise TypeError("Cantidad de extracciones tiene que ser un numero entero")
        if cantidad_extracciones < 0:
            raise ValueError("Cantidad extracciones tiene que ser un numero positivo")
        
        if not isinstance(cantidad_deposito, int):
            raise TypeError("Cantidad deposito tiene que ser un numero entero")
        if cantidad_deposito < 0:
            raise ValueError("Cantidad deposito tiene que ser un numero positivo")

        if not isinstance(tasa_anual, (float, int)):
            raise TypeError("Tasa anual tiene que ser un entero o un numero con decima")
        if tasa_anual <= 0:
            raise ValueError("Tasa anual tiene que ser un numero valido")
        
        if not isinstance(comision_mensual, (float, int)):
            raise TypeError("Comision mensual tiene que ser un entero o un numero con decima")
        if comision_mensual <= 0:
            raise ValueError("Comision mensual tiene que ser un numero valido")
        
        self._saldo = saldo
        self._cantidad_extracciones = cantidad_extracciones
        self._cantidad_deposito = cantidad_deposito
        self._tasa_anual = tasa_anual
        self._comision_mensual = comision_mensual

    def establecer_saldo(self, saldo: float | int):
        if not isinstance(saldo, (float, int)):
            raise TypeError("Saldo tiene que ser un entero o un numero con decima")
        if saldo < 0:
            raise ValueError("Saldo tiene que ser un numero positivo")

        self._saldo = saldo

    def establecer_cantidad_extracciones(self, cantidad: int):
        if not isinstance(cantidad, int):
            raise TypeError("Cantidad de extracciones tiene que ser un numero entero")
        if cantidad < 0:
            raise ValueError("Cantidad extracciones tiene que ser un numero positivo")
        
        self._cantidad_extracciones = cantidad

    def establecer_cantidad_deposito(self, cantidad: int):
        if not isinstance(cantidad, int):
            raise TypeError("Cantidad deposito tiene que ser un numero entero")
        if cantidad < 0:
            raise ValueError("Cantidad deposito tiene que ser un numero positivo")

        self._cantidad_deposito = cantidad

    def establecer_tasa_anual(self, tasa: float | int):
        if not isinstance(tasa, (float, int)):
            raise TypeError("Tasa anual tiene que ser un entero o un numero con decima")
        if tasa <= 0:
            raise ValueError("Tasa anual tiene que ser un numero valido")
        
        self._tasa_anual = tasa

    def establecer_comision_mensual(self, comision: float | int):
        if not isinstance(comision, (float, int)):
            raise TypeError("Comision mensual tiene que ser un entero o un numero con decima")
        if comision <= 0:
            raise ValueError("Comision mensual tiene que ser un numero valido")
        
        self._comision_mensual = comision

    def obtener_saldo(self) -> float | int:
        return self._saldo
    
    def obtener_cantidad_extracciones(self) -> int:
        return self._cantidad_extracciones
    
    def obtener_cantidad_deposito(self) -> int:
        return self._cantidad_deposito
    
    def obtener_tasa_anual(self) -> float | int:
        return self._tasa_anual
    
    def obtener_comision_mensual(self) -> float | int:
        return self._comision_mensual
    
    @abstractmethod
    def depositar(self, monto: float | int):
        pass
    
    @abstractmethod
    def retirar(self, monto: float | int):
        pass
    
    @abstractmethod
    def extracto(self) -> str:
        pass
    
    def __str__(self) -> str:
        return (
            f"Saldo: {self._saldo} \n"
            f"Cantidad extracciones: {self._cantidad_extracciones} \n"
            f"Cantidad deposito: {self._cantidad_deposito} \n"
            f"Tasa anual: {self._tasa_anual} \n"
            f"Comision mensual: {self._comision_mensual}"
        )
        
