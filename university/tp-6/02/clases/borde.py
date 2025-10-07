from colorb import Color

class Borde:
    def __init__(self, grosor: int, color: Color):
        if not isinstance(grosor, int):
            raise TypeError("Grosor tiene que ser un numero")
        if grosor < 0:
            raise ValueError("Grosor tiene que ser un numero positivo")

        if not isinstance(color, Color):
            raise TypeError("Color tiene que ser una instancia de Color")

        self.__grosor = grosor
        self.__color = color

    """COMANDOS"""

    def copiar_valores(self, borde: 'Borde'):
        if not isinstance(borde, Borde):
            raise TypeError("Borde tiene que ser una instancia de Borde")

        self.__grosor = borde.obtener_grosor()
        self.__color = borde.obtener_color()

    """CONSULTAS"""

    def obtener_grosor(self) -> int:
        return self.__grosor

    def obtener_color(self) -> Color:
        return self.__color
 
    def clonar(self) -> 'Borde':
        return Borde(self.__grosor, self.__color)

    def es_igual_que(self, borde: 'Borde') -> bool:
        if not isinstance(borde, Borde):
            raise TypeError("Borde tiene que ser una instancia de Borde")

        return (self.__grosor, self.__color) == (borde.obtener_grosor(), borde.obtener_color())

