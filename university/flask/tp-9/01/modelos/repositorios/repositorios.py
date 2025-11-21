from modelos.repositorios.repositorio_libros import RepositorioLibro

repositorio_libros = None

def obtener_repositorio_libros():
    global repositorio_libros

    if repositorio_libros is None:
        repositorio_libros = RepositorioLibro()

    return repositorio_libros