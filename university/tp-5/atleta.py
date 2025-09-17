class Atleta:
  __MAX_VALOR: int = 100
  __MIN_VALOR: int = 0

  def __init__(self, nombre: str, energia: int = __MAX_VALOR, destreza: int = __MIN_VALOR, cantidad_entrenamientos: int = __MIN_VALOR):
    if not isinstance(nombre, str):
      raise TypeError("No es un texto")
    if nombre == "" or nombre.isspace():
      raise ValueError("El nombre esta vacio")

    self.__nombre = nombre
    self.__energia = energia
    self.__destreza = destreza
    self.__cantidad_entrenamientos = cantidad_entrenamientos

  def establecer_nombre(self, nombre: str):
    if not isinstance(nombre, str):
      raise TypeError("No es un texto")
    if nombre == "" or nombre.isspace():
      raise ValueError("El nombre esta vacio")

    self.__nombre = nombre

  def entrenar(self):
    self.__energia -= 5
    self.__cantidad_entrenamientos += 1
  
  def descansar(self):
    self.__energia += 20

  def puede_aumentar_destreza(self) -> bool:
    if self.__cantidad_entrenamientos % 5 == 0:
      self.__destreza += 1
      return True
    
    return False
  
  def obtener_nombre(self) -> str:
    return self.__nombre
  
  def obtener_energia(self) -> int:
    return self.__energia
  
  def obtener_destreza(self) -> int:
    return self.__destreza
  
  def obtener_cantidad_entrenamientos(self) -> int:
    return self.__cantidad_entrenamientos
  
  def misma_destreza_que(self, otroAtleta: 'Atleta') -> bool:
    return self.__destreza == otroAtleta.obtener_destreza()
  
  def mayor_destreza_que(self, otroAtleta: 'Atleta') -> bool:
    return self.__destreza > otroAtleta.obtener_destreza()