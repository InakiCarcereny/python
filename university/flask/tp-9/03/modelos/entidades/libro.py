class Libro:
    __CANTIDAD_EJEMPLARES: int = 5

    @classmethod
    def from_diccionario(cls, data: dict) -> 'Libro':
        if not isinstance(data, dict):
            raise TypeError("Data tiene que ser de tipo diccionario")
        if 'ISBN' not in data or 'titulo' not in data or 'autor' not in data or 'genero' not in data or 'anio_publicacion' not in data:
            raise ValueError("Data tiene que tener las claves ISBN, titulo, autor, genero, anio_publicacion")
        
        return cls(
            ISBN = data['ISBN'],
            titulo = data['titulo'],
            autor = data['autor'],
            genero = data['genero'],
            anio_publicacion = data['anio_publicacion']
        )
    
    def __init__(self, ISBN: int, titulo: str, autor: str, genero: str, anio_publicacion: int):
        if not isinstance(ISBN, int):
            raise TypeError("ISBN tiene que ser un numero entero")
        if ISBN < 0:
            raise ValueError("ISBN tiene que ser un numero positivo")
        
        if not isinstance(titulo, str):
            raise TypeError("Titulo tiene que ser una cadena de texto")
        if titulo == "" or titulo.isspace():
            raise ValueError("Titulo no puede estar vacio")
        
        if not isinstance(autor, str):
            raise TypeError("Autor tiene que ser una cadena de texto")
        if autor == "" or autor.isspace():
            raise ValueError("Autor no puede estar vacio")
        
        if not isinstance(genero, str):
            raise TypeError("Genero tiene que ser una cadena de texto")
        if genero == "" or genero.isspace():
            raise ValueError("Genero no puede estar vacio")
        
        if not isinstance(anio_publicacion, int):
            raise TypeError("Anio de publicacion tiene que ser un numero entero")
        if anio_publicacion < 0 or anio_publicacion > 2025:
            raise ValueError("Anio de publicacion tiene que ser un anio valido")
        
        self.__ISBN = ISBN
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio_publicacion = anio_publicacion
        self.__cantidad_ejemplares = Libro.__CANTIDAD_EJEMPLARES

    def obtener_ISBN(self) -> int:
        return self.__ISBN
    
    def obtener_titulo(self) -> str:
        return self.__titulo
    
    def obtener_autor(self) -> str:
        return self.__autor
    
    def obtener_genero(self) -> str:
        return self.__genero
    
    def obtener_anio_publicacion(self) -> int:
        return self.__anio_publicacion
    
    def obtener_cantidad_ejemplares(self) -> int:
        return self.__cantidad_ejemplares
    
    def establecer_ISBN(self, ISBN: int):
        if not isinstance(ISBN, int):
            raise TypeError("ISBN tiene que ser un numero entero")
        if ISBN < 0:
            raise ValueError("ISBN tiene que ser un numero positivo")
        
        self.__ISBN = ISBN

    def establecer_titulo(self, titulo: str):
        if not isinstance(titulo, str):
            raise TypeError("Titulo tiene que ser una cadena de texto")
        if titulo == "" or titulo.isspace():
            raise ValueError("Titulo no puede estar vacio")
        
        self.__titulo = titulo

    def establecer_autor(self, autor: str):
        if not isinstance(autor, str):
            raise TypeError("Autor tiene que ser una cadena de texto")
        if autor == "" or autor.isspace():
            raise ValueError("Autor no puede estar vacio")
        
        self.__autor = autor

    def establecer_genero(self, genero: str):
        if not isinstance(genero, str):
            raise TypeError("Genero tiene que ser una cadena de texto")
        if genero == "" or genero.isspace():
            raise ValueError("Genero no puede estar vacio")
        
        self.__genero = genero

    def establecer_anio_publicacion(self, anio_publicacion: int):
        if not isinstance(anio_publicacion, int):
            raise TypeError("Anio de publicacion tiene que ser un numero entero")
        if anio_publicacion < 0 or anio_publicacion > 2025:
            raise ValueError("Anio de publicacion tiene que ser un anio valido")
        
        self.__anio_publicacion = anio_publicacion

    def establecer_cantidad_ejemplares(self, cantidad_ejemplares: int):
        if not isinstance(cantidad_ejemplares, int):
            raise TypeError("Cantidad de ejemplares tiene que ser un numero entero")
        if cantidad_ejemplares < 0:
            raise ValueError("Cantidad de ejemplares tiene que ser un numero positivo")
        
        self.__cantidad_ejemplares = cantidad_ejemplares

    def es_igual(self, otro: 'Libro') -> bool:
        return self == otro
    
    def to_diccionario(self) -> dict:
        return {
            'ISBN': self.__ISBN,
            'titulo': self.__titulo,
            'autor': self.__autor,
            'genero': self.__genero,
            'anio_publicacion': self.__anio_publicacion,
            'cantidad_ejemplares': self.__cantidad_ejemplares
        }
    
    def __str__(self) -> str:
        return (
            f"ISBN: {self.__ISBN} \n"
            f"titulo: {self.__titulo} \n"
            f"autor: {self.__autor} \n"
            f"genero: {self.__genero} \n"
            f"anio_publicacion: {self.__anio_publicacion} \n"
            f"cantidad_ejemplares: {self.__cantidad_ejemplares} \n"
        )

