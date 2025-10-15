class PessoaBase:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade


class AlunoHeranca(PessoaBase):
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def estudar(self):
        print(f"{self.nome} está estudando.")


class Professor(PessoaBase):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self):
        print(f"{self.nome} está dando aula de {self.disciplina}.")


tipo = input("Digite o tipo de pessoa (aluno/professor): ").strip().lower()

match tipo:
    case "aluno":
        matricula = input("Digite a matrícula do aluno: ")
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(4)]
        pessoa = AlunoHeranca(matricula, nome, idade, notas)
        pessoa.estudar()
        print(f"Média do aluno: {pessoa.calcular_media():.2f}")
    case "professor":
        matricula = input("Digite a matrícula do professor: ")
        nome = input("Digite o nome do professor: ")
        idade = int(input("Digite a idade do professor: "))
        formacao = input("Digite a formação: ")
        disciplina = input("Digite a disciplina: ")
        carga_horaria = int(input("Digite a carga horária: "))
        salario = float(input("Digite o salário: "))
        pessoa = Professor(matricula, nome, idade, formacao, disciplina, carga_horaria, salario)
        pessoa.lecionar()
    case _:
        print("Tipo inválido.")
