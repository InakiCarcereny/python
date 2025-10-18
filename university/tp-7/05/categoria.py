class Categoria():
    def __init__(self, nombre: str, apellido: str, dni: int):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

    def establecer_nombre(self, nombre: str):
        self._nombre = nombre

    def establecer_apellido(self, apellido: str):
        self._apellido = apellido

    def establecer_dni(self, dni: int):
        self._dni = dni

    def obtener_nombre(self) -> str:
        return self._nombre
    
    def obtener_apellido(self) -> str:
        return self._apellido
    
    def obtener_dni(self) -> int:
        return self._dni