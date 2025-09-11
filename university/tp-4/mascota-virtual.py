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
      return(f"{self.__nombre} esta MUERTO :(")

    if self.__dormido:
      return(f"{self.__nombre} NO puede comer, esta dormido")

    if not self.puede_realizar_actividades():
      return(f"{self.__nombre} NO puede reazliar mas actividades hasta que vuelva a dormir, ya realiz las 3 diarias")

    nueva_energia = self.__energia + 20

    if nueva_energia <= MascotaVirtual.__MAX_VALOR:
      self.__energia = nueva_energia
    else:
      self.__energia = MascotaVirtual.__MAX_VALOR
  
  def beber(self):
    if not self.esta_vivo():
      return(f"{self.__nombre} esta MUERTO :(")

    if self.__dormido:
      return(f"{self.__nombre} NO puede beber, esta dormido")

    if not self.puede_realizar_actividades():
      return(f"{self.__nombre} NO puede reazliar mas actividades hasta que vuelva a dormir, ya realiz las 3 diarias")

    nueva_energia = self.__energia + 10

    if nueva_energia <= MascotaVirtual.__MAX_VALOR:
      self.__energia = nueva_energia
    else:
      self.__energia = MascotaVirtual.__MAX_VALOR
  
  def dormir(self):
    self.__dormido = True

    if not self.esta_vivo():
      return(f"{self.__nombre} esta MUERTO :(")

    if not self.puede_realizar_actividades():
      return(f"{self.__nombre} NO puede reazliar mas actividades hasta que vuelva a dormir, ya realiz las 3 diarias")

    nueva_energia = self.__energia + 20
    nueva_diversion = self.__diversion - 10

    if nueva_energia <= MascotaVirtual.__MAX_VALOR:
      self.__energia = nueva_energia
    else:
      self.__energia = MascotaVirtual.__MAX_VALOR

    if nueva_diversion >= MascotaVirtual.__MIN_VALOR:
      self.__diversion = nueva_diversion
    else:
      self.__diversion = MascotaVirtual.__MIN_VALOR

  
  def despertar(self):
    self.__dormido = False
    self.__can_actividades_desgaste = 3
  
  def jugar(self):
    if not self.esta_vivo():
      return(f"{self.__nombre} esta MUERTO :(")

    if self.__dormido:
      return(f"{self.__nombre} NO puede jugar, esta dormido")

    if not self.puede_realizar_actividades():
      return(f"{self.__nombre} NO puede reazliar mas actividades hasta que vuelva a dormir, ya realiz las 3 diarias")

    nueva_diversion = self.__diversion + 40
    nueva_energia = self.__energia - 20
    nueva_higiene = self.__higiene - 15

    if nueva_diversion <= MascotaVirtual.__MAX_VALOR:
      self.__diversion = nueva_diversion
    else:
      self.__diversion = MascotaVirtual.__MAX_VALOR

    if nueva_energia >= MascotaVirtual.__MIN_VALOR:
      self.__energia = nueva_energia
    else:
      self.__energia = MascotaVirtual.__MIN_VALOR

    if nueva_higiene >= MascotaVirtual.__MIN_VALOR:
      self.__higiene = nueva_higiene
    else:
      self.__higiene = MascotaVirtual.__MIN_VALOR

    self.__can_actividades_desgaste -= 1
  
  def caminar(self):
    if not self.esta_vivo():
      return(f"{self.__nombre} esta MUERTO :(")

    if self.__dormido:
      return(f"{self.__nombre} NO puede caminar, esta dormido")

    if not self.puede_realizar_actividades():
      return(f"{self.__nombre} NO puede reazliar mas actividades hasta que vuelva a dormir, ya realiz las 3 diarias")

    nueva_diversion = self.__diversion + 20
    nueva_energia = self.__energia - 10
    nueva_higiene = self.__higiene - 8

    if nueva_diversion <= MascotaVirtual.__MAX_VALOR:
      self.__diversion = nueva_diversion
    else:
      self.__diversion = MascotaVirtual.__MAX_VALOR

    if nueva_energia >= MascotaVirtual.__MIN_VALOR:
      self.__energia = nueva_energia
    else:
      self.__energia = MascotaVirtual.__MIN_VALOR

    if nueva_higiene >= MascotaVirtual.__MIN_VALOR:
      self.__higiene = nueva_higiene
    else:
      self.__higiene = MascotaVirtual.__MIN_VALOR

    self.__can_actividades_desgaste -= 1
  
  def saltar(self):
    if not self.esta_vivo():
      return(f"{self.__nombre} esta MUERTO :(")

    if self.__dormido:
      return(f"{self.__nombre} NO puede saltar, esta dormido")

    if not self.puede_realizar_actividades():
      return(f"{self.__nombre} NO puede reazliar mas actividades hasta que vuelva a dormir, ya realiz las 3 diarias")

    nueva_diversion = self.__diversion + 10
    nueva_energia = self.__energia - 15
    nueva_higiene = self.__higiene - 10

    if nueva_diversion <= MascotaVirtual.__MAX_VALOR:
      self.__diversion = nueva_diversion
    else:
      self.__diversion = MascotaVirtual.__MAX_VALOR

    if nueva_energia >= MascotaVirtual.__MIN_VALOR:
      self.__energia = nueva_energia
    else:
      self.__energia = MascotaVirtual.__MIN_VALOR

    if nueva_higiene >= MascotaVirtual.__MIN_VALOR:
      self.__higiene = nueva_higiene
    else:
      self.__higiene = MascotaVirtual.__MIN_VALOR

    self.__can_actividades_desgaste -= 1
  
  def baniar(self):
    if not self.esta_vivo():
      return(f"{self.__nombre} esta MUERTO :(")

    if self.__dormido:
      return(f"{self.__nombre} NO puede baniarse, esta dormido")

    if not self.puede_realizar_actividades():
      return(f"{self.__nombre} NO puede reazliar mas actividades hasta que vuelva a dormir, ya realiz las 3 diarias")

    nueva_higiene = self.__higiene + 40
    nueva_diversion = self.__diversion - 10

    if nueva_higiene <= MascotaVirtual.__MAX_VALOR:
      self.__higiene = nueva_higiene
    else:
      self.__higiene = MascotaVirtual.__MAX_VALOR
  
    if nueva_diversion >= MascotaVirtual.__MIN_VALOR:
      self.__diversion = nueva_diversion
    else:
      self.__diversion = MascotaVirtual.__MIN_VALOR

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
    energia = self.__energia
    diversion = self.__diversion
    higiene = self.__higiene

    if energia > 70 and diversion > 70 and higiene > 70:
        return "Feliz"
    elif energia > 50 and diversion > 50 and higiene > 50:
        return "Alegre"
    elif (30 < energia <= 50) or (30 < diversion <= 50) or (30 < higiene <= 50):
        return "Neutral"
    elif (10 < energia <= 30) or (10 < diversion <= 30) or (10 < higiene <= 30):
        return "Triste"
    elif energia <= 10 or diversion <= 10 or higiene <= 10:
        return "Muy Triste"

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
    