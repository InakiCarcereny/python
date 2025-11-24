from modelos.entidades.ciudad import Ciudad
import json

class RepositorioCiudad:
    __RUTA_ARCHIVO = 'datos/ciudades.json'

    def __init__(self):
        self.__ciudades: list[Ciudad] = []
        self.__repo_hoteles = None
        self.__repo_paquetes = None
        self.__cargar_desde_archivo()

    def set_repo_hoteles(self, repo_hoteles):
        self.__repo_hoteles = repo_hoteles

    def set_repo_paquetes_grupales(self, paquetes_grupales):
        self.__repo_paquetes = paquetes_grupales

    def __cargar_desde_archivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding = 'utf-8') as archivo:
                datos = json.load(archivo)

                for ciudad_diccionario in datos['ciudades']:
                    ciudad = Ciudad.from_diccionario(ciudad_diccionario)
                    self.__ciudades.append(ciudad)

        except Exception as e:
            print(f"Error al cargar desde archivo: {e}")

    def __guardar_en_archivo(self):
        lista_ciudades_diccionario = [ciudad.to_diccionario() for ciudad in self.__ciudades]

        datos_a_guardar = {
            'ciudades': lista_ciudades_diccionario
        }

        try:
            with open(self.__RUTA_ARCHIVO, 'w', encoding = 'utf-8') as archivo:
                json.dump(datos_a_guardar, archivo, indent = 4, ensure_ascii = False)

        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

    def existe_ciudad(self, ciudad: Ciudad) -> bool:
        for c in self.__ciudades:
            if c == ciudad:
                return True
            
        return False
    
    def existe_ciudad_nombre_provincia(self, nombre: str, provincia: str) -> bool:
        for c in self.__ciudades:
            if c.obtener_nombre() == nombre and c.obtener_provincia() == provincia:
                return True
            
        return False

    # PETICION GET ALL
    def obtener_ciudades(self) -> list[Ciudad]:
        return self.__ciudades
    
    # PETICION GET BY NOMBRE
    def obtener_ciudad_nombre(self, nombre: str) -> Ciudad | None:
        for c in self.__ciudades:
            if c.obtener_nombre() == nombre:
                return c
            
        return None
    
    # PETICION GET BY ID
    def obtener_ciudad_id(self, id: int) -> Ciudad | None:
        for c in self.__ciudades:
            if c.obtener_id() == id:
                return c
            
        return None
    
    # PETICION POST
    def agregar_ciudad(self, ciudad: Ciudad) -> bool:
        if not isinstance(ciudad, Ciudad):
            raise TypeError("Ciudad tiene que ser una instancia de Ciudad")
        
        if not self.existe_ciudad_nombre_provincia(ciudad.obtener_nombre(), ciudad.obtener_provincia()):
            self.__ciudades.append(ciudad)
            self.__guardar_en_archivo()
            return True
        
        return False
    
    # PETICION DELETE
    def eliminar_ciudad(self, id: int) -> bool:
        ciudad = self.obtener_ciudad_id(id)

        if ciudad is None:
            return False

        if self.__repo_hoteles is not None:
            for hotel in self.__repo_hoteles.obtener_hoteles():
                if hotel.obtener_ciudad().obtener_id() == ciudad.obtener_id():
                    raise Exception("No se puede eliminar la ciudad: está siendo utilizada por un hotel")

        if self.__repo_paquetes is not None:
            for paquete in self.__repo_paquetes.obtener_paquetes():
                if paquete.obtener_ciudad().obtener_id() == ciudad.obtener_id():
                    raise Exception("No se puede eliminar la ciudad: está siendo utilizada por un paquete grupal")

        self.__ciudades.remove(ciudad)
        self.__guardar_en_archivo()
        return True
    
    # PETICION PUT
    def actualizar_ciudad(self, id: int, data: dict) -> bool:
        ciudad = self.obtener_ciudad_id(id)

        if ciudad is None:
            return False

        nombre_actual = ciudad.obtener_nombre()
        provincia_actual = ciudad.obtener_provincia()
        puntos_actuales = ciudad.obtener_puntos_turisticos()

        nuevo_nombre = data.get('nombre', nombre_actual)
        nueva_provincia = data.get('provincia', provincia_actual)
        nuevos_puntos = data.get('puntos_turisticos', puntos_actuales)

        if not isinstance(nuevo_nombre, str):
            raise TypeError("Nuevo nombre tiene que ser una cadena de texto")
        if nuevo_nombre.strip() == "":
            raise ValueError("Nuevo nombre no puede estar vacío")

        if not isinstance(nueva_provincia, str):
            raise TypeError("Nueva provincia tiene que ser una cadena de texto")
        if nueva_provincia.strip() == "":
            raise ValueError("Nueva provincia no puede estar vacía")

        if not isinstance(nuevos_puntos, str):
            raise TypeError("Nuevos puntos turísticos tiene que ser una cadena de texto")
        if nuevos_puntos.strip() == "":
            raise ValueError("Los puntos turísticos no pueden estar vacíos")

        if (nuevo_nombre == nombre_actual and
            nueva_provincia == provincia_actual and
            nuevos_puntos == puntos_actuales):
            raise Exception("Debe modificar al menos un campo para actualizar la ciudad")

        for otra in self.__ciudades:
            if otra.obtener_id() != id:
                if (otra.obtener_nombre().lower() == nuevo_nombre.lower() and
                    otra.obtener_provincia().lower() == nueva_provincia.lower() and
                    otra.obtener_puntos_turisticos().lower() == nuevos_puntos.lower()):
                    raise Exception("Ya existe una ciudad con esos datos (duplicado)")

        ciudad.establecer_nombre(nuevo_nombre)
        ciudad.establecer_provincia(nueva_provincia)
        ciudad.establecer_puntos_turisticos(nuevos_puntos)

        self.__guardar_en_archivo()
        return True