from clases.borde import Borde
from clases.colorb import Color

class Test:
    @staticmethod
    def ejecutar():
        C1 = Color(150, 150, 150)
        C2 = Color(150, 150, 150)
        B1 = Borde(1,C1)
        B2 = Borde(1,C2)
        B3 = B2.clonar()
        B4 = Borde(B2.obtener_grosor(), B2.obtener_color())
        print( B2 == B3)
        print( B2 == B4)
        print(B2.es_igual_que(B1))
        print(B2.es_igual_que(B3))
        print(B2.obtener_grosor() == B1.obtener_grosor() and
        B2.obtener_color() == B1.obtener_color())
        print(B2.obtener_grosor() == B3.obtener_grosor() and
        B2.obtener_color() == B3.obtener_color())
        print(B2.obtener_grosor() == B1.obtener_grosor() and
        B2.obtener_color().es_igual_que(B1.obtener_color()))
        print(B2.obtener_grosor() == B4.obtener_grosor() and
        B2.obtener_color().es_igual_que(B4.obtener_color()))

if __name__ == "__main__":
    Test.ejecutar()

