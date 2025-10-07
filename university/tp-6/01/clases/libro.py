class Libro:
    def __init__(self, nombre: str, autor: str, editorial: str, categoria: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser una cadena de texto")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no puede estar vacio")

        if not isinstance(autor, str):
            raise TypeError("Autor tiene que ser una cadena de texto")
        if autor == "" or autor.isspace():
            raise ValueError("Autor no puede estar vacio")

        if not isinstance(editorial, str):
            raise TypeError("Editorial tiene que ser una cadena de texto")
        if editorial == "" or editorial.isspace():
            raise ValueError("Editorial no puede estar vacio")

        if not isinstance(categoria, str):
            raise TypeError("categoria tiene que ser una cadena de texto")
        if categoria == "" or categoria.isspace():
            raise ValueError("categoria no puede estar vacio")
        if categoria not in ('A', 'B', 'C'):
            raise ValueError("Categoría debe ser 'A', 'B' o 'C'")
            
        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria

    """CONSULTAS"""

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_autor(self) -> str:
        return self.__autor

    def obtener_editorial(self) -> str:
        return self.__editorial

    def obtener_categoria(self) -> str:
        return self.__categoria

    def __str__(self):
        return f"{self.__nombre} ({self.__categoria}) - {self.__autor}, {self.__editorial}"

