import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def imprimir_raio(self):
        print(f"Raio: {self.raio}")

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_circunferencia(self):
        return 2 * math.pi * self.raio



raio = float(input("Digite o raio do círculo: "))


c = Circulo(raio)


c.imprimir_raio()
print(f"Área: {c.calcular_area():.2f}")
print(f"Circunferência: {c.calcular_circunferencia():.2f}")
