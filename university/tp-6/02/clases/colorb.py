class Color:
    __MIN_VALOR: int = 0
    __MAX_VALOR: int = 255

    def __init__(self, rojo: int | None = None, verde: int | None = None, azul: int | None = None):
        self.__rojo = rojo if rojo is not None else Color.__MAX_VALOR
        self.__verde = verde if verde is not None else Color.__MAX_VALOR
        self.__azul = azul if azul is not None else Color.__MAX_VALOR

    """COMANDOS"""
    def variar(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("El valor tiene que ser un numero")
        if valor < 0 or valor > 255:
            raise ValueError("EL valor tiene que ser un numero mayor a 0 y menor a 255")

        calcular_rojo = self.__rojo + valor
        calcular_azul = self.__azul + valor
        calcular_verde = self.__verde + valor

        if calcular_rojo > 255:
            self.__rojo = 255
        else:
            self.__rojo = calcular_rojo

        if calcular_azul > 255:
            self.__azul = 255
        else: 
            self.__azul = calcular_azul

        if calcular_verde > 255:
            self.__verde = 255
        else:
            self.__verde = calcular_verde

    def variar_rojo(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("El valor tiene que ser un numero")
        if valor < 0 or valor > 255:
            raise ValueError("El valor tiene que ser un numero mayor a 0 y menor a 255")

        calcular_rojo = self.__rojo + valor

        if calcular_rojo > 255:
            self.__rojo = 255
        else:
            self.__rojo = calcular_rojo

    def variar_azul(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("El valor tiene que ser un numero positivo")
        if valor < 0 or valor > 255:
            raise ValueError("El valor tiene que ser un numero maoyor a 0 y menor a 255")

        calcular_azul = self.__azul + valor

        if calcular_azul > 255:
            self.__azul = 255
        else:
            self.__azul = calcular_azul

    def variar_verde(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("El valor tiene que ser un numero positivo")
        if valor < 0 or valor > 255:
            ("El valor tiene que ser un numero mayor a 0 y menor a 255")

        calcular_verde = self.__verde + valor

        if calcular_verde > 255:
            self.__verde = 255
        else:
            self.__verde = calcular_verde

    def establecer_rojo(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("El valor tiene que ser un numero positivo")
        if valor < 0 or valor > 255:
            ("El valor tiene que ser un numero mayor a 0 y menor a 255")

        self.__rojo = valor

    def establecer_azul(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("El valor tiene que ser un numero positivo")
        if valor < 0 or valor > 255:
            ("El valor tiene que ser un numero mayor a 0 y menor a 255")

        self.__azul = valor

    def establecer_verde(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("El valor tiene que ser un numero positivo")
        if valor < 0 or valor > 255:
            ("El valor tiene que ser un numero mayor a 0 y menor a 255")

        self.__verde = valor

    def copiar(self, otro_color: 'Color'):
        self.__rojo = otro_color.__rojo
        self.__verde = otro_color.__verde
        self.__azul = otro_color.__azul

    """CONSULTAS"""
    def obtener_rojo(self) -> int:
        return self.__rojo

    def obtener_azul(self) -> int:
        return self.__azul

    def obtener_verde(self) -> int:
        return self.__verde

    def es_rojo(self) -> bool:
        if self.__rojo == 255 and self.__verde == 0 and self.__azul == 0:
            return True
        else:
            return False

    def es_gris(self) -> bool:
        if self.__rojo == 50 and self.__verde == 50 and self.__azul == 50:
            return True
        else:
            return False

    def es_negro(self) -> bool:
        if self.__rojo == 0 and self.__verde == 0 and self.__azul == 0:
            return True
        else:
            return False

    def complemento(self) -> 'Color':
        return Color(255 - self.__rojo, 255 - self.__verde, 255 - self.__azul)

    def es_igual_que(self, otro_color: 'Color') -> bool:
        return (self.__rojo, self.__verde, self.__azul) == (otro_color.__rojo, otro_color.__verde, otro_color.__azul)

    def clonar(self) -> 'Color':
        return Color(self.__rojo, self.__azul, self.__verde)




