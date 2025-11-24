from modelos.entidades.hotel import Hotel
from modelos.entidades.ciudad import Ciudad
from modelos.entidades.pension import Pension
import json

class RepositorioHotel:
    __RUTA_ARCHIVO = 'datos/hoteles.json'

    def __init__(self):
        self.__hoteles: list[Hotel] = []
        self.__repo_paquetes = None
        self.__cargar_desde_archivo()

    def set_repo_paquetes(self, paquetes):
        self.__repo_paquetes = paquetes

    def __cargar_desde_archivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding = 'utf-8') as archivo:
                datos = json.load(archivo)

                for hotel_diccionario in datos['hoteles']:
                    hotel = Hotel.from_diccionario(hotel_diccionario)
                    self.__hoteles.append(hotel)

        except Exception as e:
            print(f"Error al cargar desde archivo: {e}")

    def __guardar_en_archivo(self):
        lista_hoteles_diccionario = [hotel.to_diccionario() for hotel in self.__hoteles]

        datos_a_guardar = {
            'hoteles': lista_hoteles_diccionario
        }

        try:
            with open(self.__RUTA_ARCHIVO, 'w', encoding = 'utf-8') as archivo:
                json.dump(datos_a_guardar, archivo, indent = 4, ensure_ascii = False)

        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

    def existe_hotel(self, hotel: Hotel) -> bool:
        for h in self.__hoteles:
            if h.es_igual(hotel):
                return True
            
        return False
    
    def existe_hotel_en_ciudad(self, nombre: str, ciudad: Ciudad) -> bool:
        for h in self.__hoteles:
            if h.obtener_nombre() == nombre and h.obtener_ciudad().obtener_nombre() == ciudad.obtener_nombre():
                return True
            
        return False

    # PETICION GET ALL
    def obtener_hoteles(self) -> list[Hotel]:
        return self.__hoteles
    
    # PETICION GET BY ID
    def obtener_hotel(self, id: int) -> Hotel | None:
        for h in self.__hoteles:
            if h.obtener_id() == id:
                return h
            
        return None
    
    # PETICION GET ID BY NOMBRE
    def obtener_id_por_nombre(self, nombre: str, ciudad: Ciudad) -> int:
        for h in self.__hoteles:
            if h.obtener_nombre() == nombre and h.obtener_ciudad().obtener_nombre() == ciudad.obtener_nombre():
                return h.obtener_id()
            
        return -1
    
    # PETICION POST
    def agregar_hotel(self, hotel: Hotel) -> bool:
        if not isinstance(hotel, Hotel):
            raise TypeError("Hotel tiene que ser una instancia de Hotel")
        
        if not self.existe_hotel_en_ciudad(hotel.obtener_nombre(), hotel.obtener_ciudad()):
            self.__hoteles.append(hotel)
            self.__guardar_en_archivo()
            return True
        
        return False
    
    # PETICION DELETE
    def eliminar_hotel(self, id: int) -> bool:
        hotel = self.obtener_hotel(id)

        if hotel is None:
            return False

        if self.__repo_paquetes is not None:
            for paquete in self.__repo_paquetes.obtener_paquetes():
                if paquete.obtener_hotel().obtener_id() == hotel.obtener_id():
                    raise Exception("No se puede eliminar el hotel: está siendo utilizado por un paquete grupal")

        self.__hoteles.remove(hotel)
        self.__guardar_en_archivo()
        return True
    
    # PETICION PUT
    def actualizar_hotel(self, id, data: dict) -> bool:
        hotel = self.obtener_hotel(id)

        if hotel is None:
            return False
        
        nombre_actual = hotel.obtener_nombre()
        estrellas_actual = hotel.obtener_estrellas()
        descripcion_actual = hotel.obtener_descripcion()
        pension_actual = hotel.obtener_pension()
        ciudad_actual = hotel.obtener_ciudad()

        nuevo_nombre = data.get('nombre', nombre_actual)
        nuevo_estrellas = data.get('estrellas', estrellas_actual)
        nuevo_descripcion = data.get('descripcion', descripcion_actual)
        nuevo_pension = data.get('pension', pension_actual)
        nuevo_ciudad = data.get('ciudad', ciudad_actual)

        if not isinstance(nuevo_nombre, str):
            raise TypeError("Nuevo nombre tiene que ser una cadena de texto")
        if nuevo_nombre == "" or nuevo_nombre.isspace():
            raise ValueError("Nuevo nombre no puede estar vacio")
        
        if not isinstance(nuevo_estrellas, int):
            raise TypeError("Nuevo estrellas tiene que ser un numero entero")
        if nuevo_estrellas < 0:
            raise ValueError("Nuevo estrellas tiene que ser positivo")
        
        if not isinstance(nuevo_descripcion, str):
            raise TypeError("Nuevo descripcion tiene que ser una cadena de texto")
        if nuevo_descripcion == "" or nuevo_descripcion.isspace():
            raise ValueError("Nuevo descripcion no puede estar vacio")
        
        if isinstance(nuevo_pension, str):
            try:
                nuevo_pension = Pension(nuevo_pension)
            except ValueError:
                raise ValueError("Pension inválida")
        
        if isinstance(nuevo_ciudad, dict):
            try:
                nuevo_ciudad = Ciudad.from_diccionario(nuevo_ciudad)
            except ValueError:
                raise ValueError("Ciudad invalida")

        if(nombre_actual == nuevo_nombre and
           estrellas_actual == nuevo_estrellas and
           descripcion_actual == nuevo_descripcion and
           pension_actual == nuevo_pension and
           ciudad_actual == nuevo_ciudad):
            raise Exception("Tiene que modificar alguno de los campos")
        
        for otro in self.__hoteles:
            if otro.obtener_id() != id:
                if(otro.obtener_nombre().lower() == nuevo_nombre.lower() and
                   otro.obtener_estrellas() == nuevo_estrellas and
                   otro.obtener_descripcion().lower() == nuevo_descripcion.lower() and
                   otro.obtener_pension() == nuevo_pension and
                   otro.obtener_ciudad().to_diccionario() == nuevo_ciudad.to_diccionario()):
                    raise Exception("Ya existe un hotel con esos datos (duplicado)")
                
        hotel.establecer_nombre(nuevo_nombre)
        hotel.establecer_estrellas(nuevo_estrellas)
        hotel.establecer_descripcion(nuevo_descripcion)
        hotel.establecer_pension(nuevo_pension)
        hotel.establecer_ciudad(nuevo_ciudad)
                
        self.__guardar_en_archivo()
        return True