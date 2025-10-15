class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")


class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Limite insuficiente!")


class ContaPoupanca(ContaBancaria):
    def render_juros(self, taxa):
        self.saldo += self.saldo * (taxa / 100)


tipo = input("Digite o tipo de conta (bancaria/corrente/poupanca): ").strip().lower()
titular = input("Nome do titular: ")
saldo = float(input("Saldo inicial: "))

match tipo:
    case "bancaria":
        conta = ContaBancaria(titular, saldo)
    case "corrente":
        limite = float(input("Limite da conta corrente: "))
        conta = ContaCorrente(titular, saldo, limite)
    case "poupanca":
        conta = ContaPoupanca(titular, saldo)
    case _:
        print("Tipo de conta inválido.")
        conta = ContaBancaria(titular, saldo)

acao = input("Deseja depositar, sacar ou render juros? ").strip().lower()

match acao:
    case "depositar":
        valor = float(input("Valor a depositar: "))
        conta.depositar(valor)
    case "sacar":
        valor = float(input("Valor a sacar: "))
        conta.sacar(valor)
    case "render juros":
        if isinstance(conta, ContaPoupanca):
            taxa = float(input("Taxa de juros (%): "))
            conta.render_juros(taxa)
        else:
            print("Apenas contas poupança podem render juros.")

print(f"Saldo final: R$ {conta.saldo:.2f}")
