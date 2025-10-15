class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def escolher_assento(self, novo_assento):
        self.assento = novo_assento


class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print(f"Ônibus {self.placa} está sendo abastecido!")


class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portao_embarque, checkin):
        super().__init__(preco, assento)
        self.portao_embarque = portao_embarque
        self.checkin = checkin

    def decolar(self):
        print(f"Avião decolando do portão {self.portao_embarque}!")


tipo = input("Digite o tipo de passagem (bus/aviao): ").strip().lower()

match tipo:
    case "bus":
        preco = float(input("Preço da passagem: "))
        assento = input("Assento: ")
        placa = input("Placa do ônibus: ")
        leito = input("É leito? (s/n): ").strip().lower() == "s"
        passagem = PassagemBus(preco, assento, placa, leito)
        passagem.abastecer()
    case "aviao":
        preco = float(input("Preço da passagem: "))
        assento = input("Assento: ")
        portao = input("Portão de embarque: ")
        checkin = input("Fez check-in? (s/n): ").strip().lower() == "s"
        passagem = PassagemAviao(preco, assento, portao, checkin)
        passagem.decolar()
    case _:
        print("Tipo de passagem inválido.")
