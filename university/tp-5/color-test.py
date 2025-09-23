from color import Color

class Test:
    @staticmethod
    def ejecutar():
        try:
            color1 = Color()
            color2 = Color(100, 150, 250)

            print(f"Rojo: {color1.obtener_rojo()}")
            print(f"Verde: {color1.obtener_verde()}")
            print(f"Azul: {color1.obtener_azul()}")

            print(f"Rojo: {color2.obtener_rojo()}")
            print(f"Verde: {color2.obtener_verde()}")
            print(f"Azul: {color2.obtener_azul()}")

            color1.variar(25)
            color2.variar(25)

            print(f"Rojo: {color1.obtener_rojo()}")
            print(f"Verde: {color1.obtener_verde()}")
            print(f"Azul: {color1.obtener_azul()}")

            print(f"Rojo: {color2.obtener_rojo()}")
            print(f"Verde: {color2.obtener_verde()}")
            print(f"Azul: {color2.obtener_azul()}")

            color2.variar_rojo(5)
            color2.variar_verde(5)
            color2.variar_azul(5)

            print(f"Rojo: {color2.obtener_rojo()}")
            print(f"Verde: {color2.obtener_verde()}")
            print(f"Azul: {color2.obtener_azul()}")

            color2.establecer_rojo(100)
            color2.establecer_verde(100)
            color2.establecer_azul(100)

            print(f"Rojo: {color2.obtener_rojo()}")
            print(f"Verde: {color2.obtener_verde()}")
            print(f"Azul: {color2.obtener_azul()}")

            color2.copiar(color1)
            print(f"Rojo: {color2.obtener_rojo()}")
            print(f"Verde: {color2.obtener_verde()}")
            print(f"Azul: {color2.obtener_azul()}")

            if color2.es_rojo():
                print("Color 2 es rojo")
            else:
                print("Color 2 NO es rojo")

            color2.establecer_rojo(255)
            color2.establecer_verde(0)
            color2.establecer_azul(0)

            if color2.es_rojo():
                print("Color 2 es rojo")
            else:
                print("Color 2 NO es rojo")

            if color2.es_gris():
                print("Color 2 es es gris")
            else:
                print("Color 2 NO es es gris")

            color2.establecer_rojo(50)
            color2.establecer_verde(50)
            color2.establecer_azul(50)

            if color2.es_gris():
                print("Color 2 es gris")
            else:
                print("Color 2 NO es gris")

            if color2.es_negro():
                print("Color 2 es negro")
            else:
                print("Color 2 NO es negro")

            color2.establecer_rojo(0)
            color2.establecer_verde(0)
            color2.establecer_azul(0)

            if color2.es_negro():
                print("Color 2 es ngro")
            else:
                print("Color 2 NO es negro")

            nuevo_color = color1.complemento()
            print(f"Rojo complemento: {nuevo_color.obtener_rojo()}")
            print(f"Verde complemneto: {nuevo_color.obtener_verde()}")
            print(f"Azul complemento: {nuevo_color.obtener_azul()}")

            print(f"Rojo: {color1.obtener_rojo()}")
            print(f"Verde: {color1.obtener_verde()}")
            print(f"Azul: {color1.obtener_azul()}")

            if color1.es_igual_que(color2):
                print("Los colores 1 y 2 son iguales")
            else:
                print("Los colores 1 y 2 NO son iguales")

            color3 = Color()
            color4 = Color()

            if color3.es_igual_que(color4):
                print("Los colores 3 y 4 son iguales")
            else:
                print("Los colores 3 y 4 NO son iguales")

            clon_color3 = color3.clonar()
            print(f"Rojo: {clon_color3.obtener_rojo()}")
            print(f"Verde: {clon_color3.obtener_verde()}")
            print(f"Azul: {clon_color3.obtener_azul()}")

        except ValueError as e:
            print(f"{e}")
        except TypeError as e:
            print(f"{e}")

if __name__ == "__main__":
    Test.ejecutar()
