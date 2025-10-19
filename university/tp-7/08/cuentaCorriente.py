from cuenta import Cuenta

class CuentaCorriente(Cuenta):
    __LIMITE_DESCUBIERTO = 0

    def __init__(self, saldo: float | int, cantidad_extracciones: int, cantidad_deposito: int, tasa_anual: float | int, comision_mensual: float | int, penalizaciones: int):
        super().__init__(saldo, cantidad_extracciones, cantidad_deposito, tasa_anual, comision_mensual)
        if not isinstance(penalizaciones, int):
            raise TypeError("Penalizaciones tiene que ser un numero entero")
        if penalizaciones < 0:
            raise ValueError("Penalizaciones tiene que ser un numero positivo")

        self.__penalizaciones = penalizaciones
        self.__limite_descubierto = CuentaCorriente.__LIMITE_DESCUBIERTO
    
    def establecer_penalizaciones(self, penalizaciones: int):
        if not isinstance(penalizaciones, int):
            raise TypeError("Penalizaciones tiene que ser un numero entero")
        if penalizaciones < 0:
            raise ValueError("Penalizaciones tiene que ser un numero positivo")

        self.__penalizaciones = penalizaciones

    def establecer_limite_descubierto(self, limite: float | int):
        if not isinstance(limite, (float, int)):
            raise TypeError("Limite descubierto tiene que ser un entero o un numero con decima")
        if limite < 0:
            raise ValueError("Limite descubierto tiene que ser un numero positivo")
        
        self.__limite_descubierto = limite

    def obtener_penalizaciones(self) -> int:
        return self.__penalizaciones
    
    def obtener_limite_descubierto(self) -> float | int:
        return self.__limite_descubierto
    
    def retirar(self, monto: float | int):
        if not isinstance(monto, (float, int)):
            raise TypeError("Monto tiene que ser un entero o un numero con decima")
        if monto < 0:
            raise ValueError("Monto tiene que ser un numero positivo")
        
        if (self._saldo + self.__limite_descubierto) - monto > 0:
            self._saldo -= monto
        else:
            self._saldo -= monto

    def depositar(self, monto: float | int):
        if not isinstance(monto, (float, int)):
            raise TypeError("Monto tiene que ser un entero o un numero con decima")
        if monto < 0:
            raise ValueError("Monto tiene que ser un numero positivo")
        
        if self._saldo < 0:
            penalizacion = abs(self._saldo) * 0.02
            nuevo_monto = monto - penalizacion
            self._saldo += nuevo_monto
            self.__penalizaciones += 1
        else:
            self._saldo += monto

    def extracto(self) -> str:
        return (
            f"{super().__str__()} \n"
            f"Penalizaciones: {self.__penalizaciones}"
        )
        