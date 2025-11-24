from modelos.repositorios.repositorio_ciudades import RepositorioCiudad
from modelos.repositorios.repositorio_hoteles import RepositorioHotel
from modelos.repositorios.repositorio_paquetesGrupales import RepositorioPaqueteGrupal

repositorio_ciudades = None
repositorio_hoteles = None
repositorio_paquetes_grupales = None

def obtener_repositorio_ciudades():
    global repositorio_ciudades, repositorio_hoteles, repositorio_paquetes_grupales

    if repositorio_ciudades is None:
        repositorio_ciudades = RepositorioCiudad()

    if repositorio_hoteles is not None:
        repositorio_ciudades.set_repo_hoteles(repositorio_hoteles)

    if repositorio_paquetes_grupales is not None:
        repositorio_ciudades.set_repo_paquetes_grupales(repositorio_paquetes_grupales)

    return repositorio_ciudades

def obtener_repositorio_hoteles():
    global repositorio_hoteles, repositorio_ciudades, repositorio_paquetes_grupales

    if repositorio_hoteles is None:
        repositorio_hoteles = RepositorioHotel()

    if repositorio_ciudades is not None:
        repositorio_ciudades.set_repo_hoteles(repositorio_hoteles)

    if repositorio_paquetes_grupales is not None:
        repositorio_hoteles.set_repo_paquetes(repositorio_paquetes_grupales)

    return repositorio_hoteles

def obtener_repositorio_paquetes_grupales():
    global repositorio_paquetes_grupales

    if repositorio_paquetes_grupales is None:
        repositorio_paquetes_grupales = RepositorioPaqueteGrupal()

    return repositorio_paquetes_grupales