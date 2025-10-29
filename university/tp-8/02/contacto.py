import json

class Contacto:
    def __init__(self, nombre: str, apellido: str, telefono: str, correo_electronico: str, direccion: str):
        if not isinstance(nombre, str):
          raise TypeError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
          raise ValueError("Nombre NO puede estar vacio")
        
        if not isinstance(apellido, str):
          raise TypeError("Apellido tiene que ser un string")
        if apellido == "" or apellido.isspace():
          raise ValueError("Apellido NO puede estar vacio")
        
        if not isinstance(telefono, str):
          raise TypeError("Telefono tiene que ser un string")
        if telefono == "" or telefono.isspace():
          raise ValueError("Telefono NO puede estar vacio")
        
        if not isinstance(correo_electronico, str):
          raise TypeError("Correo electronico tiene que ser un string")
        if correo_electronico == "" or correo_electronico.isspace():
          raise ValueError("Correo electronico NO puede estar vacio")
        
        if not isinstance(direccion, str):
          raise TypeError("Direccion tiene que ser un string")
        if direccion == "" or direccion.isspace():
          raise ValueError("Direccion NO puede estar vacio")
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correo_electronico = correo_electronico
        self.__direccion = direccion

    def obtener_nombre(self) -> str:
      return self.__nombre
    
    def obtener_apellido(self) -> str:
      return self.__apellido
    
    def obtener_telefono(self) -> str:
      return self.__telefono
    
    def obtener_correo_electronico(self) -> str:
      return self.__correo_electronico
    
    def obtener_direccion(self) -> str:
      return self.__direccion

    def a_json(self) -> dict:
      return {
        "nombre": self.__nombre,
        "apellido": self.__apellido,
        "telefono": self.__telefono,
        "correo_electronico": self.__correo_electronico,
        "direccion": self.__direccion
      }
    
    @classmethod
    def desde_json(cls, json_data) -> 'Contacto':      
      return cls(json_data["nombre"], json_data["apellido"], json_data["telefono"], json_data["correo_electronico"], json_data["direccion"])
    
    def __str__(self) -> str:
      return f"{self.__nombre} - {self.__apellido} - {self.__telefono} - {self.__correo_electronico} - {self.__direccion}" 