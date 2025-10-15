from datetime import datetime, date

class Agenda:
    def __init__(self, dia, mes, ano, anotacao=""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self):
        try:
            datetime(self.ano, self.mes, self.dia)
            return True
        except ValueError:
            return False

    def anotar_tarefa(self, texto):
        self.anotacao = texto

    def mostrar_anotacao(self):
        if self.validar_data():
            print(f"{self.dia:02d}/{self.mes:02d}/{self.ano}: {self.anotacao}")
        else:
            print("Data inválida. Não é possível mostrar anotação.")



dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))


agenda = Agenda(dia, mes, ano)


if agenda.validar_data():
    print(" Data válida!")
else:
    print(" Data inválida!")


texto = input("Digite a anotação para essa data: ")
agenda.anotar_tarefa(texto)


print("\n--- Anotação registrada ---")
agenda.mostrar_anotacao()
