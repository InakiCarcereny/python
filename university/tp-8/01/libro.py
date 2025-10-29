import json

class Libro:
    def __init__(self, titulo: str, autor: str, genero: str, ISBN: str, anio_publicacion: int):
        if not isinstance(titulo, str):
          raise TypeError("Titulo tiene que ser un string")
        if titulo == "" or titulo.isspace():
          raise ValueError("Titulo NO puede estar vacio")
        
        if not isinstance(autor, str):
          raise TypeError("Autor tiene que ser un string")
        if autor == "" or autor.isspace():
          raise ValueError("Autor NO puede estar vacio")
        
        if not isinstance(genero, str):
          raise TypeError("Genero tiene que ser un string")
        if genero == "" or genero.isspace():
          raise ValueError("Genero NO puede estar vacio")
        
        if not isinstance(ISBN, str):
          raise TypeError("ISBN tiene que ser un string")
        if ISBN == "" or ISBN.isspace():
          raise ValueError("ISBN NO puede estar vacio")
        
        if not isinstance(anio_publicacion, int):
          raise TypeError("Anio de publiacion tiene que ser un numero entero")
        if anio_publicacion <= 0 or anio_publicacion > 2025:
          raise ValueError("Anio de publiacion tiene que ser un numero valido")
        
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__ISBN = ISBN
        self.__anio_publicacion = anio_publicacion

    def obtener_anio_publicacion(self) -> int:
      return self.__anio_publicacion

    def a_json(self) -> str:
      libro = {
        "titulo": self.__titulo,
        "autor": self.__autor,
        "genero": self.__genero,
        "ISBN": self.__ISBN,
        "anio_publicacion": self.__anio_publicacion
        }
      
      return json.dumps(libro, ensure_ascii=False)

    @classmethod
    def desde_json(cls, json_data) -> 'Libro':
      datos = json.loads(json_data)

      return cls(datos["titulo"], datos["autor"], datos["genero"], datos["ISBN"], datos["anio_publicacion"])
    
    def __str__(self):
      return f"{self.__titulo} - {self.__autor} ({self.__anio_publicacion})"
 


