class FuncionarioBase:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self):
        self.pontos.append(1)
        print(f"{self.nome} bateu o ponto! Total de pontos: {len(self.pontos)}")


class Vendedor(FuncionarioBase):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao

    def bater_meta(self, vendas):
        if vendas >= 10:
            print(f"{self.nome} bateu a meta! Comissão: R$ {self.comissao:.2f}")
        else:
            print(f"{self.nome} não atingiu a meta!")


class Gerente(FuncionarioBase):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def acessar_sistema(self, senha_digitada):
        if senha_digitada == self.senha:
            print(f"Acesso liberado para {self.nome}")
        else:
            print("Senha incorreta!")


tipo = input("Digite o tipo de funcionário (vendedor/gerente): ").strip().lower()

match tipo:
    case "vendedor":
        nome = input("Nome: ")
        matricula = input("Matrícula: ")
        salario = float(input("Salário: "))
        comissao = float(input("Comissão: "))
        vendedor = Vendedor(nome, matricula, salario, comissao)
        vendedor.bater_ponto()
        vendas = int(input("Quantidade de vendas realizadas: "))
        vendedor.bater_meta(vendas)
    case "gerente":
        nome = input("Nome: ")
        matricula = input("Matrícula: ")
        salario = float(input("Salário: "))
        senha = input("Senha: ")
        gerente = Gerente(nome, matricula, salario, senha)
        gerente.bater_ponto()
        senha_digitada = input("Digite a senha para acessar o sistema: ")
        gerente.acessar_sistema(senha_digitada)
    case _:
        print("Tipo de funcionário inválido.")
