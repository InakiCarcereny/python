from modelos.repositorios.repositorio_socios import RepositorioSocio

repositorio_socios = None

def obtener_repositorio_socios():
    global repositorio_socios

    if repositorio_socios is None:
        repositorio_socios = RepositorioSocio()

    return repositorio_socios