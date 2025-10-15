class Imovel:
    def __init__(self, inscricao, valor_aluguel, iptu):
        self.inscricao = inscricao
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_iptu(self):
        return self.iptu / 12

    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor


class Casa(Imovel):
    def __init__(self, inscricao, valor_aluguel, iptu, piscina, quartos, churrasqueira):
        super().__init__(inscricao, valor_aluguel, iptu)
        self.piscina = piscina
        self.quartos = quartos
        self.churrasqueira = churrasqueira


class Apartamento(Imovel):
    def __init__(self, inscricao, valor_aluguel, iptu, andar, elevador):
        super().__init__(inscricao, valor_aluguel, iptu)
        self.andar = andar
        self.elevador = elevador


class Terreno(Imovel):
    def __init__(self, inscricao, valor_aluguel, iptu, area_m2):
        super().__init__(inscricao, valor_aluguel, iptu)
        self.area_m2 = area_m2


class Chacara(Imovel):
    def __init__(self, inscricao, valor_aluguel, iptu, area_lazer):
        super().__init__(inscricao, valor_aluguel, iptu)
        self.area_lazer = area_lazer


tipo = input("Digite o tipo de imóvel (casa/apartamento/terreno/chacara/outro): ").strip().lower()
inscricao = input("Inscrição do imóvel: ")
valor_aluguel = float(input("Valor do aluguel: "))
iptu = float(input("Valor do IPTU: "))

match tipo:
    case "casa":
        piscina = input("Possui piscina? (s/n): ").strip().lower() == "s"
        quartos = int(input("Quantidade de quartos: "))
        churrasqueira = input("Possui churrasqueira? (s/n): ").strip().lower() == "s"
        imovel = Casa(inscricao, valor_aluguel, iptu, piscina, quartos, churrasqueira)
    case "apartamento":
        andar = int(input("Número do andar: "))
        elevador = input("Possui elevador? (s/n): ").strip().lower() == "s"
        imovel = Apartamento(inscricao, valor_aluguel, iptu, andar, elevador)
    case "terreno":
        area_m2 = float(input("Área em m²: "))
        imovel = Terreno(inscricao, valor_aluguel, iptu, area_m2)
    case "chacara":
        area_lazer = float(input("Área de lazer em m²: "))
        imovel = Chacara(inscricao, valor_aluguel, iptu, area_lazer)
    case _:
        imovel = Imovel(inscricao, valor_aluguel, iptu)

print(f"Parcela do IPTU: R$ {imovel.obter_parcela_iptu():.2f}")
print(f"Valor do aluguel: R$ {imovel.valor_aluguel:.2f}")
