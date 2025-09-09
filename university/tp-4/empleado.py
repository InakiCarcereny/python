class Empleado:
  def __init__(self, legajo: int, horas_trabajadas: int = 0, valor_hora: float = 0.0):
    self.__legajo = legajo
    self.__horas_trabajadas = horas_trabajadas
    self.__valor_hora = valor_hora

  def establecer_horas_trabajadas(self, cant_horas: int):
    if not isinstance(cant_horas, int):
      raise TypeError("Cantidad de horas trabajadas debe ser un entero")
    if cant_horas < 0:
      raise ValueError("Cantidad de horas trabajadas no puede ser negativa")
    if cant_horas == 0:
      raise ValueError("Cantidad de horas trabajadas debe ser mayor a 0")
    self.__horas_trabajadas = cant_horas
    
  def establecer_valor_hora(self, valor_hora: float):
    if not isinstance(valor_hora, float):
      raise TypeError("Valor de la hora debe ser un float")
    if valor_hora < 0:
      raise ValueError("Valor de la hora no puede ser negativo")
    if valor_hora == 0:
      raise ValueError("Valor de la hora debe ser mayor a 0")
    self.__valor_hora = valor_hora
    
  def obtener_legajo(self) -> int:
    return self.__legajo
    
  def obtener_horas_trabajadas(self) -> int:
    return self.__horas_trabajadas
    
  def obtener_valor_hora(self) -> float:
    return self.__valor_hora
    
  def obtener_sueldo(self) -> float:
    return self.__horas_trabajadas * self.__valor_hora