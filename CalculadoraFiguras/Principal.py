from Figuras import *


def pedir_int(mensaje):
        try:
            op = int(input(mensaje))
        except ValueError:
            op = None
        finally:
            return op



if __name__ == '__main__':

    while True:
        print("FIGURAS GEOMÉTRICAS\n", "1. Triángulo\n", "2. Rectángulo\n" " 3. Cuadrado\n" " 4. Pentágono\n", "0. Salir\n")
        opcion = pedir_int("***Escoja una opción***\n")#metodito para la opcion

        if opcion == 0:
            exit(0)
        elif opcion == 1:
            pedir_lado1 = float(input("Introduzca lado 1: "))
            pedir_lado2 = float(input("Introduzca lado 2: "))
            pedir_lado3 = float(input("Introduzca lado 3: "))
            pedir_altura = float(input("Introduzca altura: "))
            triangulo = Triangulo(pedir_lado1, pedir_lado2, pedir_lado3, pedir_altura)
            print(triangulo.calcular_area())
            print(triangulo.calcular_perimetro())

        elif opcion == 2:
            pedir_base = float(input("Introduzca la base: "))
            pedir_altura = float(input("Introduzca la altura: "))
            rectangulo = Rectangulo(pedir_base, pedir_altura)
            print("El área del rectángulo es: ",rectangulo.calcular_area())
            print("El perímetro del rectángulo es: ",rectangulo.calcular_perimetro())

        elif opcion == 3:
            pedir_apotema = float(input("Introduzca la base: "))
            pedir_lado = float(input("Introduzca el lado"))
            pentagono = Pentagono(pedir_apotema, pedir_lado)
            print("El perímetro del pentágono es: ",pentagono.calcular_perimetro())
            print("El área del pentágono es: ",pentagono.calcular_area())


        elif opcion == 4:
            pedir_cara = float(input("Introduzca un lado: "))
            cuadrado = Cuadrado(pedir_cara)
            print("El área del cuadrado es: ", cuadrado.calcular_area())
            print("El perímetro del cuadrado es",cuadrado.calcular_perimetro())













