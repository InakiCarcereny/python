from modelos.entidades.libro import Libro
from modelos.entidades.prestamo import Prestamo
import json

class RepositorioLibros:
    __RUTA_ARCHIVO = 'datos/libros.json'

    def __init__(self):
        self.__libros: list[Libro] = []
        self.__cargar_desde_archivo()

    def __cargar_desde_archivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding = 'utf-8') as archivo:
                datos = json.load(archivo)

                for libro in datos:
                    l = Libro.from_diccionario(libro)
                    self.__libros.append(l)
        
        except Exception as e:
            print(f"Error al cargar desde archivo: {e}")

    def __guardar_en_archivo(self):
        lista_libros_diccionario = [libro.to_diccionario() for libro in self.__libros]

        datos_a_guardar = {
            'libros': lista_libros_diccionario
        }

        try:
            with open(self.__RUTA_ARCHIVO, 'w', encoding = 'utf-8') as archivo:
                json.dump(datos_a_guardar, archivo, indent = 4, ensure_ascii = False)

        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

    def existe_libro(self, libro: Libro) -> bool:
        for l in self.__libros:
            if l == libro:
                return True
            
        return False
    
    def existe_libro_ISBN(self, ISBN: int) -> bool:
        for l in self.__libros:
            if l.obtener_ISBN() == ISBN:
                return True
            
        return False

    # PETICION GET ALL
    def obtener_libros(self) -> list[Libro]:
        return self.__libros
    
    # PETICION GET BY ISBN
    def obtener_libro_ISBN(self, ISBN: int) -> Libro | None:
        for l in self.__libros:
            if l.obtener_ISBN() == ISBN:
                return l
            
        return None
    
    # PETICION POST
    def agregar_libro(self, libro: Libro) -> bool:
        if not isinstance(libro, Libro):
            raise TypeError("Libro tiene que ser una instancia de Libro")
        
        if not self.existe_libro_ISBN(libro.obtener_ISBN()):
            self.__libros.append(libro)
            self.__guardar_en_archivo()
            return True
        
        return False
    
    # PETICION DELETE
    def eliminar_libro(self, ISBN: int, prestamos: list[Prestamo]) -> bool:
        libro = self.obtener_libro_ISBN(ISBN)
        prestado = False

        for p in prestamos:
            if p.obtener_libro_isbn() == ISBN and p.obtener_fecha_devolucion() is None:
                prestado = True

        if libro is not None and not prestado:
            self.__libros.remove(libro)
            self.__guardar_en_archivo()
            return True
        
        return False
    
    # PETICION UPDATE
    def actualizar_libro(self, ISBN: int, data: dict) -> bool:
        libro = self.obtener_libro_ISBN(ISBN)

        if libro is not None:
            if 'ISBN' in data:
                nuevo_ISBN = data['ISBN']

                if not isinstance(nuevo_ISBN, int):
                    raise TypeError("Nuevo ISBN tiene que ser un numero entero")
                if nuevo_ISBN < 0:
                    raise ValueError("Nuevo ISBN tiene que ser un numero positivo")
                
                libro.establecer_ISBN(nuevo_ISBN)
                
            if 'titulo' in data:
                nuevo_titulo = data['titulo']

                if not isinstance(nuevo_titulo, str):
                    raise TypeError("Nuevo titulo tiene que ser una cadena de texto")
                if nuevo_titulo == '' or nuevo_titulo.isspace():
                    raise ValueError("Nuevo titulo no puede estar vacio")
                
                libro.establecer_titulo(nuevo_titulo)
                
            if 'autor' in data:
                nuevo_autor = data['autor']

                if not isinstance(nuevo_autor, str):
                    raise TypeError("Nuevo autor tiene que ser una cadena de texto")
                if nuevo_autor == '' or nuevo_autor.isspace():
                    raise ValueError("Nuevo autor no puede estar vacio")
                
                libro.establecer_autor(nuevo_autor)
                
            if 'genero' in data:
                nuevo_genero = data['genero']

                if not isinstance(nuevo_genero, str):
                    raise TypeError("Nuevo genero tiene que ser una cadena de texto")
                if nuevo_genero == '' or nuevo_genero.isspace():
                    raise ValueError("Nuevo genero no puede estar vacio")
                
                libro.establecer_genero(nuevo_genero)
                
            if 'anio_publicacion' in data:
                nuevo_anio_publicacion = data['anio_publicacion']

                if not isinstance(nuevo_anio_publicacion, int):
                    raise TypeError("Nuevo anio de publicacion tiene que ser un numero entero")
                if nuevo_anio_publicacion < 0 or nuevo_anio_publicacion > 2025:
                    raise ValueError("Nuevo anio de publicacion tiene que ser un numero valido")
                
                libro.establecer_anio_publicacion(nuevo_anio_publicacion)
                
            self.__guardar_en_archivo()
            return True
        
        return False