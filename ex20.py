class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        return self.valor_total


class CompraAvista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def calcular_valor_total(self):
        total = super().calcular_valor_total()
        total -= self.desconto
        return total


class CompraParcelada(Compra):
    def __init__(self, numero, produto, valor, parcelas):
        super().__init__(numero, produto, valor)
        self.parcelas = parcelas

    def simular_numero_de_parcelas(self):
        total = super().calcular_valor_total()
        valor_parcela = total / self.parcelas
        print(f"{self.parcelas}x de R$ {valor_parcela:.2f}")


tipo = input("Digite o tipo de compra (avista/parcelada): ").strip().lower()
numero = input("Número da compra: ")
produto = input("Produto: ")
valor = float(input("Valor do produto: "))

match tipo:
    case "avista":
        desconto = float(input("Desconto: "))
        compra = CompraAvista(numero, produto, valor, desconto)
        print(f"Valor total à vista: R$ {compra.calcular_valor_total():.2f}")
    case "parcelada":
        parcelas = int(input("Número de parcelas: "))
        compra = CompraParcelada(numero, produto, valor, parcelas)
        compra.simular_numero_de_parcelas()
        print(f"Valor total parcelado: R$ {compra.calcular_valor_total():.2f}")
    case _:
        compra = Compra(numero, produto, valor)
        print(f"Valor total: R$ {compra.calcular_valor_total():.2f}")
