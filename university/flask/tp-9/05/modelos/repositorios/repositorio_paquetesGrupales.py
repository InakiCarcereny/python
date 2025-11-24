from modelos.entidades.paqueteGrupal import PaqueteGrupal
from modelos.entidades.ciudad import Ciudad
from modelos.entidades.hotel import Hotel
from modelos.entidades.tipoViaje import TipoViaje
from modelos.entidades.transporte import Transporte

from datetime import date

import json

class RepositorioPaqueteGrupal:
    __RUTA_ARCHIVO = 'datos/paquetes-grupales.json'

    def __init__(self):
        self.__paquetes_grupales: list[PaqueteGrupal] = []
        self.__cargar_desde_archivo()

    def __cargar_desde_archivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding = 'utf-8') as archivo:
                datos = json.load(archivo)

                for paquete_grupal_diccionario in datos['paquetes-grupales']:
                    paquete_grupal = PaqueteGrupal.from_diccionario(paquete_grupal_diccionario)
                    self.__paquetes_grupales.append(paquete_grupal)

        except Exception as e:
            print(f"Error al cargar desde archivo: {e}")

    def __guardar_en_archivo(self):
        lista_paquetes_grupales_diccionario = [paquete_grupal.to_diccionario() for paquete_grupal in self.__paquetes_grupales]

        datos_a_guardar = {
            'paquetes-grupales': lista_paquetes_grupales_diccionario
        }

        try:
            with open(self.__RUTA_ARCHIVO, 'w', encoding = 'utf-8') as archivo:
                json.dump(datos_a_guardar, archivo, indent = 4, ensure_ascii = False)

        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

    def existe_paquete(self, paquete: PaqueteGrupal) -> bool:
        for p in self.__paquetes_grupales:
            if p.es_igual(paquete):
                return True
            
        return False
    
    def existe_paquete_clave(self, ciudad: Ciudad, hotel: Hotel, fecha_salida: date, fecha_vuelta: date, tipo: TipoViaje, transporte: Transporte) -> bool:
        for p in self.__paquetes_grupales:
            if p.obtener_ciudad().obtener_nombre() == ciudad.obtener_nombre() and p.obtener_hotel().obtener_nombre() == hotel.obtener_nombre() and p.obtener_fecha_salida() == fecha_salida and p.obtener_fecha_vuelta() == fecha_vuelta and p.obtener_tipo() == tipo and p.obtener_transporte() == transporte:
                return True
            
        return False

    # PETICION GET ALL
    def obtener_paquetes_grupales(self) -> list[PaqueteGrupal]:
        return self.__paquetes_grupales
    
    # PETICION GET BY ID
    def obtener_paquete_grupal_id(self, id: int) -> PaqueteGrupal | None:
        for p in self.__paquetes_grupales:
            if p.obtener_id() == id:
                return p
            
        return None
    
    # PETICION GET BY PAQUETE CLAVE
    def obtener_paquete_grupal(self, ciudad: Ciudad, hotel: Hotel, fecha_salida: date, fecha_vuelta: date, tipo: TipoViaje, transporte: Transporte) -> PaqueteGrupal | None:
        for p in self.__paquetes_grupales:
            if p.obtener_ciudad().obtener_nombre() == ciudad.obtener_nombre() and p.obtener_hotel().obtener_nombre() == hotel.obtener_nombre() and p.obtener_fecha_salida() == fecha_salida and p.obtener_fecha_vuelta() == fecha_vuelta and p.obtener_tipo() == tipo and p.obtener_transporte() == transporte:
                return p
            
        return None
    
    # PETICION POST
    def agregar_paquete_grupal(self, paquete: PaqueteGrupal) -> bool:
        if not isinstance(paquete, PaqueteGrupal):
            raise TypeError("Paquete tiene que ser una instancia de PaqueteGrupal")
        
        if not self.existe_paquete_clave(paquete.obtener_ciudad(), paquete.obtener_hotel(), paquete.obtener_fecha_salida(), paquete.obtener_fecha_vuelta(), paquete.obtener_tipo(), paquete.obtener_transporte()):
            self.__paquetes_grupales.append(paquete)
            self.__guardar_en_archivo()
            return True
        
        return False
    
    # PETICION DELETE
    def eliminar_paquete_grupal(self, id: int) -> bool:
        for p in self.__paquetes_grupales:
            if p.obtener_id() == id:
                self.__paquetes_grupales.remove(p)
                self.__guardar_en_archivo()
                return True
            
        return False
    
    # PETICION PUT
    def actualizar_paquete_grupal(self, id: int, data: dict) -> bool:
        paquete_grupal = self.obtener_paquete_grupal_id(id)

        if paquete_grupal is None:
            return False
        
        fecha_salida_actual = paquete_grupal.obtener_fecha_salida()
        fecha_vuelta_actual = paquete_grupal.obtener_fecha_vuelta()
        descripcion_actual = paquete_grupal.obtener_descripcion()
        tipo_actual = paquete_grupal.obtener_tipo()
        transporte_actual = paquete_grupal.obtener_transporte()
        precio_actual = paquete_grupal.obtener_precio()
        ciudad_actual = paquete_grupal.obtener_ciudad()
        hotel_actual = paquete_grupal.obtener_hotel()
        cupo_maximo_actual = paquete_grupal.obtener_cupo_maximo()
        cupo_actual_actual = paquete_grupal.obtener_cupo_actual()

        nuevo_fecha_salida = data.get('fecha_salida', fecha_salida_actual)
        nuevo_fecha_vuelta = data.get('fecha_vuelta', fecha_vuelta_actual)
        nuevo_descripcion = data.get('descripcion', descripcion_actual)
        nuevo_tipo = data.get('tipo', tipo_actual)
        nuevo_transporte = data.get('transporte', transporte_actual)
        nuevo_precio = data.get('precio', precio_actual)
        nuevo_ciudad = data.get('ciudad', ciudad_actual)
        nuevo_hotel = data.get('hotel', hotel_actual)
        nuevo_cupo_maximo = data.get('cupo_maximo', cupo_maximo_actual)
        nuevo_cupo_actual = data.get('cupo_actual', cupo_actual_actual)

        if not isinstance(nuevo_fecha_salida, date):
            raise TypeError("Fecha salida tiene que ser de tipo date")
        
        if not isinstance(nuevo_fecha_vuelta, date):
            raise TypeError("Fecha vuelta tiene que ser de tipo date")
        
        if not isinstance(nuevo_descripcion, str):
            raise TypeError("Descripcion tiene que ser una cadena de texto")
        if nuevo_descripcion == "" or nuevo_descripcion.isspace():
            raise ValueError("Descripcion no puede estar vacio")
        
        if isinstance(nuevo_tipo, str):
            try:
                nuevo_tipo = TipoViaje(nuevo_tipo)
            except ValueError:
                raise ValueError("Tipo viaje inválido")
        
        if isinstance(nuevo_transporte, str):
            try:
                nuevo_transporte = Transporte(nuevo_transporte)
            except ValueError:
                raise ValueError("Transporte inválido")
        
        if not isinstance(nuevo_precio, (int, float)):
            raise TypeError("Precio tiene que ser un numero entero o con decimales")
        if nuevo_precio < 0:
            raise ValueError("Precio tiene que ser positivo")
        
        if isinstance(nuevo_ciudad, dict):
            try:
                nuevo_ciudad = Ciudad.from_diccionario(nuevo_ciudad)
            except ValueError:
                raise ValueError("Ciudad invalida")
        
        if isinstance(nuevo_hotel, dict):
            try:
                nuevo_hotel = Hotel.from_diccionario(nuevo_hotel)
            except ValueError:
                raise ValueError("Hotel invalido")
        
        if not isinstance(nuevo_cupo_maximo, int):
            raise TypeError("Cupo maximo tiene que ser un numero entero")
        if nuevo_cupo_maximo < 0:
            raise ValueError("Cupo maximo tiene que ser positivo")
        
        if not isinstance(nuevo_cupo_actual, int):
            raise TypeError("Cupo actual tiene que ser un numero entero")
        if nuevo_cupo_actual < 0:
            raise ValueError("Cupo actual tiene que ser positivo")
        
        if (nuevo_fecha_salida == fecha_salida_actual and
            nuevo_fecha_vuelta == fecha_vuelta_actual and
            nuevo_descripcion == descripcion_actual and
            nuevo_tipo == tipo_actual and
            nuevo_transporte == transporte_actual and
            nuevo_precio == precio_actual and
            nuevo_ciudad == ciudad_actual and
            nuevo_hotel == hotel_actual and
            nuevo_cupo_maximo == cupo_maximo_actual and
            nuevo_cupo_actual == cupo_actual_actual):
            raise Exception("Debe modificar al menos un campo")

        for otro in self.__paquetes_grupales:
            if otro.obtener_id() != id:
                if (otro.obtener_fecha_salida() == nuevo_fecha_salida and
                    otro.obtener_fecha_vuelta() == nuevo_fecha_vuelta and
                    otro.obtener_descripcion().lower() == nuevo_descripcion.lower() and
                    otro.obtener_tipo() == nuevo_tipo and
                    otro.obtener_transporte() == nuevo_transporte and
                    otro.obtener_precio() == nuevo_precio and
                    otro.obtener_ciudad().to_diccionario() == nuevo_ciudad.to_diccionario() and
                    otro.obtener_hotel().to_diccionario() == nuevo_hotel.to_diccionario() and
                    otro.obtener_cupo_maximo() == nuevo_cupo_maximo and
                    otro.obtener_cupo_actual() == nuevo_cupo_actual):
                    raise Exception("Ya existe un paquete grupal con esos datos (duplicado)")

        paquete_grupal.establecer_fecha_salida(nuevo_fecha_salida)
        paquete_grupal.establecer_fecha_vuelta(nuevo_fecha_vuelta)
        paquete_grupal.establecer_descripcion(nuevo_descripcion)
        paquete_grupal.establecer_tipo(nuevo_tipo)
        paquete_grupal.establecer_transporte(nuevo_transporte)
        paquete_grupal.establecer_precio(nuevo_precio)
        paquete_grupal.establecer_ciudad(nuevo_ciudad)
        paquete_grupal.establecer_hotel(nuevo_hotel)
        paquete_grupal.establecer_cupo_maximo(nuevo_cupo_maximo)
        paquete_grupal.establecer_cupo_actual(nuevo_cupo_actual)

        self.__guardar_en_archivo()
        return True