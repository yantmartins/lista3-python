class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def obter_valor_mensalidade(self):
        if self.idade < 18:
            return self.mensalidade * 0.8  
        return self.mensalidade



nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

aluno = AlunoAcademia(nome, idade, peso, altura)


imc = aluno.calcular_imc()
print(f"\nAluno: {aluno.nome}")
print(f"IMC: {imc:.2f}")


mensalidade = aluno.obter_valor_mensalidade()
print(f"Mensalidade a pagar: R$ {mensalidade:.2f}")
