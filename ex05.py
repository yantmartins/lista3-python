class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora

    def incrementar_horas(self, horas):
        self.horas_trabalhadas += horas


nome = input("Digite o nome do funcionário: ")
sobrenome = input("Digite o sobrenome do funcionário: ")
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora: "))


func = Funcionario(nome, sobrenome, horas_trabalhadas, valor_hora)


print(f"\nFuncionário: {func.nome_completo()}")
print(f"Salário atual: R$ {func.calcular_salario():.2f}")


horas_extra = float(input("\nDigite as horas extras trabalhadas: "))
func.incrementar_horas(horas_extra)


print(f"Total de horas trabalhadas: {func.horas_trabalhadas}")
print(f"Novo salário: R$ {func.calcular_salario():.2f}")
