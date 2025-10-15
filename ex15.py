class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def mostrar_setor(self):
        print(f"Setor: {self.setor}")


class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote=True, open_bar=False, open_food=False, estacionamento=True):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            print("Pegando bebida no open bar!")
        else:
            print("Sem open bar nesse ingresso.")

    def acessar_camarote(self):
        if self.camarote:
            print("Acesso liberado ao camarote!")
        else:
            print("Este ingresso não inclui camarote.")


tipo = input("Digite o tipo de ingresso (normal/vip): ").strip().lower()

match tipo:
    case "normal":
        preco = float(input("Preço do ingresso: "))
        setor = input("Setor: ")
        ingresso = Ingresso(preco, setor)
        ingresso.mostrar_setor()
    case "vip":
        preco = float(input("Preço do ingresso VIP: "))
        setor = input("Setor: ")
        open_bar = input("Inclui open bar? (s/n): ").strip().lower() == "s"
        open_food = input("Inclui open food? (s/n): ").strip().lower() == "s"
        camarote = input("Inclui camarote? (s/n): ").strip().lower() == "s"
        estacionamento = input("Inclui estacionamento? (s/n): ").strip().lower() == "s"
        ingresso = IngressoVIP(preco, setor, camarote, open_bar, open_food, estacionamento)
        ingresso.mostrar_setor()
        ingresso.acessar_camarote()
        ingresso.pegar_bebida()
    case _:
        print("Tipo de ingresso inválido.")
