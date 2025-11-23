from modelos.repositorios.repositorio_libros import RepositorioLibros
from modelos.repositorios.repositorio_socios import RepositorioSocios
from modelos.repositorios.repositorio_prestamos import RepositorioPrestamos

repositorio_libros = None
repositorio_socios = None
repositorio_prestamos = None

def obtener_repositorio_libros():
    global repositorio_libros

    if repositorio_libros is None:
        repositorio_libros = RepositorioLibros()
    
    return repositorio_libros

def obtener_repositorio_socios():
    global repositorio_socios

    if repositorio_socios is None:
        repositorio_socios = RepositorioSocios()

    return repositorio_socios

def obtener_repositorio_prestamos():
    global repositorio_prestamos

    if repositorio_prestamos is None:
        repositorio_prestamos = RepositorioPrestamos()

    return repositorio_prestamos