from modelos.entidades.prestamo import Prestamo
import json

class RepositorioPrestamos:
    __RUTA_ARCHIVO = 'datos/prestamos.json'

    def __init__(self):
        self.__prestamos: list[Prestamo] = []
        self.__cargar_desde_archivo()

    def __cargar_desde_archivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding = 'utf-8') as archivo:
                datos = json.load(archivo)

                for prestamos_diccionario in datos:
                    prestamo = Prestamo.from_diccionario(prestamos_diccionario)
                    self.__prestamos.append(prestamo)

        except Exception as e:
            print(f"Error al cargar desde archivo: {e}")

    def __guardar_en_archivo(self):
        lista_prestamos_diccionario = [prestamo.to_diccionario() for prestamo in self.__prestamos]

        datos_a_guardar = {
            'prestamos': lista_prestamos_diccionario
        }

        try:
            with open(self.__RUTA_ARCHIVO, 'w', encoding = 'utf-8') as archivo:
                json.dump(datos_a_guardar, archivo, indent = 4, ensure_ascii = False)
        
        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

    def esta_devuelto(self, prestamo: Prestamo) -> bool:
        if not isinstance(prestamo, Prestamo):
            raise TypeError("Prestamo tiene que ser una instancia de Prestamo")
        
        if prestamo.obtener_fecha_devolucion() is None:
            return False
        
        return True
    
    def existe_prestamo(self, socio_dni: int, libro_isbn: int, fecha_retiro: int) -> bool:
        for p in self.__prestamos:
            if p.obtener_socio_dni() == socio_dni and p.obtener_libro_isbn() == libro_isbn and p.obtener_fecha_retiro() == fecha_retiro:
                return True
            
        return False
    
    def cantidad_libros_sin_devolver(self, ISBN: int) -> int:
        contador = 0

        for p in self.__prestamos:
            if p.obtener_libro_isbn() == ISBN:
                contador += 1

        return contador

    # PETICION GET ALL
    def obtener_prestamos(self) -> list[Prestamo]:
        return self.__prestamos
    
    # PETICION GET BY COMBINACION
    def obtener_prestamo(self, socio_dni: int, libro_isbn: int, fecha_retiro: int) -> Prestamo | None:
        for p in self.__prestamos:
            if p.obtener_socio_dni() == socio_dni and p.obtener_libro_isbn() == libro_isbn and p.obtener_fecha_retiro() == fecha_retiro:
                return p
            
        return None
    
    # PETICION GET BY ID
    def obtener_prestamo_id(self, id: int) -> Prestamo | None:
        for p in self.__prestamos:
            if p.obtener_ID() == id:
                return p
            
        return None
    
    # PETICION POST
    def agregar_prestamo(self, prestamo: Prestamo) -> bool:
        if not isinstance(prestamo, Prestamo):
            raise TypeError("Prestamo tiene que ser una instancia de Prestamo")
        
        if self.cantidad_libros_sin_devolver(prestamo.obtener_libro_isbn()) >= 5:
            print("El libro solicitado no tiene ejemplares disponibles para prestar")
        
        if not self.existe_prestamo(prestamo.obtener_socio_dni(), prestamo.obtener_libro_isbn(), prestamo.obtener_fecha_retiro()):
            self.__prestamos.append(prestamo)
            self.__guardar_en_archivo()
            return True
        
        return False
    
    # PETICION DELETE
    def eliminar_prestamo(self, id: int) -> bool:
        for p in self.__prestamos:
            if p.obtener_ID() == id:
                self.__prestamos.remove(p)
                self.__guardar_en_archivo()
                return True
            
        return False
    
    # PETICION PUT
    def actualizar_prestamo(self, id: int, data: dict) -> bool:
        prestamo = self.obtener_prestamo_id(id)

        if prestamo is not None:
            if 'socio_dni' in data:
                nuevo_socio_dni = data['socio_dni']

                if not isinstance(nuevo_socio_dni, int):
                    raise TypeError("Nuevo socio dni tiene que ser un numero entero")
                if nuevo_socio_dni < 0:
                    raise ValueError("Nuevo socio dni tiene que ser positivo")
                
                prestamo.establecer_socio_dni(nuevo_socio_dni)
                
            if 'libro_isbn' in data:
                nuevo_libro_isbn = data['libro_isbn']

                if not isinstance(nuevo_libro_isbn, int):
                    raise TypeError("Nuevo libro isbn tiene que ser un numero entero")
                if nuevo_libro_isbn < 0:
                    raise ValueError("Nuevo libro isbn tiene que ser positivo")
                
                prestamo.establecer_libro_isbn(nuevo_libro_isbn)
                
            if 'fecha_retiro' in data:
                nueva_fecha_retiro = data['fecha_retiro']

                if not isinstance(nueva_fecha_retiro, int):
                    raise TypeError("Nueva fecha retiro tiene que ser un numero entero")
                if nueva_fecha_retiro < 0 or nueva_fecha_retiro > 2025:
                    raise ValueError("Nueva fecha retiro tiene que ser un numero valido")
                
                prestamo.establecer_fecha_retiro(nueva_fecha_retiro)
                
            if 'cant_dias' in data:
                nuevo_cant_dias = data['cant_dias']

                if not isinstance(nuevo_cant_dias, int):
                    raise TypeError("Nuevo cantidad dias tiene que ser un numero entero")
                if nuevo_cant_dias < 0:
                    raise ValueError("Nuevo cantidad dias tiene que ser positivo")
                
                prestamo.establecer_cant_dias(nuevo_cant_dias)

            self.__guardar_en_archivo()
            return True
        
        return False
    
    # PETICION PUT DEVOLVER LIBRO
    def devolver_libro(self, id: int, fecha_devolucion: int) -> bool:
        prestamo = self.obtener_prestamo_id(id)

        if prestamo is not None:
            if not isinstance(fecha_devolucion, int):
                raise TypeError("Fecha devolucion tiene que ser un numero entero")
            if fecha_devolucion < 0 or fecha_devolucion > 2025:
                raise ValueError("Fecha devolucion tiene que ser un numero valido")
        
            prestamo.establecer_fecha_devolucion(fecha_devolucion)

            self.__guardar_en_archivo()
            return True
        
        return False
    