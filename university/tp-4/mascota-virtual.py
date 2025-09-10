class MascotaVirtual:
  __MAX_VALOR = 100
  __MIN_VALOR = 0

  def __init__(self, nombre: str, energia: int = __MAX_VALOR, diversion: int = __MAX_VALOR, higiene: int = __MAX_VALOR, dormido: bool = False, can_actividades_desgaste: int = 3):
    if not isinstance(nombre, str):
      raise TypeError("El nombre tiene que ser un texto")
    if nombre == "" or nombre.isspace():
      raise ValueError ("El texto esta vacio")

    self.__nombre = nombre
    self.__energia = energia
    self.__diversion = diversion
    self.__higiene = higiene
    self.__dormido = dormido
    self.__can_actividades_desgaste = can_actividades_desgaste

  #METODOS

  def comer(self):
    if not self.esta_vivo():
      print(f"{self.__nombre} esta MUERTO :(")

    if self.__dormido:
      print(f"{self.__nombre} NO puede comer, esta dormido")

    if not self.puede_realizar_actividades():
      print(f"{self.__nombre} NO puede reazliar mas actividades hasta que vuelva a dormir, ya realiz las 3 diarias")

    nueva_energia = self.__energia + 20

    if nueva_energia < 100:
      self.__energia = nueva_energia
    else:
      self.__energia = 100

    self.__can_actividades_desgaste -= 1
  
  def beber(self):
    if not self.esta_vivo():
      print(f"{self.__nombre} esta MUERTO :(")

    if self.__dormido:
      print(f"{self.__nombre} NO puede comer, esta dormido")

    if not self.puede_realizar_actividades():
      print(f"{self.__nombre} NO puede reazliar mas actividades hasta que vuelva a dormir, ya realiz las 3 diarias")

    nueva_energia = self.__energia + 10

    if nueva_energia < 100:
      self.__energia = nueva_energia
    else:
      self.__energia = 100

    self.__can_actividades_desgaste -= 1
  
  def dormir(self):
    self.__dormido = True
  
  def despertar(self):
    self.__dormido = False
    self.__can_actividades_desgaste = 3
  
  def jugar(self):
    if not self.esta_vivo():
      print(f"{self.__nombre} esta MUERTO :(")

    if self.__dormido:
      print(f"{self.__nombre} NO puede comer, esta dormido")

    if not self.puede_realizar_actividades():
      print(f"{self.__nombre} NO puede reazliar mas actividades hasta que vuelva a dormir, ya realiz las 3 diarias")

    nueva_diversion = self.__diversion + 40

    if nueva_diversion < 100:
      self.__diversion = nueva_diversion
    else:
      self.__diversion = 100

    self.__energia -= 20

    self.__higiene -= 15
  
  def caminar(self):
    return
  
  def saltar(self):
    return
  
  def baniar(self):
    return
  
  #CONSULTAS
  
  def obtener_nombre(self):
    return self.__nombre
  
  def obtener_energia(self):
    return self.__energia
  
  def obtener_diversion(self):
    return self.__diversion
  
  def obtener_higiene(self):
    return self.__higiene
  
  def esta_dormido(self):
    return self.__dormido
  
  def obtener_humor(self):
    return 
  
  def esta_vivo(self) -> bool:
    if self.__energia != 0:
      return True
    else:
      return False
  
  def puede_realizar_actividades(self) -> bool:
    if self.__can_actividades_desgaste > 0:
      return True
    else:
      return False
    
  def tiene_higiene(self) -> bool:
    if self.__higiene > 0:
      return True
    else:
      return False
    
  def tiene_diversion(self) -> bool:
    if self.__diversion > 0:
      return True
    else:
      return False