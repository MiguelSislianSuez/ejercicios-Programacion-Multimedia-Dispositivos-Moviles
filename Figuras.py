class FiguraGeometrica():
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass


class Triangulo(FiguraGeometrica):
    def __init__(self, l1, l2, l3, h):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.h = h

    def calcular_area(self):
        return print("El area es: ", (self.h * self.l1) / 2)  # ya se que no se peude concatenar

    def calcular_perimetro(self):
        return print("El perimetro es: ", self.l1 + self.l2 + self.l3)


class Rectangulo(FiguraGeometrica):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calcular_area(self):
        return self.b * self.h

    def calcular_perimetro(self):
        return (self.b * 2) + (self.h * 2)


class Pentagono(FiguraGeometrica):
    def __init__(self, a, l):
        self.a = a
        self.l = l

    def calcular_perimetro(self):
        self.p = self.l * 5
        return self.p

    def calcular_area(self):
        return (self.p * self.a) / 2


class Cuadrado(Rectangulo):
    def __init__(self, b):
        super().__init__(b, b)
