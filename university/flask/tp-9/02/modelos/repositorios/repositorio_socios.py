from modelos.entidades.socio import Socio
import json

class RepositorioSocio:
    __RUTA_ARCHIVO = 'datos/socios.json'

    def __init__(self):
        self.__socios = []
        self.__cargar_desde_archivo()

    def __cargar_desde_archivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding = 'utf-8') as archivo:
                datos_cargados = json.load(archivo)

                if 'socios' in datos_cargados:
                    lista_socios = datos_cargados['socios']
                    for s in lista_socios:
                        socio = Socio.from_diccionario(s)
                        self.__socios.append(socio)

        except Exception as e:
            print(f"Error al cargar los datos desde el archivo: {e}")

    def __guardar_en_archivo(self):
        lista_socios_diccionario = [socio.to_diccionario() for socio in self.__socios]

        datos_a_guardar = {
            'socios': lista_socios_diccionario
        }

        try:
            with open(self.__RUTA_ARCHIVO, 'w', encoding = 'utf-8') as archivo:
                json.dump(datos_a_guardar, archivo, indent = 4, ensure_ascii = False)

        except Exception as e:
            print(f"Error al cargar los datos en el archivo: {e}")

    def existe_socio(self, socio: Socio) -> bool:
        for s in self.__socios:
            if s == socio:
                return True
        
        return False
    
    def existe_socio_DNI(self, DNI: int) -> bool:
        for s in self.__socios:
            if s.obtener_DNI() == DNI:
                return True
            
        return False
    
    # PETICION GET ALL
    def obtener_socios(self) -> list[Socio]:
        return self.__socios
    
    # PETICION GET BY DNI
    def obtener_socio(self, DNI: int) -> Socio | None:
        for l in self.__socios:
            if l.obtener_DNI() == DNI:
                return l
            
        return None
    
    # PETICION POST
    def agregar_socio(self, socio: Socio) -> bool:
        if not isinstance(socio, Socio):
            raise TypeError("Socio tiene que ser una instancia de Socio")
        
        if not self.existe_socio_DNI(socio.obtener_DNI()):
            self.__socios.append(socio)
            self.__guardar_en_archivo()
            return True
        
        return False
    
    # PETICION DELETE
    def elimiar_socio(self, DNI: int) -> bool:
        for s in self.__socios:
            if s.obtener_DNI() == DNI:
                self.__socios.remove(s)
                self.__guardar_en_archivo()
                return True
            
        return False
    
    # PETICION PUT
    def actualizar_socio(self, DNI: int, data: dict) -> bool:
        socio = self.obtener_socio(DNI)

        if socio is not None:
            if 'DNI' in data:
                nuevo_DNI = data['DNI']

                if not isinstance(nuevo_DNI, int):
                    raise TypeError("Nuevo DNI tiene que ser un numero entero")
                if nuevo_DNI < 0:
                    raise ValueError("Nuevo DNI tiene que ser un numero positivo")
                
                socio.establecer_DNI(nuevo_DNI)
                
            if 'nombre' in data:
                nuevo_nombre = data['nombre']

                if not isinstance(nuevo_nombre, str):
                    raise TypeError("Nuevo nombre tiene que ser una cadena de texto")
                if nuevo_nombre == '' or nuevo_nombre.isspace():
                    raise ValueError("Nuevo nombre no puede estar vacio")
                
                socio.establecer_nombre(nuevo_nombre)
                
            if 'apellido' in data:
                nuevo_apellido = data['apellido']

                if not isinstance(nuevo_apellido, str):
                    raise TypeError("Nuevo apellido tiene que ser una cadena de texto")
                if nuevo_apellido == '' or nuevo_apellido.isspace():
                    raise ValueError("Nuevo apellido no puede estar vacio")
                
                socio.establecer_apellido(nuevo_apellido)
                
            if 'mail' in data:
                nuevo_mail = data['mail']

                if not isinstance(nuevo_mail, str):
                    raise TypeError("Nuevo mail tiene que ser una cadena de texto")
                if nuevo_mail == '' or nuevo_mail.isspace():
                    raise ValueError("Nuevo mail no puede estar vacio")
                
                socio.establecer_mail(nuevo_mail)
                
            if 'fecha_nacimiento' in data:
                nueva_fecha_nacimiento = data['fecha_nacimiento']

                if not isinstance(nueva_fecha_nacimiento, int):
                    raise TypeError("Nueva fecha nacimiento tiene que ser un numero entero")
                if nueva_fecha_nacimiento < 0 or nueva_fecha_nacimiento > 2025:
                    raise ValueError("Nueva fecha nacimiento tiene que ser un numero valido")
                
                socio.establecer_fecha_nacimiento(nueva_fecha_nacimiento)
                
            self.__guardar_en_archivo()
            return True
        
        return False
