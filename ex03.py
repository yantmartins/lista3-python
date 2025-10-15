class Aluno:
    def __init__(self, nome, ra, n1, n2, n3, n4):
        self.nome = nome
        self.ra = ra
        self.notas = [n1, n2, n3, n4]

    def mostrar_situacao(self):
        media = sum(self.notas) / len(self.notas)
        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Exame"
        else:
            situacao = "Reprovado"
        print(f"Aluno {self.nome} - Média {media:.1f} - {situacao}")



nome = input("Digite o nome do aluno: ")
ra = input("Digite o RA do aluno: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))


aluno = Aluno(nome, ra, n1, n2, n3, n4)


aluno.mostrar_situacao()
