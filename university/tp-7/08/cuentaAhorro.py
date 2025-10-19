from cuenta import Cuenta

class CuentaAhorro(Cuenta):
    def __init__(self, saldo: float | int, cantidad_extracciones: int, cantidad_deposito: int, tasa_anual: float | int, comision_mensual: float | int, activa: bool):
        super().__init__(saldo, cantidad_extracciones, cantidad_deposito, tasa_anual, comision_mensual)
        if not isinstance(activa, bool):
            raise TypeError("Activa tiene que ser un booleano")
        
        self.__activa = activa
        
    def esta_activa(self) -> bool:
        if self._saldo > 0:
            return True
        else: 
            return False
        
    def depositar(self, monto: float | int):
        if not isinstance(monto, (float, int)):
            raise TypeError("Monto tiene que ser un entero o un numero con decima")
        if monto < 0:
            raise ValueError("Monto tiene que ser un numero positivo")
        
        if self.esta_activa():
            self._saldo += monto
            self._cantidad_deposito += 1
        else:
            raise ValueError("La cuenta esta inactiva")
        
    def retirar(self, monto: float | int):
        if not isinstance(monto, (float, int)):
            raise TypeError("Monto tiene que ser un entero o un numero con decima")
        if monto < 0:
            raise ValueError("Monto tiene que ser un numero positivo")
        
        if self.esta_activa():
          if self._saldo - monto > 0:
              self._saldo -= monto
              self._cantidad_extracciones += 1
              self.extracto()
        else:
            raise ValueError("La cuenta esta inactiva")
        
    def extracto(self) -> str:
        if self._cantidad_extracciones > 4:
            self._saldo -= 1000
            if self._saldo > 0:
                self.__activa = True
            else:
                self.__activa = False

        return (
                f"{super().__str__()} \n"
                f"Activa: {self.__activa}"
            )