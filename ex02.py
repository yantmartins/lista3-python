class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, nova_editora):
        self.editora = nova_editora

    def listar_qtde_paginas(self):
        print(f"O livro '{self.nome}' possui {self.paginas} páginas.")



nome = input("Digite o nome do livro: ")
autor = input("Digite o nome do autor: ")
editora = input("Digite o nome da editora: ")
paginas = int(input("Digite a quantidade de páginas: "))


livro = Livro(nome, autor, editora, paginas)


livro.listar_qtde_paginas()
print(f"Autor: {livro.autor}")
print(f"Editora atual: {livro.editora}")


nova_editora = input("Digite o nome da nova editora: ")
livro.alterar_editora(nova_editora)


print(f"Editora atualizada: {livro.editora}")
