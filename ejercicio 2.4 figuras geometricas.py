import math

class Figura:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def determinar_tipo_triangulo(self):
        lados = [self.base, self.altura, self.calcular_hipotenusa()]
        lados = [round(l, 5) for l in lados]
        unicos = len(set(lados))
        if unicos == 1:
            return "Equilatero"
        elif unicos == 2:
            return "Isosceles"
        else:
            return "Escaleno"

class Rombo(Figura):
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, lado1, lado2, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

# Clase de prueba
if __name__ == "__main__":
    figuras = [
        Circulo(5),
        Rectangulo(4, 6),
        Cuadrado(3),
        TrianguloRectangulo(3, 4),
        Rombo(8, 6, 5),
        Trapecio(10, 6, 4, 4, 5)
    ]

    for figura in figuras:
        print("-------------------------")
        print(f"Figura: {figura.__class__.__name__}")
        print(f"Área: {figura.calcular_area():.2f}")
        print(f"Perímetro: {figura.calcular_perimetro():.2f}")
        if isinstance(figura, TrianguloRectangulo):
            print(f"Hipotenusa: {figura.calcular_hipotenusa():.2f}")
            print(f"Tipo: {figura.determinar_tipo_triangulo()}")
