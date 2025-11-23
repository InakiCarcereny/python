from modelos.repositorios.repositorio_polizas import RepositorioPolizas

repositorio_polizas = None

def obtener_repositorio_polizas():
    global repositorio_polizas

    if repositorio_polizas is None:
        repositorio_polizas = RepositorioPolizas()

    return repositorio_polizas