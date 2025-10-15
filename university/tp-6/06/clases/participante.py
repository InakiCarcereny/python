from disciplinas import Disciplinas

class Participante:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre tiene que tener un valor")

        if not isinstance(edad, int):
            raise TypeError("Edad tiene que ser un numero entero")
        if edad <= 0:
            raise ValueError("Edad tiene que ser un numero positivo")
        
        if not isinstance(nacionalidad, str):
            raise TypeError("Nacionalidad tiene que ser un string")
        if nacionalidad == "" or nacionalidad.isspace():
            raise ValueError("Nacionalidad tiene que tener un valor")

        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad 
        self.__disciplinas: list[Disciplinas] = []
    
    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_edad(self) -> int:
        return self.__edad
    
    def obtener_nacionalidad(self) -> str:
        return self.__nacionalidad
    
    def obtener_disciplinas(self):
        for dis in self.__disciplinas:
            print(dis)

    def establecer_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("Nombre tiene que ser un string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre tiene que tener un valor")

        self.__nombre = nombre

    def establecer_edad(self, edad: int):
        if not isinstance(edad, int):
            raise TypeError("Edad tiene que ser un numero entero")
        if edad <= 0:
            raise ValueError("Edad tiene que ser un numero positivo")

        self.__edad = edad

    def establecer_nacionalidad(self, nacionalidad: str):
        if not isinstance(nacionalidad, str):
            raise TypeError("Nacionalidad tiene que ser un string")
        if nacionalidad == "" or nacionalidad.isspace():
            raise ValueError("Nacionalidad tiene que tener un valor")
      
        self.__nacionalidad = nacionalidad

    def agregar_disciplina(self, disciplina: Disciplinas):
        if not isinstance(disciplina, Disciplinas):
            raise TypeError("Disciplina tiene que ser una instancia de la clase Disciplina")

        if disciplina not in self.__disciplinas:
            self.__disciplinas.append(disciplina)
        else:
            raise ValueError("Esa disciplina ya se encuentra")