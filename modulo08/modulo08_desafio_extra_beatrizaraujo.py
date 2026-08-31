class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print("Livro emprestado!")
                return

        print("Livro não disponível.")

    def listar_livros(self):
        for livro in self.livros:
            print(livro.titulo, "-", "Disponível" if livro.disponivel else "Emprestado")


biblioteca = Biblioteca()

livro1 = Livro("O Pequeno Príncipe")
livro2 = Livro("Harry Potter")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()

biblioteca.emprestar("O Pequeno Príncipe")

biblioteca.listar_livros()