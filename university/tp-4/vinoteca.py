class Vinoteca:
  __CAPACIDAD_MAXIMA: int = 5000

  def __init__(self, cant_jugos: int = __CAPACIDAD_MAXIMA, cant_blancos: int = __CAPACIDAD_MAXIMA, cant_tintos_jovenes: int = __CAPACIDAD_MAXIMA, cant_tintos_aniejados: int = __CAPACIDAD_MAXIMA):
    self.__cant_jugos = cant_jugos
    self.__cant_blancos = cant_blancos
    self.__cant_tintos_jovenes = cant_tintos_jovenes
    self.__cant_tintos_aniejados = cant_tintos_aniejados

  def reponer_jugos(self):
    self.__cant_jugos = Vinoteca.__CAPACIDAD_MAXIMA

  def reponer_vinos_blancos(self):
    self.__cant_blancos = Vinoteca.__CAPACIDAD_MAXIMA

  def reponer_vinos_tinto_joven(self):
    self.__cant_tintos_jovenes = Vinoteca.__CAPACIDAD_MAXIMA

  def reponer_vinos_tinto_aniejados(self):
    self.__cant_tintos_aniejados = Vinoteca.__CAPACIDAD_MAXIMA

  def vender_jugos(self, unidades: int):
    if unidades >= self.__cant_jugos:
      self.__cant_jugos = 0
      return self.__cant_jugos
    
    self.__cant_jugos = self.__cant_jugos - unidades
    return self.__cant_jugos

  def vender_vinos_blancos(self, unidades: int):
    if unidades >= self.__cant_blancos:
      self.__cant_blancos = 0
      return self.__cant_blancos
    
    self.__cant_blancos = self.__cant_blancos - unidades
    return self.__cant_blancos
  
  def vender_vinos_tinto_joven(self, unidades: int):
    if unidades >= self.__cant_tintos_jovenes:
      self.__cant_tintos_jovenes = 0
      return self.__cant_tintos_jovenes
    
    self.__cant_tintos_jovenes = self.__cant_tintos_jovenes - unidades
    return self.__cant_tintos_jovenes
  
  def vender_vinos_tinto_aniejados(self, unidades: int):
    if unidades >= self.__cant_tintos_aniejados:
      self.__cant_tintos_aniejados = 0
      return self.__cant_tintos_aniejados
    
    self.__cant_tintos_aniejados = self.__cant_tintos_aniejados - unidades
    return self.__cant_tintos_aniejados
  
  def obtener_cantidad_jugos(self) -> int:
    return self.__cant_jugos
  
  def obtener_cantidad_blancos(self) -> int:
    return self.__cant_blancos
  
  def obtener_cantidad_tinto_jovenes(self) -> int:
    return self.__cant_tintos_jovenes
  
  def obtener_cantidad_tinto_aniejados(self) -> int:
    return self.__cant_tintos_aniejados