class PessoaBase:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está negociando...")


class PessoaFisica(PessoaBase):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def apresentar_documento(self):
        print(f"CPF: {self.cpf}")


class PessoaJuridica(PessoaBase):
    def __init__(self, nome, telefone, email, endereco, cnpj, razao_social):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.razao_social = razao_social

    def apresentar_razao_social(self):
        print(f"Razão Social: {self.razao_social} - CNPJ: {self.cnpj}")


tipo = input("Digite o tipo de pessoa (fisica/juridica): ").strip().lower()

match tipo:
    case "fisica":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        endereco = input("Endereço: ")
        cpf = input("CPF: ")
        pessoa = PessoaFisica(nome, telefone, email, endereco, cpf)
        pessoa.negociar()
        pessoa.apresentar_documento()
    case "juridica":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        endereco = input("Endereço: ")
        cnpj = input("CNPJ: ")
        razao_social = input("Razão Social: ")
        pessoa = PessoaJuridica(nome, telefone, email, endereco, cnpj, razao_social)
        pessoa.negociar()
        pessoa.apresentar_razao_social()
    case _:
        print("Tipo inválido.")
