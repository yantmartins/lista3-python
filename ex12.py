class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"Reproduzindo o filme '{self.nome}'")


class Acao(Filme):
    def explodir(self):
        print("BOOM! Cena de ação intensa!")


class Drama(Filme):
    def chorar(self):
        print("Cena emocionante...")


class Suspense(Filme):
    def assustar(self):
        print("Algo assustador aconteceu!")


nome = input("Digite o nome do filme: ")
duracao = int(input("Digite a duração do filme (minutos): "))
tipo = input("Digite o gênero (acao, drama, suspense): ").strip().lower()

match tipo:
    case "acao":
        filme = Acao(nome, duracao)
    case "drama":
        filme = Drama(nome, duracao)
    case "suspense":
        filme = Suspense(nome, duracao)
    case _:
        filme = Filme(nome, duracao)

filme.play()

match tipo:
    case "acao":
        filme.explodir()
    case "drama":
        filme.chorar()
    case "suspense":
        filme.assustar()
