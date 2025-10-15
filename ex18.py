class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Brincando com {self.nome}!")


class BuzzLightyear(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está voando para o infinito e além!")


class Woody(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está laçando com sua corda!")


class Rex(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está rugindo alto!")


class Barbie(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está desfilando na passarela!")


class SrCabeçaDeBatata(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está trocando suas partes divertidas!")


tipo = input("Digite o tipo de brinquedo (buzz/woody/rex/barbie/srbatata/outro): ").strip().lower()
nome = input("Nome do brinquedo: ")
cor = input("Cor: ")
tamanho = input("Tamanho: ")
preco = float(input("Preço: "))

match tipo:
    case "buzz":
        brinquedo = BuzzLightyear(nome, cor, tamanho, preco)
    case "woody":
        brinquedo = Woody(nome, cor, tamanho, preco)
    case "rex":
        brinquedo = Rex(nome, cor, tamanho, preco)
    case "barbie":
        brinquedo = Barbie(nome, cor, tamanho, preco)
    case "srbatata":
        brinquedo = SrCabeçaDeBatata(nome, cor, tamanho, preco)
    case _:
        brinquedo = Brinquedo(nome, cor, tamanho, preco)

brinquedo.brincar()
