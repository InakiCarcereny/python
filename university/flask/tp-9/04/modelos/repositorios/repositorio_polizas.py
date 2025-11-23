from modelos.entidades.polizaInmueble import PolizaInmueble
from modelos.entidades.polizaInmuebleEscolar import PolizaInmuebleEscolar
import json

class RepositorioPolizas:
    __RUTA_ARCHIVO = 'datos/polizas.json'

    def __init__(self):
        self.__polizas: list[PolizaInmueble | PolizaInmuebleEscolar] = []
        self.__cargar_desde_archivo()

    def __cargar_desde_archivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding = 'utf-8') as archivo:
                datos = json.load(archivo)

                for poliza_diccionario in datos:
                    if 'cant_personas' in poliza_diccionario:
                        p = PolizaInmuebleEscolar.from_diccionario(poliza_diccionario)
                    else:
                        p = PolizaInmueble.from_diccionario(poliza_diccionario)

                    self.__polizas.append(p)
        
        except Exception as e:
            print(f"Error al cargar desde archivo: {e}")

    def __guardar_en_archivo(self):
        lista_polizas_diccionario = [poliza.to_diccionario() for poliza in self.__polizas]

        datos_a_guardar = {
            'polizas': lista_polizas_diccionario
        }

        try:
            with open(self.__RUTA_ARCHIVO, 'w', encoding = 'utf-8') as archivo:
                json.dump(datos_a_guardar, archivo, indent = 4, ensure_ascii = False)

        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

    def existe_poliza(self, poliza: PolizaInmueble | PolizaInmuebleEscolar) -> bool:
        for p in self.__polizas:
            if p == poliza:
                return True
            
        return False
    
    def existe_poliza_numero(self, numero: int) -> bool:
        for p in self.__polizas:
            if p.obtener_numero() == numero:
                return True
            
        return False
    
    def ingresos_mensuales(self) -> int | float:
        suma = 0

        for p in self.__polizas:
            suma = suma + p.valor_mensual_poliza()

        return suma

    # PETICION GET ALL
    def obtener_polizas(self) -> list[PolizaInmueble | PolizaInmuebleEscolar]:
        return self.__polizas
    
    # PETICION GET BY NUMERO
    def obtener_poliza(self, numero: int) -> PolizaInmueble | PolizaInmuebleEscolar | None:
        for p in self.__polizas:
            if p.obtener_numero() == numero:
                return p
            
        return None
    
    # PETICION POST
    def agregar_poliza(self, poliza: PolizaInmueble | PolizaInmuebleEscolar) -> bool:
        if not isinstance(poliza, (PolizaInmueble, PolizaInmuebleEscolar)):
            raise TypeError("Poliza tiene que ser una instancia de PolizaInmueble o de PolizaInmuebleEscolar")
        
        if not self.existe_poliza_numero(poliza.obtener_numero()):
            self.__polizas.append(poliza)
            self.__guardar_en_archivo()
            return True
        
        return False
    
    # PETICION DELETE
    def elimiar_poliza(self, numero: int) -> bool:
        for p in self.__polizas:
            if p.obtener_numero() == numero:
                self.__polizas.remove(p)
                self.__guardar_en_archivo()
                return True
            
        return False
    
    # PETICION PUT
    def actualizar_poliza(self, numero: int, data: dict) -> bool:
        poliza = self.obtener_poliza(numero)

        if poliza is not None:
            if isinstance(poliza, PolizaInmuebleEscolar):
                if 'cant_personas' in data:
                    nueva_cant_personas = data['cant_personas']

                    if not isinstance(nueva_cant_personas, int):
                        raise TypeError("Nueva cantidad personas tiene que ser un numero entero")
                    if nueva_cant_personas < 0:
                        raise ValueError("Nueva cantidad personas tiene que ser positivo")
                    
                    poliza.establecer_cant_personas(nueva_cant_personas)

                if 'monto_equipamiento' in data:
                    nuevo_monto_equipamiento = data['monto_equipamiento']

                    if not isinstance(nuevo_monto_equipamiento, (int, float)):
                        raise TypeError("Nuevo monto equipamiento tiene que ser un numero entero o con decimales")
                    if nuevo_monto_equipamiento < 0:
                        raise ValueError("Nuevo monto equipamiento tiene que ser positivo")
                    
                    poliza.establecer_monto_equipamiento(nuevo_monto_equipamiento)
                    
                if 'monto_mobiliario' in data:  
                    nuevo_monto_mobiliario = data['monto_mobiliario']

                    if not isinstance(nuevo_monto_mobiliario, (int, float)):
                        raise TypeError("Nuevo monto mobiliario tiene que ser un numero entero o con decimales")
                    if nuevo_monto_mobiliario < 0:
                        raise ValueError("Nuevo monto mobiliario tiene que ser positivo")
                    
                    poliza.establecer_monto_mobiliario(nuevo_monto_mobiliario)
                    
                if 'monto_persona' in data:
                    nuevo_monto_persona = data['monto_persona']

                    if not isinstance(nuevo_monto_persona, (int, float)):
                        raise TypeError("Nuevo monto persona tiene que ser un numero entero o con decimales")
                    if nuevo_monto_persona < 0:
                        raise ValueError("Nuevo monto persona tiene que ser positivo")
                    
                    poliza.establecer_monto_persona(nuevo_monto_persona)
                    
            if 'incendio' in data:
                nuevo_incendio = data['incendio']

                if not isinstance(nuevo_incendio, (int, float)):
                    raise TypeError("Nuevo incendio tiene que ser un numero entero o con decimales")
                if nuevo_incendio < 0:
                    raise ValueError("Nuevo incendio tiene que ser positivo")
                
                poliza.establecer_incendio(nuevo_incendio)
                
            if 'explosion' in data:
                nueva_explosion = data['explosion']

                if not isinstance(nueva_explosion, (int, float)):
                    raise TypeError("Nueva explosion tiene que ser un numero entero o con decimales")
                if nueva_explosion < 0:
                    raise ValueError("Nueva explosion tiene que ser positivo")
                
                poliza.establecer_explosion(nueva_explosion)
                
            if 'robo' in data:
                nuevo_robo = data['robo']

                if not isinstance(nuevo_robo, (int, float)):
                    raise TypeError("Nuevo robo tiene que ser un numero entero o con decimales")
                if nuevo_robo < 0:
                    raise ValueError("Nuevo robo tiene que ser positivo")
                
                poliza.establecer_robo(nuevo_robo)

            self.__guardar_en_archivo()
            return True
        
        return False






