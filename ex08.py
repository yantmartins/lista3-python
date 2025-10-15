import math

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.a = ladoA
        self.b = ladoB
        self.c = ladoC

    def validar(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def calcular_perimetro(self):
        return self.a + self.b + self.c

    def get_maior_lado(self):
        return max(self.a, self.b, self.c)

    def calcular_area(self):
        if not self.validar():
            raise ValueError("Lados não formam um triângulo válido.")
        s = self.calcular_perimetro() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))


tri = Triangulo(a, b, c)


if tri.validar():
    print("\nOs lados formam um triângulo válido!")
    print(f"Perímetro: {tri.calcular_perimetro():.2f}")
    print(f"Maior lado: {tri.get_maior_lado():.2f}")
    print(f"Área: {tri.calcular_area():.2f}")
else:
    print("\nOs lados informados não formam um triângulo válido.")
