class Conta:
    def __init__(self, nome, cpf, numero, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def imprimir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")



nome = input("Digite o nome do titular: ")
cpf = input("Digite o CPF: ")
numero = input("Digite o número da conta: ")


conta = Conta(nome, cpf, numero)


conta.imprimir_saldo()


valor_deposito = float(input("Digite o valor para depósito: "))
conta.depositar(valor_deposito)
conta.imprimir_saldo()


valor_saque = float(input("Digite o valor para saque: "))
conta.sacar(valor_saque)
conta.imprimir_saldo()
