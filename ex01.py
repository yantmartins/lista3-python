class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_nome(self):
        print(f"Nome: {self.nome}")

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def imprimir_endereco(self):
        print(f"Endereço: {self.endereco}")




# --- Parte que usa a classe ---
# Recebendo dados do usuário
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
endereco = input("Digite o endereço: ")


p = Pessoa(nome, idade, endereco)


p.mostrar_nome()
p.imprimir_endereco()


nova_idade = int(input("Digite a nova idade: "))
p.alterar_idade(nova_idade)

print(f"Idade atualizada: {p.idade}")
