from departamentoClase import Departamento
from inmobiliaria import Inmobiliaria
from inmuebleClase import Inmueble_clase
from propietario import Propietario
from quintaClase import Quinta

class Test:
  @staticmethod
  def ejecutar():
      p1 = Propietario("Inaki", 46697629)
      p2 = Propietario("Luca", 46895678)

      print(p1)
      print("-----------------------------")
      print(p2)
      print("-----------------------------")

      inmueble1 = Inmueble_clase(1111, "Martin 245", 50, 1)
      inmueble2 = Inmueble_clase(2222, "Zapiola 796", 35, 2)

      inmueble1.establecer_propietario(p1)
      inmueble2.establecer_propietario(p2)

      print(inmueble1)
      print("-----------------------------")
      print(inmueble2)
      print("-----------------------------")

      print(f"Precio venta inmueble 1: {inmueble1.precio_venta(15)}")
      print("-----------------------------")
      print(f"Precio venta inmueble 2: {inmueble2.precio_venta(45)}")
      print("-----------------------------")

      print(f"Costo alquiler inmueble 1: {inmueble1.costo_alquiler(150)}")
      print("-----------------------------")
      print(f"Cosot alquiler inmueble 2: {inmueble2.costo_alquiler(150)}")
      print("-----------------------------")

      departamento1 = Departamento(3333, "Las heras 123", 65, 3, 1000, True)
      departamento2 = Departamento(4444, "Dorrego 456", 45, 4, 800, False)

      departamento1.establecer_propietario(p1)

      print(departamento1)
      print("-----------------------------")
      print(departamento2)
      print("-----------------------------")

      print(f"Precio venta departamento 1: {departamento1.precio_venta(15)}")
      print("-----------------------------")
      print(f"Precio venta departamento 2: {departamento2.precio_venta(45)}")
      print("-----------------------------")

      print(f"Costo alquiler departamento 1: {departamento1.costo_alquiler(150)}")
      print("-----------------------------")
      print(f"Cosot alquiler departamento 2: {departamento2.costo_alquiler(150)}")
      print("-----------------------------")     

      quinta1 = Quinta(5555, "Gabril 687", 100, 5, 50)
      quinta2 = Quinta(6666, "Alem 589", 50, 6, 50)

      quinta2.establecer_propietario(p1)

      print(quinta1)
      print("-----------------------------")
      print(quinta2)
      print("-----------------------------")

      print(f"Precio venta quinta 1: {quinta1.precio_venta(15)}")
      print("-----------------------------")
      print(f"Precio venta quinta 2: {quinta2.precio_venta(45)}")
      print("-----------------------------")

      print(f"Costo alquiler quinta 1: {quinta1.costo_alquiler(150)}")
      print("-----------------------------")
      print(f"Cosot alquiler quinta 2: {quinta2.costo_alquiler(150)}")
      print("-----------------------------")

      inmobiliaria1 = Inmobiliaria()
      inmobiliaria2 = Inmobiliaria()

      inmobiliaria1.insertar(inmueble1)
      inmobiliaria1.insertar(departamento1)
      inmobiliaria1.insertar(quinta1)  

      for inmobiliaria in inmobiliaria1.obtener_inmuebles():
        print(f"{inmobiliaria} tiene la inmobiliaria 1")
      print("-----------------------------")

      inmobiliaria2.insertar(inmueble2)

      for inmo in inmobiliaria2.obtener_inmuebles():
        print(f"{inmo} tiene la inmobiliaria 2")
      print("-----------------------------")

      print("Encontrar inmueble con codigo")
      if inmobiliaria1.esta_inmueble_codigo(1111):
        print("Ese inmueble se encuentra en la lista de la inmobiliaria 1")
      else:
        print("Ese inmueble NO se encuentra en la lista de la inmobiliaria 1")

      print("Encontrar inmueble con objeto")
      if inmobiliaria1.esta_inmueble(departamento1):
        print("Ese inmueble se encuentra en la lista de la inmobiliaria 1")
      else:
        print("Ese inmueble NO se encuentra en la lista de la inmobiliaria 1")

      if inmobiliaria1.hay_inmuebles():
        print("Tiene inmuebles")
      else:
        print("NO tiene inmuebles")

      print(f"Cantidad: {inmobiliaria1.contar_propiedades_mas_metros(100)}")

      print(f"El inmueble con mayor precio de venta es: {inmobiliaria1.mayor_precio_venta()}")

if __name__ == "__main__":
    Test.ejecutar()


      