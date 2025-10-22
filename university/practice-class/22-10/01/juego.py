from producto import Producto
from consola import Consola

class Juego(Producto):
    def __init__(self, id: int, precio: float | int, nombre: str, genero: str, anio: int, descripcion: str, multijugador: bool):
        super().__init__(id, precio)
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre NO puede estar vacio")
        
        if not isinstance(genero, str):
            raise TypeError("Genero tiene que ser un string")
        if genero == "" or genero.isspace():
            raise ValueError("Genero NO puede estar vacio")
        
        if not isinstance(anio, int):
            raise TypeError("Anio tiene que ser un numero entero")
        if anio < 1980 or anio >=2025:
            raise ValueError("Anio tiene que ser un numero valido")
        
        if not isinstance(descripcion, str):
            raise TypeError("Descripcion tiene que ser un string")
        if descripcion == "" or descripcion.isspace():
            raise ValueError("Descripcion NO puede estar vacio")
        
        if not isinstance(multijugador, bool):
            raise TypeError("Multijugador tiene que ser un booleano")
        
        self._nombre = nombre
        self._genero = genero
        self._anio = anio
        self._descripcion = descripcion
        self._multijugador = multijugador
        self._consolas_compatibles: list[Consola] = []

    def agregar_consola_compatible(self, consola: 'Consola'):
        if not isinstance(consola, Consola):
            raise TypeError("Consola tiene que ser una instancia de Consola")

        if not consola in self._consolas_compatibles:
            self._consolas_compatibles.append(consola)
        else:
            raise ValueError("Esa consola ya se encuentra en la lista de consolas compatibles")
        
    def eliminar_consola_compatible(self, consola: 'Consola'):
        if not isinstance(consola, Consola):
            raise TypeError("Consola tiene que ser una instancia de Consola")
        
        if consola in self._consolas_compatibles:
            self._consolas_compatibles.remove(consola)
        else:
            raise ValueError("Esa consola NO se encuentra en la lista de consolas compatibles")