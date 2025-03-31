class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Preço: R${self.preco:.2f}")

livro1 = Livro("1984", "George Orwell", 1949, 39.90)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 1899, 29.90)

livro1.exibir_informacoes()
livro2.exibir_informacoes()