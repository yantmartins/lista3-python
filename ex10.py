class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo_km_por_litro, nivel=0.0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
        self.consumo = consumo_km_por_litro

    def abastecer(self, litros):
        self.nivel += litros

    def andar(self, distancia_km):
        litros_necessarios = distancia_km / self.consumo
        if litros_necessarios <= self.nivel:
            self.nivel -= litros_necessarios
        else:
            print("Combustível insuficiente! O carro só percorreu parte da distância.")
            self.nivel = 0

    def verificar_nivel(self):
        return self.nivel

    def calcular_imposto(self):
        return self.valor * 0.035



marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo: ")
cor = input("Digite a cor: ")
ano = int(input("Digite o ano: "))
valor = float(input("Digite o valor do carro: "))
consumo = float(input("Digite o consumo (km por litro): "))


carro = Carro(marca, modelo, cor, ano, valor, consumo)


litros = float(input("\nDigite a quantidade de litros para abastecer: "))
carro.abastecer(litros)
print(f"Nível de combustível: {carro.verificar_nivel():.2f} litros")

distancia = float(input("Digite a distância a percorrer (km): "))
carro.andar(distancia)
print(f"Nível de combustível após o trajeto: {carro.verificar_nivel():.2f} litros")


imposto = carro.calcular_imposto()
print(f"Imposto sobre o carro: R$ {imposto:.2f}")
