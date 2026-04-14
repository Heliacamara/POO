class Livro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor

class Biblioteca:
    def __init__(self,nome):
        self.nome=nome
        self.lista_de_livros=[]

    def adicionar_livros(self):
        self.lista_de_livros.append()