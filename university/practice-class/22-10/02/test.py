from cliente import Cliente
from compra import Compra
from consola import Consola
from juego_fisico import JuegoFisico   
from juego_digital import JuegoDigital
from items import Item
from datetime import datetime

class Tester:
    @staticmethod
    def test():
        separador = "="*60
        cliente1 = Cliente("Juan", "Perez", 123456, "juan.perez@mail.com")
        ps5 = Consola(1,700,"Sony", "PlayStation 5", 1024, 2, 10)
        xbox = Consola(2, 650, "Microsoft", "Xbox Series X", 1024, 2, 8)
        switch = Consola(3, 400, "Nintendo", "Switch", 512, 1, 15)
        theLastOfUs = JuegoFisico(4, 79.99, "The Last of Us Part II", "Acción/Aventura", 2020, "Un juego de acción y aventura post-apocalíptico.", True, 5)
        Hades = JuegoDigital(5, 24.99, "Hades", "Roguelike", 2020, "Un juego de acción roguelike ambientado en la mitología griega.", True, "PC", 15.5, "Supergiant Games")
        
        cod = JuegoDigital(6, 65.99, "Call of Duty: Modern Warfare 2", "Shooter", 2022, "Un juego de disparos en primera persona.", True, "Xbox", 20.0, "Activision")
        print("Datos iniciales:")
        print(cliente1)
        print(separador)
        print(ps5)
        print(separador)
        print(theLastOfUs)
        print(separador)
        print(Hades)
        print(separador)
        print(separador)
        print("Modificando stock y agregando consolas compatibles...")
        ps5.agregarStock(5)
        theLastOfUs.agregarStock(3)

        theLastOfUs.agregarConsolaCompatible(ps5)
        theLastOfUs.agregarConsolaCompatible(xbox)
        theLastOfUs.agregarConsolaCompatible(switch)
        Hades.agregarConsolaCompatible(ps5)
        Hades.agregarConsolaCompatible(xbox)

        print(ps5)
        print(separador)
        print(theLastOfUs)
        print(separador)
        print(Hades)
        print(separador)

        print(separador)
        print(separador)
        print("Realizando una compra...")

        compra = Compra(cliente1, datetime.now(), "Tarjeta de crédito")
        item1 = Item(theLastOfUs, 1)
        item2 = Item(Hades, 2)
        item3 = Item(ps5, 1)
        item4 = Item(cod, 1)

        compra.agregarItem(item1)
        compra.agregarItem(item2)
        compra.agregarItem(item3)
        compra.agregarItem(item4)

        print("Items en la compra:")
        for item in compra.obtenerItems():
            print(f"- {item} ")

        print(f"Total de la compra: {compra.calcularTotal()}")

        compra.entregar()
        print(f"Estado de la compra: {compra.obtenerEstado()}")

        print(separador)
        print(separador)
        print("Datos después de la compra:")

        print(ps5)
        print(separador)
        print(theLastOfUs)
        print(separador)
        print(Hades)
        print(separador)

if __name__ == "__main__":
    Tester.test()