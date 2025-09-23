class Automovil:
  def __init__(self, marca: str, modelo: str, anio: int, velocidad_maxima: float, velocidad_actual: float):
    self.__marca = marca
    self.__modelo = modelo
    self.__anio = anio
    self.__velocidad_maxima = velocidad_maxima
    self.__velocidad_actual = velocidad_actual

  def establecer_marca(self, marca: str):
    if not isinstance(marca, str):
      raise TypeError("La marca tiene que ser un string")
    if marca == "" or marca.isspace():
      raise ValueError ("El texto esta vacio")
    
    self.__marca = marca
  
  def establecer_modelo(self, modelo: str):
    if not isinstance(modelo, str):
      raise TypeError("El modelo tiene que ser un string")
    if modelo == "" or modelo.isspace():
      raise ValueError ("El texto esta vacio")
    
    self.__modelo = modelo
  
  def establecer_anio(self, anio: int):
    if not isinstance(anio, int):
      raise TypeError("El anio tiene que ser un numero")
    if anio <= 0:
      raise ValueError("El anio tiene que ser positivo")
    
    self.__anio = anio
  
  def establecer_velocidad_maxima(self, velocidad_max: float):
    if not isinstance(velocidad_max, float):
      raise TypeError("La velocidad_max tiene que ser un numero")
    if velocidad_max <= 0:
      raise ValueError("La velocidad_max tiene que ser positivo")
    
    self.__velocidad_maxima = velocidad_max
  
  def establecer_velocidad_actual(self, velocidad_act: float):
    if not isinstance(velocidad_act, float):
      raise TypeError("La velocidad_act tiene que ser un numero")
    if velocidad_act <= 0:
      raise ValueError("La velocidad_act tiene que ser positivo")
    
    self.__velocidad_actual = velocidad_act
  
  def acelerar(self, incremento_vel: int):
    if not isinstance(incremento_vel, int):
      raise TypeError("El incremento_vel tiene que ser un numero")
    if incremento_vel <= 0:
      raise ValueError("El incremento_vel tiene que ser positivo")
    
    nueva_velocidad = self.__velocidad_actual + incremento_vel

    if nueva_velocidad <= self.__velocidad_maxima:
      self.__velocidad_actual = nueva_velocidad
    else:
      self.__velocidad_actual = self.__velocidad_maxima

  
  def desacelerar(self, decremento_vel: int):
    if not isinstance(decremento_vel, int):
      raise TypeError("El decremento_vel tiene que ser un numero")
    if decremento_vel <= 0:
      raise ValueError("El decremento_vel tiene que ser positivo")

    nueva_velocidad = self.__velocidad_actual - decremento_vel

    if nueva_velocidad >= 0:
      self.__velocidad_actual = nueva_velocidad
    else:
      self.__velocidad_actual = 0
  
  def frenar_completo(self):
    self.__velocidad_actual = 0
  
  def obtener_marca(self):
    return self.__marca
  
  def obtener_modelo(self):
    return self.__modelo
  
  def obtener_anio(self):
    return self.__anio
  
  def obtener_velocidad_maxima(self):
    return self.__velocidad_maxima
  
  def obtener_velocidad_actual(self):
    return self.__velocidad_actual
  
  def calcular_minutos_para_llegar(self, distanciaKM: int) -> int:
    if not isinstance(distanciaKM, int):
      raise TypeError("La distanciaKM tiene que ser un numero")
    if distanciaKM <= 0:
      raise ValueError("La distanciaKM tiene que ser positivo")

    velocidad = self.__velocidad_actual
    calculo = (velocidad / distanciaKM) * 60
    
    return calculo